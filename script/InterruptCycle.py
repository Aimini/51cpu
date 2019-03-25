import pathlib
import math
import inuntil
import instructions.Component as i_comp
from functools import reduce

# label maybe use
MI_LABEL = ["IC_END","INT_ADDR_OUT",
    "PC_IN", "PC_OUT",
    "ALU_A_L8LE","ALU_OUT",
    "DTOALU","ADT_L8E","ADT_H8E","ALUADDRTE",
    "RAR_IN","RAM_IN","SP_IN","SP_OUT","MIC_CLR"
   ]

instructionControlSignal = i_comp.InstructionControlSignal(MI_LABEL)
instructionControlSignal.function = {}

# Micro instruction that takes place at each step of the interrupt cycle
INSTRUCTIONS = [[
    ["SP_OUT","DTOALU","ADT_L8E","ALU_A_L8LE"],
    ["ALU_OUT","ALU_A_L8LE","ADT_L8E","RAR_IN"],
    ["PC_OUT", "ALUADDRTE","ADT_L8E","RAM_IN"],
    ["ALU_OUT","ALU_A_L8LE","ADT_L8E","RAR_IN","SP_IN"],
    ["PC_OUT", "ALUADDRTE","ADT_H8E","RAM_IN"],
    ["INT_ADDR_OUT", "PC_IN" ],
    ["IC_END"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
    ["MIC_CLR"],
]]

directory = pathlib.Path("eeprom-bin")
file_prefix = "int-cycle"




def write_to_file():
    instructions_bin, used_mi = instructionControlSignal.create_instruction_bin_list(INSTRUCTIONS)
    inuntil.print_unused_label(instructionControlSignal)
    inuntil.print_mi_map(instructionControlSignal.control_singal_label,instructionControlSignal.contol_labels_bin,2)
    inuntil.write_to_bin(instructions_bin,16,instructionControlSignal.control_singal_label,str(directory/file_prefix))

    


write_to_file()
