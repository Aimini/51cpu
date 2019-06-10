ext_serial = {
    SFR: {
        0x98: "SCON",
        0x99: "SBUF",
    },
    regs: {
        "SBUF": new reg(),
        "SCON": new reg()
    }
}
ext_serial.regs.SBUF.setlistener = function (val_old, val_new) {
    document.body.innerText += val_new;
}

function reg(value = 0, bitlen = 8) {
    this._value = value;
    this.bitlen = bitlen
    this.max = Math.pow(2, bitlen) - 1

    this.getlistener = []
    this.setlistener = []
}
reg.prototype.set = function (val) {
    for (let one of this.setlistener) {
        one(this._value, val);
    }
    this._value = val;
    return this;
}
reg.prototype.get = function () {
    for (let one of this.getlistener) {
        one(this._value);
    }
    return this._value
}

reg.prototype.inc = function () {
    this.set(this._value + 1)
    return this
}

reg.prototype.dec = function () {
    this.set(this._value - 1)
    return this
}



function _51cpu() {
    this.A = new reg()
    this.B = new reg()
    this.PSW = new reg()
    this.SP = new reg(7)
    this.PC = new reg(0,16)
    this.DPTR = new reg(0,16)
    this.DPL = new reg()
    this.DPH = new reg()
    this.ERAM = []
    this.IRAM = []
    this.IDATA = []
    this.SFR = {
        0x81: "SP",
        0x82: "DPL",
        0x83: "DPH",
        0xD0: "PSW",
        0xE0: "A",
        0xF0: "B",
    }
    let array_get = function (index) {
        return this[index];
    }

    this.IDATA.__proto__.get = array_get

    for (let i = 0; i < 128; ++i)
        this.IRAM.push(0);

    let cpu_ref = this;
    this.DPL.get = function () {
        this.__proto__.get.call(this)
        return (cpu_ref.DPTR.get() & 0xFF)
    }

    this.DPL.set = function (val_new) {
        cpu_ref.DPL.__proto__.set.call(this, val_new)
        let val = cpu_ref.DPTR.get()
        val &= 0xFF00
        val += val_new
        cpu_ref.DPTR.set(val)
    }


    this.DPH.get = function () {
        this.__proto__.get.call(this)
        return (cpu_ref.DPTR.get() & 0xFF00) >> 8
    }
    this.DPH.set = function (val_new) {
        this.__proto__.set.call(this, val_new)
        let val = cpu_ref.DPTR.get()
        val &= 0x00FF
        val += (val_new << 8)
        cpu_ref.DPTR.set(val)
    }

    //-------Parity Flag: PSW.0 specialization--------
    this.PSW.set = function(value_new){
        let a = cpu_ref.A.get()
        let parity = cpu_ref.parity()
        this.__proto__.set.call(this,((value_new & 0xFE) + parity))
    }

    this.A.set = function(value_new){
        this.__proto__.set.call(this,value_new)
        let parity = cpu_ref.parity()
        cpu_ref.PSW.set(cpu_ref.PSW.get())
    }
    
}

//return parity flag generate by A
_51cpu.prototype.parity = function(){
    let a = this.A.get()
    return (a ^ (a >> 1) ^(a >> 2)^(a >> 3)^(a>>4)^(a>>5)^(a>>6)^(a>>7))&0x01
}

_51cpu.prototype.extend = function (ext_package) {


}

_51cpu.prototype.reset = function () {
    this.A.set(0)
    this.B.set(0)
    this.PSW.set(0)
    this.SP.set(7)
    this.PC.set(0)
    this.DPTR.set(0)
}


// paramter : addr; addr that < 0x100
// get RAM value by addr , whne add < 0x80, 
// found value in IRAM, otherwise using SFR
// map to read register' vaule
_51cpu.prototype.get_iram_cell = function (addr) {
    let cpu_ref = this
    return {
        set: function (val) {
            cpu_ref.IRAM[addr] = val
        },
        get: function () {
            return cpu_ref.IRAM[addr]
        }
    }
}
_51cpu.prototype.get_ram_cell = function (addr) {
    if (addr < 0x80)
        return this.get_iram_cell(addr)
    else {
        let sfrname = this.SFR[addr]
        let sfr_reg = this[sfrname]
        if(sfr_reg){
            return sfr_reg
        }else{
            err = "invalid SFR address: 0x" + addr.toString(16)
            if(strict = 0)
                throw new RangeError(err)
            else{
                console.log(err)
                return new reg()
            }
        }
    }
}


_51cpu.prototype.op_inc = function (value) {
    let val = value.get()
    let mask = 0xFF
    if (value.bitlen)
        mask = Math.pow(2, value.bitlen) - 1
    val = (val + 1) & mask
    value.set(val)
}

