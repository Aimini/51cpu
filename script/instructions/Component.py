from functools import reduce
# label maybe use
class InstructionControlSignal():
    def __init__(self,control_singal_label):
        self.control_singal_label = control_singal_label
        self.function = dict()
        
        # Label corresponding binary
        # self.contol_labels_bin = {}
        # self.used_control_label = set()
        # self.instructions_bin = dict
        
        
    def create_instruction_bin_list(self,instructions_list):
        self.instructions_bin = []
        insctructions =self.extract_instruction(instructions_list)

        for instruction_order, one_instruction in  enumerate(insctructions):  # get one instructon
            one_instruction_bin = []
            for step_order,one_step in enumerate(one_instruction): # for each step ,get every mciroinstruction's binary 
                try:
                    one_instruction_bin.append(self.merge_step_microinstructions(one_step))
                except KeyError as e:
                    print("unknow control singal label '{}' in instruction {:X} at step {}:".format(e.args[0], instruction_order,step_order))
                    exit(-1)
            self.instructions_bin.append(one_instruction_bin)
        return self.instructions_bin, self.used_control_label


    def extract_instruction(self,instructions_list):
        flatten_insctruction = []
        #record used control label
        self.used_control_label = set()
        for  one_instruction in  instructions_list:  # get one instructon
            one_flatten_instruction = []
            for one_step in one_instruction: # for each step ,get every mciroinstruction's binary            
                flatten_control_singal_step= list()
                for one_microinstruction in one_step:
                    #some microinstruction maybe a function label
                    if one_microinstruction in self.function.keys():
                        flatten_control_singal_step.extend(self.function[one_microinstruction])
                    else:
                        flatten_control_singal_step.append(one_microinstruction)
                self.used_control_label.update(flatten_control_singal_step)    
                one_flatten_instruction.append(flatten_control_singal_step)
            flatten_insctruction.append(one_flatten_instruction)
        self.genrate_contol_labels_bin()
        return flatten_insctruction


    def genrate_contol_labels_bin(self, just_used_label = False):
        if just_used_label:
             self.contol_labels_bin = {v: 1 << i for i, v in enumerate(self.used_control_label)}
        else:
            self.contol_labels_bin = {v: 1 << i for i, v in enumerate(self.control_singal_label)}


    def merge_step_microinstructions(self,step):
        step_bin = 0
        for x in step:
            step_bin |= self.contol_labels_bin[x]
        return step_bin



    def create_instruction_file(self,instruction_list):
        instruction_bin_list = self.create_instruction_bin_list(instruction_list)


if __name__ == '__main__':
    a = InstructionControlSignal(["A_O","A_I","B_O","B_I","C_S0","C_S1"])
    a.function.update({"C_IN":["C_S0","C_S1"]})
    bin_list,used_label = a.create_instruction_bin_list([
        [["A_O","B_I"],["B_O"]],
        [["C_IN"]]
    ])
    print(bin_list)
    







    

