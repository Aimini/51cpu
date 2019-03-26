import inuntil
import pathlib
path =  pathlib.Path("eeprom-bin")/"ISR.bin"

def ISR_conuter(doit):
    for ISE in range(2**1):
        for IRA in range(2**1):
            for IPSQn in range(2**4):
                for Qn in range(2**4):
                    doit(ISE,IRA,IPSQn,Qn)


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
    def gen(ISE,IRA,IPSQn,Qn):
        lsb,empty = least_sgn(Qn)
        
        result = Qn
        if ISE == 1:
            result &= (0xF&(~(1 << lsb)))
        if IRA == 1:
            result |= IPSQn
        result = result + (lsb << 4) + (empty << 6)
        print('{} {} {:0>4b} {:0>4b} {:0>8b}'.format(ISE,IRA,IPSQn,Qn,result))
        f.write(inuntil.write_as_bin(result))
    return gen

f = open(path,'wb')    
ISR_conuter(bitop_gen(f))