_51cpu.prototype.op_dec = function (value) {
    let val = value.get()
    let mask = 0xFF
    if (value.bitlen)
        mask = Math.pow(2, value.bitlen) - 1
    val = val <= 0 ? mask : val - 1
    value.set(val)
    return val
}
_51cpu.prototype.op_move = function (dest, src) {
    if (typeof (src) == "number")
        dest.set(src)
    else
        dest.set(src.get())
}

_51cpu.prototype.op_rr = function (store_cell) {

}

_51cpu.prototype.op_rl = function (store_cell) {

}

_51cpu.prototype.op_add_offset = function (offset_raw) {
    let pt = this.PC.get()
    let offset = 0
    if (offset_raw >= 0x80) {
        offset = - (256 - offset_raw);
    } else {
        offset = offset_raw
    }
    this.PC.set(pt + offset)
}

_51cpu.prototype.op_push = function (store_cell) {
    let sp = this.SP.inc().get()
    this.IRAM[sp] = typeof (store_cell) == "number" ? store_cell : store_cell.get()
    return this
}

_51cpu.prototype.op_pop = function (store_cell) {
    let sp = this.SP.get()
    store_cell.set(this.IRAM[sp])
    this.SP.dec()
    return this
}


_51cpu.prototype.op_call = function (addr) {
    this.op_push(this.PC.get() & 0xFF)
    this.op_push((this.PC.get() >> 8) & 0xFF)
    this.PC.set(addr)
    return this
}

_51cpu.prototype.op_ret = function () {
    let temp = new reg()
    let low8bit = 0
    let high8bit = 0
    this.op_pop(temp)
    high8bit = temp.get()
    this.op_pop(temp)
    low8bit = temp.get()
    this.PC.set((high8bit << 8) + low8bit)
    return this
}

_51cpu.prototype.fetch_opcode = function () {
    let pt = this.PC.get()
    let cpu_ref = this;
    let opcode = {
        value: cpu_ref.IDATA.get(pt),
        test: function (target_opcode, mask = 0xFF) {
            return (this.value & mask) == target_opcode
        }
    }
    this.PC.inc()

    let Ri_addr = (this.PSW.get() & 0x18) + (0x01 & opcode.value);
    let Rn_addr = (this.PSW.get() & 0x18) + (0x07 & opcode.value);

    let Ri = this.IRAM[Ri_addr]

    opcode.get_Ri = function () {
        return {
            set: function (val) {
                cpu_ref.IRAM[Ri] = val
            },
            get: function () {
                return cpu_ref.IRAM[Ri]
            }
        }
    }

    opcode.get_Rn = function () {
        return {
            set: function (val) {
                cpu_ref.IRAM[Rn_addr] = val
            },
            get: function () {
                return cpu_ref.IRAM[Rn_addr]
            }
        }
    }

    opcode.fetch_addr11 = function () {
        let comb = ((this.value & 0xE0) << 3) + cpu_ref.IDATA[cpu_ref.PC.get()]
        let next_PC = cpu_ref.PC.inc().get()
        comb += (next_PC & 0xF800)
        return comb
    }

    return opcode
}

_51cpu.prototype.fetch_const16 = function () {
    let pt = this.PC.get()
    let high8bit = this.IDATA.get(pt)
    let low8bit = this.IDATA.get(pt + 1)
    this.PC.set(pt + 2)
    return (high8bit << 8) + low8bit
}

_51cpu.prototype.fetch_const = function () {
    let value = this.IDATA.get(this.PC.get())
    this.PC.inc()
    return value
}

_51cpu.prototype.fetch_direct = function () {
    let addr = this.IDATA.get(this.PC.get())
    this.PC.inc()
    return this.get_ram_cell(addr)
}

_51cpu.prototype.fetch_bit = function () {
    let pt = this.PC.get()
    let bit_addr = this.IDATA.get(pt)
    let addr = 0
    let bit_index = bit_addr & 0x07
    if (bit_addr < 0x80) {
        addr = 0x20 + (bit_addr >> 3)
    } else {
        addr = bit_addr & 0xF8
    }

    let cpu_ref = this
    let mem_reg = cpu_ref.get_ram_cell(addr)



    let mem_cell = {
        set: b => {
            let value = mem_reg.get()
            let set_value = (b << bit_index) | (value & (~(1 << bit_index)))
            mem_reg.set(set_value)
        },
        get: () => {
            let value = mem_reg.get()
            return (value >> bit_index) & 0x01
        }
    }
    this.PC.set(pt + 1)
    return mem_cell

}


