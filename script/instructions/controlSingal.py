circuit_control_label = {
    'INT_CHK','MIC_CLR',
    "ALU_OUT", "ALU_M", "ALU_S0", "ALU_S1", "ALU_S2", "ALU_S3", "ALU_S3", "ALU_CN",
    "PAR_IN", "FLASH_OUT",
    "IR_IN", "IR_IN",
    "PC_IN", "PC_OUT" ,"PC_INC_OUT" , "PC_INC",
    "ACC_OUT" ,"ACC_S0", "ACC_S1",
    "B_IN","B_OUT"}

control_function = {
    "ALU_ADD" : ('ALU_S3','ALU_S0','ALU_CN'),
    "ALU_ADDD" : ('ALU_S3','ALU_S0'),
    "ALU_SUB" :('ALU_S2','ALU_S1'),
    "ALU_SUBB" :('ALU_S2','ALU_S1','ALU_CN'),
    "ALU_AND": ('ALU_M','ALU_S3','ALU_S1','ALU_S0'),
    "ALU_OR": ('ALU_M','ALU_S3','ALU_S2','ALU_S1'),
    "ALU_XOR":('ALU_M','ALU_S2','ALU_S1'),
    "ALU_NOT" : ('ALU_M',),
    "ACC_IN" : ('ACC_S0', 'ACC_S1'),
    "ACC_SHIFT_LEFT" : ('ACC_S0',),
    "ACC_SHIFT_RIGHT" : ('ACC_S1',),
}