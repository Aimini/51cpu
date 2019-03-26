import inuntil
import pathlib
path =  pathlib.Path("eeprom-bin")/"IPS.bin"

def IPS_conuter(doit):
    for ISREpt in range(2**1):
        for ISRMSB in range(2**2):
            for ISRQn in range(2**2):
                for IE in range(2**2):
                    for IP in range(2**2):
                        for IRRQn in range(2**2):
                            doit(ISREpt,ISRMSB,ISRQn,IE,IP,IRRQn)


def least_sgn(number):
    zero = 0
    if number == 0:
        zero = 1
    msb = 0
    while number > 1 and number & 0x1 == 0:
            number >>= 1
            msb += 1
    return msb,zero

def bitop_gen(f):
    def gen(ISREpt,ISRLSB,ISRQn,IE,IP,IRRQn):
        # generate signal which from IRRQn+IE+IP
        O = 0x00
        if IE & 0x1 == 1 and ISRQn &0x1 == 0:
            if IP&0x1 == 0:
                O += (IRRQn&0x1) << 2
            else:
                O += IRRQn&0x1

        if IE & 0x2 == 0x2 and ISRQn &0x2 == 0:
            if IP&0x2 == 0: 
                O += (IRRQn&0x2) << 2
            else:
                O += IRRQn&0x2
        lsb,empty = least_sgn(O)
        
        if empty == 0 and (ISREpt or lsb < ISRLSB):
            IRQ = 1
            IRRn =  lsb  & 0x1 # which one  be selected
            IRRDn = IRRQn & (0xF&(~(1 << IRRn)))
            result = (1 << lsb) + (IRRDn << 4) +(IRQ << 6) + (IRRn << 7)
        else:
            result = (IRRQn << 4)
        
        f.write(inuntil.write_as_bin(result))
    return gen

f = open(path,'wb')    
IPS_conuter(bitop_gen(f))
f.close()

