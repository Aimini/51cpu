circuit_control_label = [
    'MIC_RST', 'INT_CHK', 'INT_SVC_END',

    "PC_IN", "PC_OUT" ,"PC_INC_OUT" , "PC_INC",
    "PAR_IN", "FLASH_OUT",
    "DPTR_IN","DPTR_OUT",

    "ADDRDT_L8LE","ADDRDT_H8LE","DTOALU",
    "ALUADDRTE","ALUTOADDR",

    "ALU_OUT","ALU_EXTOUT","H8\~L8", "ALU_M", "ALU_S0", "ALU_S1", "ALU_S2", "ALU_S3", "ALU_S3", "~ALU_CN",
    "ALU_A_L8LE","ALU_A_H8LE","ALU_A_OUT",
    "ALU_B_S0","ALU_B_S1","ALU_B_OUT",

    

    "RAM_IN","RAM_OUT","RAM_LATCH_OUT",
    "RAR_IN","RAR_OUT","RAR_ADDRS0","RAR_ADDRS1",
    "ACC_IN","ACC_OUT",
    "B_IN","B_OUT",
    "SP_IN","SP_OUT",
    "TMP_S0",'TMP_S1',"TMP_OUT","TMP_SIS0","TMP_SIS1",
    "BOP_LE","BOP_OE","BOP_IN/CyIDX", "TMP_BOP_BS0","TMP_BOP_BS1",
    "TMP_DA_OUT","TMP_BITADDR_OUT",
    "IR_IN", "IR_OUT",

    "PSW_IN","PSW_OUT","PSW_ALU_FLAG_IN",
    "TMP_OUT","TMP_F0","TMP_F1","TMP_SIS0","TMP_SIS1",
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
    "ALU_B_IN" :('ALU_B_S0','ALU_B_S1')
}

if __name__ == '__main__':
    print(len(circuit_control_label))