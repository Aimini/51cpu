import pathlib
import math 
BLE    =  0b0000000000000001
BOE    =  0b0000000000000010
ACCLE  =  0b0000000000000100
ACCOE  =  0b0000000000001000
PSWLE  =  0b0000000000010000
PSWOE  =  0b0000000000100000
IPLE   =  0b0000000001000000
IPOE   =  0b0000000010000000
IELE   =  0b0000000100000000
IEOE   =  0b0000001000000000
TCONLE =  0b0000010000000000
TCONOE =  0b0000100000000000
P0LE   =  0b0001000000000000
P0RLE  =  0b0010000000000000
P0OE   =  0b0100000000000000
SPLE   =  0b1000000000000000
SPOE   = 0b10000000000000000

MMIO = dict() 
MMIO[0xF0] = "B"
MMIO[0xE0] = "ACC"
MMIO[0xD0] = "PSW"
MMIO[0xB8] = "IP"
MMIO[0xA8] = "IE"
MMIO[0x99] = "SBUF"
MMIO[0x98] = "SCON"
MMIO[0x88] = "TCON"
MMIO[0x83] = "DPH"
MMIO[0x82] = "DPL"
MMIO[0x81] = "SP"
MMIO[0x80] = "P0"
order = ["P0","SP","DPL","DPH","TCON","IE","IP","PSW","ACC","B","SCON","SBUF"]
directory =  pathlib.Path("eeprom-bin")


def write_as_bin(number8bit):
   return (number8bit).to_bytes(length=1, byteorder='big')

def get_order(REG):
    for idx,x in enumerate(order):
        if x == REG:
            return idx
    return None

def write_to_file(file,write_func,file_count):
    for b in range(256):
        reg = MMIO.get(b,None) 
        if reg is not None:
            order = get_order(reg)
            if order is None:
                print("reg {} must have a order".format(reg))
                exit(-1)
            file.write(write_as_bin(0xFF&((1 << order) >> (file_count*8))))
        else:
             file.write(write_as_bin(0))
        

def write_to_Bin():
    file_num = math.ceil(len(MMIO)/8)
    for file_count in range(file_num):
        file = open(directory / ("MMIO"+str(file_count)+".bin"),'bw')
        write_to_file(file,write_as_bin,file_count)
        file.close()

write_to_Bin()