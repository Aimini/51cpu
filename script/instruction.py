import pathlib
import instructions



#--code--#
oscillation_cycle = 12
oscillation_cycle_max = 24
final_instructions = [x for x in instructions.implement.INSTRUCTIONS]

#---------------------------------- RETI,
ignore_intrrupt_check_instrution = [0x32,]

def add_fetch(instructions):
    for one in instructions:
        one.insert(0,['PC_O','PAR_I'])
        one.insert(1,['PC_INC','FLASH_O','IR_I'])
       

    
def add_recount_and_interrupt_check(instructions):
    for one in instructions:
        if len(one) > oscillation_cycle_max:
            print("The instruction {}{} uses an excessively long oscillation period".format())
    

    

directory =  pathlib.Path("../eeprom-bin")


def write_as_bin(number8bit):
   return (number8bit).to_bytes(length=1, byteorder='big')


def write_to_file(file,write_func):
    pass 
        

def write_to_Bin():
   # file = open(directory / "instructions.bin",'bw')
   # write_to_file(file,write_as_bin)
   # file.close()
   add_fetch(final_instructions)
   print(final_instructions)

write_to_Bin()