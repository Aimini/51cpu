import pathlib
import math
from functools import reduce

# label maybe use
MI_LABEL = ["IC_END","INT_ADDR_OUT",
    "PC_IN", "PC_OUT",
    "ALU_A_L8LE","ALU_OUT",
    "DTOALU","ADDRDT_L8E","ADDRDT_H8E","ALUADDRTE",
    "RAR_IN","RAM_IN","SP_IN","SP_OUT",
   ]
# record used label
USED_MI_LABEL = {}
# Label corresponding binary
MI_LABEL_BIN_MAP = {v: 1 << i for i, v in enumerate(MI_LABEL)}
# Micro instruction that takes place at each step of the interrupt cycle
INSTRUCTIONS = [
    ["SP_OUT","DTOALU","ADDRDT_L8E","ALU_A_L8LE"],
    ["ALU_OUT","ALU_A_L8LE","ADDRDT_L8E","RAR_IN"],
    ["PC_OUT", "ALUADDRTE","ADDRDT_L8E","RAM_IN"],
    ["ALU_OUT","ALU_A_L8LE","ADDRDT_L8E","RAR_IN","SP_IN"],
    ["PC_OUT", "ALUADDRTE","ADDRDT_H8E","RAM_IN"],
    ["INT_ADDR_OUT", "PC_IN" ],
    ["IC_END"]
]

directory = pathlib.Path("eeprom-bin")
file_prefix = "int-cycle"


# covert a 8bit number to byte
def write_as_bin(number8bit):
    return (number8bit).to_bytes(length=1, byteorder='big')


def create_instruction_bin(instructions, mi_label_to_bin):
    inss_bin = []
    used_mi = set()
    for one in instructions:  # get each step
        bin_code = 0
        for mi_label in one:  # get each microinstruction
            b = mi_label_to_bin.get(mi_label, None)  # get microinstructon's binary code
            if b is not None:
                bin_code |= b  # if find binary code in map,append it to instruction binary code
            else:
                print("unknow mi label:" + mi_label)
                exit(-1)
            used_mi.add(mi_label)  # add used microinstruction
        inss_bin.append(bin_code)
    return inss_bin, used_mi


def print_mi_map(label_order,mi_bin_map):
    l = len(mi_bin_map)
    s = '{:0>' + str(l) + 'b}'  # fill 0 ,aligin right
    count = 0
    for key in label_order:
        v = mi_bin_map[key]
        print(("{:<12}" + s).format(key, v >> 8*math.floor( count / 8)))
        count += 1
        if count % 8 == 0:
            print()



def write_to_file():
    instructions_bin, used_mi = create_instruction_bin(INSTRUCTIONS, MI_LABEL_BIN_MAP)
    unused_mi = set(MI_LABEL).difference(used_mi)
    if len(unused_mi) != 0:
        print("unused micro instruction LABEL:")
        print(",".join(unused_mi))

    for x in range(math.ceil(len(MI_LABEL) / 8)):  # 检查用到几个微指令需要几个eeprom，一个eeprom可以控制8个微指令
        file = open(directory / (file_prefix + "-" + str(x) + ".bin"), 'bw')
        for i in instructions_bin:
            file.write(write_as_bin(0xFF & (i >> (x * 8))))
        file.close()

    print_mi_map(MI_LABEL_BIN_MAP)


write_to_file()