_51cpu.prototype.execute_one = function () {
    let opcode = this.fetch_opcode();
    if (opcode.test(0x00)) {
        //NOP
    } else if (opcode.test(0x01, 0x1F)) {
        //AJMP addr11
        this.PC.set(opcode.fetch_addr11())
    } else if (opcode.test(0x02)) {
        //LJMP addr16
        this.PC.set(this.fetch_const16())
    }
    else if (opcode.test(0x03)) {
        //RR A
        let val = this.A.get()
        let low = val & 0x01
        val = (val >> 1) & 0x7F
        val |= (low << 7)
        this.A.set(val)
    } else if (opcode.test(0x04)) {
        //INC A
        this.op_inc(this.A)
    } else if (opcode.test(0x05)) {
        //INC direct
        this.op_inc(this.fetch_direct())
    } else if (opcode.test(0x06, 0xFE)) {
        //INC @Ri
        this.op_inc(opcode.get_Ri())
    } else if (opcode.test(0x08, 0xF8)) {
        //INC Rn
        this.op_inc(opcode.get_Rn())
    } else if (opcode.test(0x10)) {
        //JBC bit,offset
        let bit_cell = this.fetch_bit()
        let offset_raw = this.fetch_const()
        if (bit_cell.get()) {
            bit_cell.set(0)
            this.op_add_offset(offset_raw)
        }
    } else if (opcode.test(0x11, 0x1F)) {
        //ACALL 0x11
        this.op_call(opcode.fetch_addr11())
    } else if (opcode.test(0x12)) {
        //LCALL addr16
        let addr16 = this.fetch_const16()
        this.op_call(addr16)
    } else if (opcode.test(0x13)) {
        // RRC A
        let psw = this.PSW.get()
        let carry = psw & 0x80

        let a = this.A.get()
        let low = (a & 0x01)

        a = ((a >> 1) & 0x7F) + carry
        psw = (psw & 0x7F) + (low << 7)

        this.A.set(a)
        this.PSW.set(psw)
    } else if (opcode.test(0x14)) {
        //DEC A
        this.op_dec(this.A)
    } else if (opcode.test(0x15)) {
        //DEC direct
        this.op_dec(this.fetch_direct())
    }  else if (opcode.test(0x16,0xFE)) {
        //DEC @Ri
        this.op_dec(opcode.get_Ri())
    }  else if (opcode.test(0x18,0xF8)) {
        //DEC Rn
        this.op_dec(opcode.get_Rn())
    } else if (opcode.test(0x20)) {
        //JB bit, offset
        let b = this.fetch_bit()
        let offset_raw = this.fetch_const()
        if(b.get())
            this.op_add_offset(offset_raw)
    }  else if (opcode.test(0x22)) {
        //RET
        let b = this.op_ret()
    }  else if (opcode.test(0x23)) {
        //RL A
        let value = this.A.get()
        let high = value & 0x80
        value =(( value << 1) + (high >> 7)) & 0xFF
        this.A.set(value)
    } else if (opcode.test(0x74)) {
        //MOV A,#immed
        this.A.set(this.fetch_const())
    } else if (opcode.test(0x75)) {
        //MOV direct,#immed
        let direct = this.fetch_direct()
        let immed = this.fetch_const()
        this.op_move(direct, immed) 
    } else if (opcode.test(0x76, 0xFE)) {
        //  MOV   @Ri,#immed
        let Ri = opcode.get_Ri()
        this.op_move(Ri, this.fetch_const())
    } else if (opcode.test(0x78, 0xF8)) {
        //  MOV   Rn,#immed
        let Rn = opcode.get_Rn()
        this.op_move(Rn, this.fetch_const())
    } else if (opcode.test(0x80)) {
        //SJMP offset
        this.op_add_offset(this.fetch_const())
    } else if (opcode.test(0x85)) {
        // MOV direct_dest, direct_src
        let dest = this.fetch_direct()
        let src = this.fetch_direct()
        this.op_move(dest, src)
    } else if (opcode.test(0xD5)) {
        // DJNZ direct,offset
        let direct = this.fetch_direct()
        let offset = this.fetch_const()
        //consider PSW = 0x02  and ACC = 0
        // when excute PSW dec step,
        // we consider PSW = 0x02 - 1 = 0x01
        // but ACC parity flag make PSW = 0x00
        // but! the standard CPU still using result 0x01 to make judgement
        let value = this.op_dec(direct)
        if(value != 0)
            this.op_add_offset(offset)
    }
}


_51cpu.prototype.next = function (count = 1) {


}

_51cpu.prototype.step = function (count = 1) {

}



_51cpu.prototype.coutinue = function () {

}

