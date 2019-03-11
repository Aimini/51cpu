circuit_control_label = [
    'MIC_RST', 'INT_CHK', 'INT_SVC_END',

    "PC_IN", "PC_OUT", "PC_INC",
    "PAR_IN", "FLASH_OUT",
    "DPTR_IN","DPTR_OUT",

    "ADT_L8E","ADT_H8E","DTOALU",
    "ALUADDRTE","ALUTOADDR",

    "ALU_OUT","ALU_EXTOUT", "ALU_M", "ALU_S0", "ALU_S1", "ALU_S2", "ALU_S3", "~ALU_CN",
    "ALU_A_L8LE","ALU_A_H8LE","ALU_A_OUT",
    "ALU_B_S0","ALU_B_S1","ALU_B_OUT",

    

    "RAM_IN","RAM_OUT","RAM_LATCH_OUT",
    "RAR_IN","RAR_OUT","RAR_ADDRS0","RAR_ADDRS1",
    "ACC_IN","ACC_OUT",
    "B_IN","B_OUT",
    "SP_IN","SP_OUT",
    "TMP_S0",'TMP_S1',"TMP_OUT","TMP_SIS0","TMP_SIS1",
    "BOP_IN","BOP_OUT","BOP_IN/CyIDX", "TMP_BOP_BS0","TMP_BOP_BS1",
    "TMP_DA_OUT","TMP_BITADDR_OUT",
    "IR_IN", "IR_OUT",

    "PSW_FLAG_LE","PSW_USER_LE","PSW_OUT","PSW_BUS/FLAG","PSW_CYIS0","PSW_CYIS1","PSW_CYIS2","PSW_KEEPOV","PSW_KEEPAC"
    ]

control_function = {
    "ALU_ADD" : ('ALU_S3','ALU_S0','~ALU_CN'),
    "ALU_ADDD": ('ALU_S3','ALU_S0'),
    "ALU_SUB" : ('ALU_S2','ALU_S1'),
    "ALU_SUBB": ('ALU_S2','ALU_S1','~ALU_CN'),
    "ALU_AND" : ('ALU_M','ALU_S3','ALU_S1','ALU_S0'),
    "ALU_OR"  : ('ALU_M','ALU_S3','ALU_S2','ALU_S1'),
    "ALU_XOR" : ('ALU_M','ALU_S2','ALU_S1'),
    "ALU_NOT" : ('ALU_M',),
    "ALU_DEC" : ('~ALU_CN','ALU_S3','ALU_S2','ALU_S1','ALU_S0'),
    "ALU_A_IN" : ('ALU_A_L8LE','ALU_A_H8LE'),
    "ALU_B_IN" :('ALU_B_S0','ALU_B_S1'),
    "RAR_IDXR0-7":("RAR_ADDRS0"),
    "RAR_IDXR0-1":("RAR_ADDRS0","RAR_ADDRS1"),
    "PSW_LOAD_BUS":('PSW_FLAG_LE','PSW_USER_LE'),
    "PSW_LOAD_ALUFLAG":('PSW_FLAG_LE',"PSW_FLAG"),
    "PSW_LOAD_CYOV":('PSW_FLAG_LE',"PSW_FLAG","PSW_KEEPAC"),
    "PSW_LOAD_CY":('PSW_FLAG_LE',"PSW_FLAG","PSW_KEEPAC","PSW_KEEPOV"),
    "PSW_CY_ALU":(),
    "PSW_CY_TMP0":("PSW_CYIS0"),
    "PSW_CY_TMPN":("PSW_CYIS1"),
    "PSW_CY_ORL":("PSW_CYIS0", "PSW_CYIS1"),
    "PSW_CY_AND":("PSW_CYIS2"),
    "PSW_CY_DA_FLAG":("PSW_CYIS2","PSW_CYIS0"),
    "PSW_CY_TMP_ZF":("PSW_CYIS2","PSW_CYIS1"),
    "PSW_CY_TMP_NOT_ZF":("PSW_CYIS2","PSW_CYIS1","PSW_CYIS0"),
    "TMP_RR_SHIFT":('TMP_S1', 'TMP_SIS0', 'TMP_SIS1'),
    "TMP_RL_SHIFT":('TMP_S0', 'TMP_SIS0', 'TMP_SIS1'),
    "TMP_IN":('TMP_S0','TMP_S1'),
    "TMP_BOP_CLR_OUT":('BOP_OUT'),
    "TMP_BOP_SET_OUT":('TMP_BOP_BS0','BOP_OUT'),
    "TMP_BOP_CY_OUT":('TMP_BOP_BS1','BOP_OUT'),
    "TMP_BOP_CPL_OUT":('TMP_BOP_BS1','TMP_BOP_BS0','BOP_OUT'),
}

if __name__ == '__main__':
    print(len(circuit_control_label))