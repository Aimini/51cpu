import math
import itertools
def print_mi_map(label_order,mi_bin_map,startcounter= 0):
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

def write_as_bin(number8bit):
    return (number8bit).to_bytes(length=1, byteorder='big')


def write_part_of_instrcution(file,max_cycle,instructions_bin,eeprom_index):
    #  generate_fetch_interrupt_flag_instruction(i_impl_flag.FLAG_INSTRUCTION)
    for instruction_hex, one_instruction in enumerate(instructions_bin):
        instruction_len = len(one_instruction)
        for step_order in range(max_cycle):
            if step_order < instruction_len:
                file.write(write_as_bin(0xFF & (one_instruction[step_order] >> (eeprom_index * 8))))
            else:
                file.write(write_as_bin(0))

                
def write_to_bin(mi_bin_map,interrupt_bin,max_cycle,control_signal,file_prefix):
    mi_counter_max = 2**math.ceil(math.log2(max_cycle))
    # 检查用到几个微指令需要几个eeprom，一个eeprom可以控制8个微指令
    eeprom_nmuber = math.ceil(len(control_signal) / 8)
    for x in range(eeprom_nmuber):  
        file = open((file_prefix + "-" + str(x) + ".bin"), 'bw')
        # for ins_with_flag in replace_with_flag(instructions_bin,instruction_flag_bin_map):
        write_part_of_instrcution(file,mi_counter_max,mi_bin_map, x)
        write_part_of_instrcution(file,mi_counter_max,itertools.repeat(interrupt_bin[0],len(mi_bin_map)), x)
        file.close()
    

def print_arduino_file(mi_bin_map,max_cycle,control_signal,file_name):
    mi_counter_max = 2**math.ceil(math.log2(max_cycle))
    # 检查用到几个微指令需要几个eeprom，一个eeprom可以控制8个微指令
    eeprom_nmuber = math.ceil(len(control_signal) / 8)
    file = open((file_name + ".ino"), 'w')
    file.write("int ROM_MAX = {};\n".format(eeprom_nmuber))
    file.write("byte HEX_FILE[{}][{}] = {{\n".format(eeprom_nmuber,len(mi_bin_map)*max_cycle))
    for x in range(eeprom_nmuber): 
        file.write("{\n")
        count = 0 # count for \n
        for instruction_hex, one_instruction in enumerate(mi_bin_map):
            instruction_len = len(one_instruction)
            for step_order in range(max_cycle):
                count += 1
                if step_order < instruction_len:
                    file.write("0x{:0>2X},".format(0xFF & (one_instruction[step_order] >> (x * 8))))
                else:
                    file.write("0x00,")
                if count % max_cycle == 0:
                    file.write("\n")
        file.write("},\n")
    file.write("};")
    file.close()


def print_unused_label(instruction_bin_generater):
    print("------------------------unused control signal:------------------------")
    unused_control_label = set(instruction_bin_generater.control_singal_label) - set(instruction_bin_generater.used_control_label)
    for label in unused_control_label:
        print(label)