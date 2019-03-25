import pathlib,math,os,sys
import copy

import instructions.implement as i_impl
import instructions.info as i_info
import instructions.Component as i_comp
import instructions.implementWithFlag as i_impl_flag
import instructions.controlSingal

oscillation_cycle = 8
oscillation_cycle_max = 16
instructionControlSignal = i_comp.InstructionControlSignal(instructions.controlSingal.circuit_control_label)
instructionControlSignal.function = instructions.controlSingal.control_function
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
        add_where = math.ceil(instruction_len/oscillation_cycle)*oscillation_cycle
        one.extend([[] for __ in range(add_where  - instruction_len)])
        if add_where < oscillation_cycle_max:
            one.append(['MIC_RST'])

        if idx in ignore_interrupt_check_instruction:
            print("{}(0x{:0>2x}) ignore interrupt check.".format(i_info.HEX_TO_NAME[idx], idx))
        else:
            one[add_where - 1].append('INT_CHK')
        
        
        if len(one) > oscillation_cycle_max:
            print("The instruction {}(0x{:0>2x})  uses an excessively long oscillation period".format(i_info.HEX_TO_NAME[idx], idx))
            exit(-1)


def generate_complete_instruction(instructions):
    new_instructions_list = []
    for idx,x in enumerate(instructions):
    
        if isinstance(x,list):
            new_instructions_list.append(x)
            if len(x) == 0:
                print('no implement instruction {}(0x{:0>2X})'.format(i_info.HEX_TO_NAME[idx],idx))
        elif x > 0:
            new_instructions_list.append(copy.deepcopy(new_instructions_list[x]))
        elif x == 0:
            new_instructions_list.append([])
            print('no action instruction {}(0x{:0>2X})'.format(i_info.HEX_TO_NAME[idx],idx))
        elif x == -1:
            new_instructions_list.append(copy.deepcopy(new_instructions_list[idx - 1]))
        else:
            print("can't complete instructions 0x{0:2>X}.".format(idx))
            exit(-1)
    return new_instructions_list


def generate_fetch_interrupt_instruction(instructions):
    new_instructions_list = generate_complete_instruction(instructions)
    add_fetch(new_instructions_list)
    add_recount_and_interrupt_check(new_instructions_list)
    return new_instructions_list


def generate_fetch_interrupt_flag_instruction(instrcutions):
    new_instructions = dict()
    for k,v in instrcutions.items():
        new_instructions.update({k:dict(zip(v.keys(),generate_fetch_interrupt_instruction(v.values())))})
    return new_instructions
        

directory = pathlib.Path("eeprom-bin")
file_prefix = "instruction"


def write_as_bin(number8bit):
    return (number8bit).to_bytes(length=1, byteorder='big')


def write_to_file(file, write_func):
    pass


def print_instructions(instructions):
    for idx,x in enumerate(instructions):
        print("{:<8}(0x{:0>2X}) -> ".format(i_info.HEX_TO_NAME[idx],idx),end='')
        print(x)


def write_part_of_instrcution(file,max_cycle,instructions_bin,eeprom_index):
    flags_counter_max = 2**len(i_impl_flag.FLAG)
    #  generate_fetch_interrupt_flag_instruction(i_impl_flag.FLAG_INSTRUCTION)
    for instruction_hex, one_instruction in enumerate(instructions_bin):
        instruction_len = len(one_instruction)
        for step_order in range(max_cycle):
            if step_order < instruction_len:
                file.write(write_as_bin(0xFF & (one_instruction[step_order] >> (eeprom_index * 8))))
            else:
                file.write(write_as_bin(0))

def generate_instruction_flag_bin_map(instruction_with_flag,instructionControlSignal):
    instruction_flag_bin_map = dict()
    for flag,instructions_map in instruction_with_flag.items():
        hex = instructions_map.keys()
        instructions_list = instructions_map.values()
        try:
            instructions_bin,used_control_label =  instructionControlSignal.create_instruction_bin_list(instructions_list)
            instruction_flag_bin_map.update({flag: dict(zip(hex,instructions_bin))})
        except i_comp.MINotFoundError  as e:
            print("flag '{}':unknow control singal label '{}' in instruction 0X{:0>2X} at step {}:".format(flag, e.key, list(hex)[e.order], e.step))
            exit(-1)
    return instruction_flag_bin_map


def replace_with_flag(instructions_bin,instruction_flag_bin_map):
    flags_counter_max = 2**len(i_impl_flag.FLAG)
    for flags_counter in range(flags_counter_max):
        instruction_with_flag_bin = [x for x in instructions_bin]
        for flag_idx,flag_name in enumerate(i_impl_flag.FLAG):
            if flags_counter & (1<<flag_idx) != 0:
                for hex,mi in instruction_flag_bin_map[flag_name].items():
                    instruction_with_flag_bin[hex] = mi
        yield instruction_with_flag_bin         


def print_use_label(instruction_bin_generater):
    print("used control signal:")
    used_control_label = sorted(instruction_bin_generater.used_control_label, key=lambda label: instruction_bin_generater.contol_labels_bin[label])
    for label in used_control_label:
        print(("{:<16} {:0>"+ str(len(instruction_bin_generater.control_singal_label)) +"b}").format(label,instruction_bin_generater.contol_labels_bin[label]))


def print_mi_map(startcounter,label_order,mi_bin_map):
    l = len(mi_bin_map)
    count = 0
    for key in label_order:
        v = mi_bin_map[key]
        chip_n = math.floor( count / 8)
        if count % 8 == 0:
            print("---chip " + str(chip_n))
        if count >= startcounter:
           counter_str = str(count - startcounter)
        else:
            counter_str = ''
        print(("{:<16} {:>2} {:0>8b}").format(key,counter_str, (v >> 8*chip_n)&0xFF))

        count += 1
        

def write_to_bin():
    # file = open(directory / "instructions.bin",'bw')
    # write_to_file(file,write_as_bin)
    # file.close()
    
    final_instructions = generate_fetch_interrupt_instruction(i_impl.INSTRUCTIONS)
    print_instructions(final_instructions)
    try:
        instructions_bin, use_control_label = instructionControlSignal.create_instruction_bin_list(final_instructions)
        print_use_label(instructionControlSignal)
    except i_comp.MINotFoundError  as e:
        print("unknow control singal label '{}' in instruction 0X{:0>2X} at step {}:".format( e.key, e.order, e.step))
        exit(-1)
    # final_instructions_with_flag = generate_fetch_interrupt_flag_instruction(i_impl_flag.FLAG_INSTRUCTION)
    # instruction_flag_bin_map = generate_instruction_flag_bin_map(final_instructions_with_flag,instructionControlSignal)
    #print_use_label(instructionControlSignal)

    print('---------------chip map------------------')
    print_mi_map(3,instructionControlSignal.control_singal_label,instructionControlSignal.contol_labels_bin)  
    mi_counter_max = 2**math.ceil(math.log2(oscillation_cycle_max))
    # 检查用到几个微指令需要几个eeprom，一个eeprom可以控制8个微指令
    eeprom_nmuber = math.ceil(len(instructionControlSignal.control_singal_label) / 8)
    for x in range(eeprom_nmuber):  
        file = open(directory / (file_prefix + "-" + str(x) + ".bin"), 'bw')
        # for ins_with_flag in replace_with_flag(instructions_bin,instruction_flag_bin_map):
        write_part_of_instrcution(file,mi_counter_max,instructions_bin, x)
        file.close()

    
    

write_to_bin()
