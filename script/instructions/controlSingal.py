circuit_control_label = {
    'MIR_RST','INT_CHK','INT_ACCEPT','INT_SVC_END',
    "ALU_OUT","H8\~L8", "ALU_M", "ALU_S0", "ALU_S1", "ALU_S2", "ALU_S3", "ALU_S3", "~ALU_CN",
    "ALU_A_IN","ALU_A_OUT",
    "ALU_B_S0","ALU_B_S1","ALU_B_OUT",
    "PAR_IN", "FLASH_OUT",
    "RAR_IN",
    "RAM_IN","RAM_OUT","RAM_LATCH_OUT",
    "PC_IN", "PC_OUT" ,"PC_INC_OUT" , "PC_INC",
    "PSW_IN","PSW_OUT","PSW_ALU_FLAG_IN",
    "Ri_BANK_IN","Ri_IN","Ri_OUT",
    "ACC_OUT" ,"ACC_S0", "ACC_S1",
    "B_IN","B_OUT",
    "TMP_OUT","TMP_F0","TMP_F1","TMP_SIS0","TMP_SIS1",
    "IR_IN", "IR_OUT",}

control_function = {
    "ALU_ADD" : ('ALU_S3','ALU_S0','~ALU_CN'),
    "ALU_ADDD": ('ALU_S3','ALU_S0'),
    "ALU_SUB" : ('ALU_S2','ALU_S1'),
    "ALU_SUBB": ('ALU_S2','ALU_S1','~ALU_CN'),
    "ALU_AND" : ('ALU_M','ALU_S3','ALU_S1','ALU_S0'),
    "ALU_OR"  : ('ALU_M','ALU_S3','ALU_S2','ALU_S1'),
    "ALU_XOR" : ('ALU_M','ALU_S2','ALU_S1'),
    "ALU_NOT" : ('ALU_M',),
    "ALU_INC" : ('~ALU_CN',),
    "ALU_DEC" : ('~ALU_CN','ALU_S3','ALU_S2','ALU_S1','ALU_S0'),
    "ACC_IN" :  ('ACC_S0', 'ACC_S1'),
    "ACC_SHIFT_LEFT" : ('ACC_S0',),
    "ACC_SHIFT_RIGHT" : ('ACC_S1',),
}

if __name__ == '__main__':
    print(len(circuit_control_label))