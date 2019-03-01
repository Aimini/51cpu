import pathlib,math
import instructions.implement as i_impl
import instructions.info as i_info

oscillation_cycle = 12
oscillation_cycle_max = 24
final_instructions = [x for x in i_impl.INSTRUCTIONS]

# ---------------------------------- RETI,
ignore_interrupt_check_instruction = [0x32, ]


def add_fetch(instructions):
    for one in instructions:
        one.insert(0, ['PC_OUT', 'PAR_IN'])
        one.insert(1, ['PC_INC', 'FLASH_OUT', 'IR_IN'])


def add_recount_and_interrupt_check(instructions):
    for idx, one in enumerate(instructions):
        # check instruction's oscil cycle len
        instruction_len = len(one)
        if instruction_len > oscillation_cycle_max:
            print("The instruction {}(0x{:0>2x})"
                  " uses an excessively long oscillation period".format(i_info.HEX_TO_NAME[idx], idx))
        add_where = math.ceil(instruction_len/oscillation_cycle)*oscillation_cycle
        one.extend([[] for __ in range(add_where - instruction_len)])
        one[add_where - 1].append('MIC_CLR')

        if idx in ignore_interrupt_check_instruction:
            print("{}(0x{:0>2x}) ignore interrupt check.".format(i_info.HEX_TO_NAME[idx], idx))
        else:
            one[add_where - 1].append('INT_CHK')


directory = pathlib.Path("../eeprom-bin")


def write_as_bin(number8bit):
    return (number8bit).to_bytes(length=1, byteorder='big')


def write_to_file(file, write_func):
    pass


def print_instructions(instructions):
    for x in instructions:
        print(x)

def write_to_bin():
    # file = open(directory / "instructions.bin",'bw')
    # write_to_file(file,write_as_bin)
    # file.close()
    add_fetch(final_instructions)
    add_recount_and_interrupt_check(final_instructions)
    print_instructions(final_instructions)


write_to_bin()
