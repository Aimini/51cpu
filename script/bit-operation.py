import pathlib
import inuntil

directory = pathlib.Path("eeprom-bin")
def bitoperation_conuter(doit):
    for bit_in in range(2**1):
            for bs in range(2**3):
                for data in range(2**8):
                    doit(bit_in,bs,data)



def bitop_gen(f):
    def gen(bit_in,bit_select,data):
        mask = (1 << bit_select)
        clear_bit = data & (0xFF&(~mask))
        result = clear_bit | (bit_in << bit_select)
        print('{} {} {:0>8b} {:0>8b}'.format(bit_in,bit_select,data,result))
        f.write(inuntil.write_as_bin(result))
    return gen

f = open(directory / 'bit_op.bin','wb')    
bitoperation_conuter(bitop_gen(f))
