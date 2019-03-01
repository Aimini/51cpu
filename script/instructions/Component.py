# label maybe use
circuit_control_label = {
    'INT_CHK','MIC_CLR',
    "ALU_O", "ALU_M", "ALU_S0", "ALU_S1", "ALU_S2", "ALU_S3", "ALU_S3", "ALU_CN",
    "PAR_IN", "FLASH_OUT",
    "IR_IN", "IR_IN",
    "PC_IN", "PC_OUT" ,"PC_INC_OUT" , "PC_INC",
    "ACC_OUT" ,"ACC_S0", "ACC_S1",
    "B_IN","B_OUT"}

#function obtained by combining signals
ALU_FUNCTION_ADD = ['ALU_CN','ALU_S3','ALU_S0']
ALU_FUNCTION_ADDD = ['ALU_S3','ALU_S0']
ALU_FUNCTION_SUB  = ['ALU_CN' | 'ALU_S2' | 'ALU_S1']
ALU_FUNCTION_SUBB = ['ALU_S2' | 'ALU_S1'   ]
ALU_FUNCTION_AND  = ['ALU_M' | 'ALU_S3' | 'ALU_S1' | 'ALU_S0' ]
ALU_FUNCTION_OR   = ['ALU_M' | 'ALU_S3' | 'ALU_S2' | 'ALU_S1' ]
ALU_FUNCTION_NOT  = ['ALU_M' ]
ALU_FUNCTION_XOR  = ['ALU_M' | 'ALU_S2' | 'ALU_S1']

ACC_FUNCTION_IN = ['ACC_S0' | 'ACC_S1']
ACC_FUNCTION_SHIFT_LEFT = 'ACC_S0' 
ACC_FUNCTION_SHIFT_RIGHT = 'ACC_S1'

# record used label
used_control_label = {}
# Label corresponding binary

MI_LABEL_BIN_MAP = {v: 1 << i for i, v in enumerate(used_control_label)}





    

