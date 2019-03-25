circuit_control_label = [
    'MIC_RST', 'INT_CHK', 'INT_SVC_END',

    "PC_S0", "PC_OUT", "PC_INC",
    "PAR_IN", "FLASH_OUT",
    "DPTR_IN","DPTR_OUT",

    "ADT_L8E","ADT_H8E","DTOALU",
    "ALUADDRTE","ALUTOADDR",

    "ALU_OUT","ALU_EXTOUT", "ALU_M", "ALU_S0", "ALU_S1", "ALU_S2", "ALU_S3", "ALU_CN+0_S0",
    "ALU_A_S0","ALU_A_S1","ALU_A_S2",
    "ALU_B_S0","ALU_B_S1","BOP_CLR_CY",

    

    "RAM_IN","RAM_OUT","RAM_LATCH_OUT",
    "RAR_IN","PC_S1","RAR_ADDRS0","RAR_ADDRS1",
    "ACC_IN","ACC_OUT",
    "B_IN","B_OUT",
    "SP_IN","SP_OUT",
    "TMP_S0",'TMP_S1',"TMP_OUT","TMP_SIS0","TMP_SIS1",
    "BOP_IN","BOP_OUT", "TMP_BOP_BS0","TMP_BOP_BS1","TMP_BOP_BS2","TMP_BOP_ADDS0","TMP_BOP_ADDS1",
    "TMP_DA_OUT","TMP_BITADDR_OUT",
    "IR_IN", "IR_OUT",

    "PSW_FLAG_IN","PSW_USER_IN","PSW_OUT","PSW_BUS/FLAG","DEBUG_HALT","PC_S2","ALU_CN+0_S1",
    ]
assert( len(set(circuit_control_label)) == len(circuit_control_label))

control_function = {
    "ALU_ADD" : ('ALU_S3','ALU_S0','ALU_CN+0_S0','ALU_OUT'),
    "ALU_ADDC": ('ALU_S3','ALU_S0','ALU_OUT',"ALU_CN+0_S1","ALU_CN+0_S0"),
    "ALU_SUB" : ('ALU_S2','ALU_S1','ALU_OUT'),
    "ALU_SUBB": ('ALU_S2','ALU_S1',"ALU_CN+0_S1",'ALU_OUT'),
    "ALU_AND" : ('ALU_M','ALU_S3','ALU_S1','ALU_S0','ALU_OUT'),
    "ALU_OR"  : ('ALU_M','ALU_S3','ALU_S2','ALU_S1','ALU_OUT'),
    "ALU_XOR" : ('ALU_M','ALU_S2','ALU_S1','ALU_OUT'),
    "ALU_NOT" : ('ALU_M','ALU_OUT'),
    "ALU_DEC" : ('ALU_CN+0_S0','ALU_S3','ALU_S2','ALU_S1','ALU_S0','ALU_OUT'),
    "ALU_INC" :('ALU_OUT',),
    "ALU_A_IN" : ('ALU_A_S0','ALU_A_S1'),
    'ALU_A_L8IN':('ALU_A_S0',),
    'ALU_A_H8IN':('ALU_A_S1',),
    "ALU_A_CNIN" : ('ALU_A_S2',),
    "ALU_A_BITIN" :('ALU_A_S2','ALU_A_S0'),
    "ALU_B_IN" :('ALU_B_S0','ALU_B_S1'),
    "ALU_B_SHIFT_LEFT":('ALU_B_S0',),
    "ALU_B_SHIFT_RIGHT":('ALU_B_S1',),
    "RAR_IDXR0-7":("RAR_ADDRS0",),
    "RAR_IDXR0-1":("RAR_ADDRS0","RAR_ADDRS1"),
    "PSW_LOAD_BUS":('PSW_FLAG_IN','PSW_USER_IN'),
    "PSW_LOAD_ALUFLAG":('PSW_FLAG_IN',"PSW_BUS/FLAG"),
    "TMP_RR_SHIFT":('TMP_S1', 'TMP_SIS0', 'TMP_SIS1'),
    "TMP_RL_SHIFT":('TMP_S0', 'TMP_SIS0', 'TMP_SIS1'),
    'TMP_SHIFT_RIGHT':('TMP_S1',),
    'TMP_SHIFT_CN':('TMP_S0','TMP_SIS0'),
    "TMP_IN":('TMP_S0','TMP_S1'),
    "TMP_BOP_IDX_0_IN":("BOP_IN","TMP_BOP_ADDS0"),
    "TMP_BOP_IDX_OV_IN":("BOP_IN","TMP_BOP_ADDS1"),
    "TMP_BOP_IDX_CY_IN":("BOP_IN","TMP_BOP_ADDS0","TMP_BOP_ADDS1"),
    "TMP_BOP_CPL":('TMP_BOP_BS0',),
    "TMP_BOP_TMPN":('TMP_BOP_BS1',),
    "TMP_BOP_CLR":('TMP_BOP_BS0','TMP_BOP_BS1'),
    "TMP_BOP_LOAD_TMP_ZF":('TMP_BOP_BS2',),
    "TMP_BOP_LOAD_DA_CF":('TMP_BOP_BS0','TMP_BOP_BS2'),
    "TMP_BOP_OR_TMPN":('TMP_BOP_BS1','TMP_BOP_BS2'),
    "TMP_BOP_AND_TMPN":('TMP_BOP_BS0','TMP_BOP_BS1','TMP_BOP_BS2'),
    "NEXT_BYTE":('PC_OUT','PC_INC','PAR_IN'),
    "ALU_A_DBUS_L8IN":('DTOALU','ADT_L8E','ALU_A_S0','ALU_A_S1'),
    "ALU_A_DBUS_H8IN":('DTOALU','ADT_H8E','ALU_A_S0','ALU_A_S1'),
    "ALU_B_DBUS_L8IN":('DTOALU','ADT_L8E','ALU_B_S0','ALU_B_S1'),
    "ALU_B_DBUS_H8IN":('DTOALU','ADT_H8E','ALU_B_S0','ALU_B_S1'),
    "ALU_A_OUT":('ALU_OUT','ALU_CN+0_S0'),
    "RAR-@RI":("RAR_ADDRS0","RAR_ADDRS1",'RAM_OUT','RAR_IN'),
    "RAR-RI_IN":("RAR_ADDRS0",'RAM_IN'),
    "RAR-RI_OUT":("RAR_ADDRS0",'RAM_OUT'),
    "ALUEXT_ADDR11":("ALU_S1", "ALU_S2", "ALU_S3","ALU_EXTOUT"),
    "ALUEXT_XCHD":("ALU_S0", "ALU_S2", "ALU_S3","ALU_EXTOUT"),
    "ALUEXT_TWO_CMP":("ALU_S0", "ALU_S1", "ALU_S3","ALU_EXTOUT"),
    "ALUEXT_SWAP":("ALU_S0", "ALU_S1", "ALU_S2","ALU_EXTOUT"),
    "PC_IN":("PC_S0",),
    "PC_ZFIN":("PC_S1",),
    "PC_/ZFIN":("PC_S1","PC_S0"),
    "PC_BITQIN":("PC_S2",),
    "PC_/BITQIN":("PC_S2","PC_S0"),
    "PC_CyIN":("PC_S2","PC_S1"),
    "PC_/CyIN":("PC_S2","PC_S1","PC_S0"),
}

    

if __name__ == '__main__':
    print(len(circuit_control_label))