STEP_DIRECT_ADDRESS = [['NEXT_BYTE'],['FLASH_OUT','RAR_IN']]
STEP_PC_ADD_OFFSET = [['FLASH_OUT','ALU_A_DBUS_L8IN'],["ALUEXT_TWO_CMP","ALU_B_IN"],["PC_OUT","ALUADDRTE","ALU_A_IN"],['ALU_ADD','ALUADDRTE','ALUTOADDR','PC_IN']]
def PC_add_off_when(label):
    return [['FLASH_OUT','ALU_A_DBUS_L8IN'],["ALUEXT_TWO_CMP","ALU_B_IN"],["PC_OUT","ALUADDRTE","ALU_A_IN"],['ALU_ADD','ALUADDRTE','ALUTOADDR',label]]
def merge_first(a,b):
    r = [_ for _ in a]
    r.extend(b[0])
    return [r,*(b[1:])]

INSTRUCTIONS = [ 
#00,   1,   NOP,       
0,
#01,   2,   AJMP,     addr11
[['IR_OUT','ALU_A_DBUS_H8IN','NEXT_BYTE'],['FLASH_OUT','DTOALU','ADT_L8E','ALU_A_L8IN'],['ALUEXT_ADDR11','ALUADDRTE','ALUTOADDR','PC_IN']],
#02,   3,   LJMP,     addr16
[['NEXT_BYTE'],['FLASH_OUT','ALU_A_DBUS_H8IN','NEXT_BYTE'],['FLASH_OUT','DTOALU','ADT_L8E','ALU_A_L8IN'],['ALU_A_OUT','ALUADDRTE','ALUTOADDR','PC_IN']],
#03,   1,   RR,       A
[['ACC_OUT','TMP_IN'],['TMP_RR_SHIFT'],['TMP_OUT','ACC_IN']],
#04,   1,   INC,      A
[['ACC_OUT','ALU_A_DBUS_L8IN'],['ALU_INC','ADT_L8E','ACC_IN']],
#05,   2,   INC,      direct
[*STEP_DIRECT_ADDRESS,['RAM_LATCH_OUT','ALU_A_DBUS_L8IN'],['ALU_INC','ADT_L8E','RAM_IN']],
#06,   1,   INC,      @R0
[['RAR-@RI'],['RAM_LATCH_OUT','ALU_A_DBUS_L8IN'],['ALU_INC','ADT_L8E','RAM_IN']],
#07,   1,   INC,      @R1
-1,
#08,   1,   INC,      R0
[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_INC','ADT_L8E','RAR-RI_IN']],
#09,   1,   INC,      R1
-1,
#0A,   1,   INC,      R2
-1,
#0B,   1,   INC,      R3
-1,
#0C,   1,   INC,      R4
-1,
#0D,   1,   INC,      R5
-1,
#0E,   1,   INC,      R6
-1,
#0F,   1,   INC,      R7
-1,
#10,   3,   JBC,      bit, offset
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['BOP_IN','TMP_BITADDR_OUT','RAR_IN'],['RAM_LATCH_OUT','TMP_IN'],['NEXT_BYTE'],*PC_add_off_when('PC_BITQIN'),['TMP_BOP_CLR'],['BOP_OUT','RAM_IN']],
#11,   2,   ACALL,    addr11
[['NEXT_BYTE','SP_OUT','ALU_A_DBUS_L8IN'],['ALU_INC','ALU_A_IN','ADT_L8E','RAR_IN'],['PC_OUT','ALUADDRTE','ADT_L8E','RAM_IN'],['ALU_INC','ADT_L8E','RAR_IN','SP_IN'],['PC_OUT','ALUADDRTE','ADT_H8E','RAM_IN'],['IR_OUT','ALU_A_DBUS_H8IN'],['FLASH_OUT','DTOALU','ADT_L8E','ALU_A_L8IN'],['ALUEXT_ADDR11','ALUADDRTE','ALUTOADDR','PC_IN']],
#12,   3,   LCALL,    addr16
[['NEXT_BYTE','SP_OUT','ALU_A_DBUS_L8IN'],['FLASH_OUT','TMP_IN','NEXT_BYTE'],['ALU_INC','ALU_A_IN','ADT_L8E','RAR_IN'],['PC_OUT','ALUADDRTE','ADT_L8E','RAM_IN'],['ALU_INC','ADT_L8E','RAR_IN','SP_IN'],['PC_OUT','ALUADDRTE','ADT_H8E','RAM_IN'],['TMP_OUT','ALU_A_DBUS_H8IN'],['FLASH_OUT','DTOALU','ADT_L8E','ALU_A_L8IN'],['ALU_A_OUT','ALUADDRTE','ALUTOADDR','PC_IN']],
#13,   1,   RRC,      A
[['ACC_OUT','TMP_IN','TMP_BOP_IDX_0_IN'],['TMP_S1', 'TMP_SIS1','TMP_BOP_TMPN'],['TMP_OUT','ACC_IN'],['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['BOP_OUT','PSW_LOAD_BUS']],
#14,   1,   DEC,      A
[['ACC_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','ACC_IN']],
#15,   2,   DEC,      direct
[*STEP_DIRECT_ADDRESS,['RAM_LATCH_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','RAM_IN']],
#16,   1,   DEC,      @R0
[['RAR-@RI'],['RAM_LATCH_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','RAM_IN']],
#17,   1,   DEC,      @R1
-1,
#18,   1,   DEC,      R0
[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','RAR-RI_IN']],
#19,   1,   DEC,      R1
-1,
#1A,   1,   DEC,      R2
-1,
#1B,   1,   DEC,      R3
-1,
#1C,   1,   DEC,      R4
-1,
#1D,   1,   DEC,      R5
-1,
#1E,   1,   DEC,      R6
-1,
#1F,   1,   DEC,      R7
-1,
#20,   3,   JB,       bit, offset
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['BOP_IN','TMP_BITADDR_OUT','RAR_IN'],['RAM_OUT','TMP_IN'],['NEXT_BYTE'],*PC_add_off_when('PC_BITQIN')],
#21,   2,   AJMP,     addr11
1,
#22,   1,   RET,       
[['SP_OUT','RAR_IN','ALU_A_DBUS_L8IN'],['RAM_OUT','TMP_IN'],['ALU_DEC','ALU_A_IN','RAR_IN','ADT_L8E'],['ALU_DEC','ADT_L8E','SP_IN'],['TMP_OUT','ALU_A_DBUS_H8IN'],['RAM_OUT','DTOALU','ADT_L8E','ALU_A_L8IN'],['ALU_A_OUT','ALUTOADDR','ALUADDRTE','PC_IN']],
#23,   1,   RL,       A
[['ACC_OUT','TMP_IN'],['TMP_RL_SHIFT'],['TMP_OUT','ACC_IN']],
#24,   2,   ADD,      A, #immed
[['ACC_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_ADD','ADT_L8E','PSW_LOAD_ALUFLAG','ACC_IN']],
#25,   2,   ADD,      A, direct
[*merge_first(['ACC_OUT','ALU_A_DBUS_L8IN'],STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_ADD','ADT_L8E','PSW_LOAD_ALUFLAG','ACC_IN']],
#26,   1,   ADD,      A, @R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-@RI'],['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_ADD','ADT_L8E','PSW_LOAD_ALUFLAG','ACC_IN']],
#27,   1,   ADD,      A, @R1
-1,
#28,   1,   ADD,      A, R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-RI_OUT','ALU_B_DBUS_L8IN'],['ALU_ADD','ADT_L8E','PSW_LOAD_ALUFLAG','ACC_IN']],
#29,   1,   ADD,      A, R1
-1,
#2A,   1,   ADD,      A, R2
-1,
#2B,   1,   ADD,      A, R3
-1,
#2C,   1,   ADD,      A, R4
-1,
#2D,   1,   ADD,      A, R5
-1,
#2E,   1,   ADD,      A, R6
-1,
#2F,   1,   ADD,      A, R7
-1,
#30,   3,   JNB,      bit, offset
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['BOP_IN','TMP_BITADDR_OUT','RAR_IN'],['RAM_OUT','TMP_IN'],['NEXT_BYTE'],*PC_add_off_when('PC_/BITQIN')],
#31,   2,   ACALL,    addr11
0X11,
#32,   1,   RETI,      
[],
#33,   1,   RLC,      A
[['ACC_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['TMP_S0', 'TMP_SIS1','TMP_BOP_TMPN'],['TMP_OUT','ACC_IN'],['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['BOP_OUT','PSW_LOAD_BUS']],
#34,   2,   ADDC,     A, #immed
[],
#35,   2,   ADDC,     A, direct
[],
#36,   1,   ADDC,     A, @R0
[],
#37,   1,   ADDC,     A, @R1
[],
#38,   1,   ADDC,     A, R0
[],
#39,   1,   ADDC,     A, R1
[],
#3A,   1,   ADDC,     A, R2
[],
#3B,   1,   ADDC,     A, R3
[],
#3C,   1,   ADDC,     A, R4
[],
#3D,   1,   ADDC,     A, R5
[],
#3E,   1,   ADDC,     A, R6
[],
#3F,   1,   ADDC,     A, R7
[],
#40,   2,   JC,       offset
[['NEXT_BYTE'],*PC_add_off_when('PC_CyIN')],
#41,   2,   AJMP,     addr11
1,
#42,   2,   ORL,      direct, A
[*merge_first(['ACC_OUT','ALU_B_DBUS_L8IN'], STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_A_DBUS_L8IN'],['ALU_OR','ADT_L8E','RAM_IN']],
#43,   3,   ORL,      direct, #immed
[*STEP_DIRECT_ADDRESS,['RAM_OUT','ALU_B_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_A_DBUS_L8IN'],['ALU_OR','ADT_L8E','RAM_IN']],
#44,   2,   ORL,      A, #immed
[['ACC_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_OR','ADT_L8E','ACC_IN']],
#45,   2,   ORL,      A, direct
[*merge_first(['ACC_OUT','ALU_A_DBUS_L8IN'],STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_OR','ADT_L8E','ACC_IN']],
#46,   1,   ORL,      A, @R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-@RI'],['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_OR','ADT_L8E','ACC_IN']],
#47,   1,   ORL,      A, @R1
-1,
#48,   1,   ORL,      A, R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-RI_OUT','ALU_B_DBUS_L8IN'],['ALU_OR','ADT_L8E','ACC_IN']],
#49,   1,   ORL,      A, R1
-1,
#4A,   1,   ORL,      A, R2
-1,
#4B,   1,   ORL,      A, R3
-1,
#4C,   1,   ORL,      A, R4
-1,
#4D,   1,   ORL,      A, R5
-1,
#4E,   1,   ORL,      A, R6
-1,
#4F,   1,   ORL,      A, R7
-1,
#50,   2,   JNC,      offset
[['NEXT_BYTE'],*PC_add_off_when('PC_/CyIN')],
#51,   2,   ACALL,    addr11
0x11,
#52,   2,   ANL,      direct, A
[*merge_first(['ACC_OUT','ALU_B_DBUS_L8IN'], STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_A_DBUS_L8IN'],['ALU_AND','ADT_L8E','RAM_IN']],
#53,   3,   ANL,      direct, #immed
[*STEP_DIRECT_ADDRESS,['RAM_OUT','ALU_B_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_A_DBUS_L8IN'],['ALU_AND','ADT_L8E','RAM_IN']],
#54,   2,   ANL,      A, #immed
[['ACC_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_AND','ADT_L8E','ACC_IN']],
#55,   2,   ANL,      A, direct
[*merge_first(['ACC_OUT','ALU_A_DBUS_L8IN'],STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_AND','ADT_L8E','ACC_IN']],
#56,   1,   ANL,      A, @R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-@RI'],['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_AND','ADT_L8E','ACC_IN']],
#57,   1,   ANL,      A, @R1
-1,
#58,   1,   ANL,      A, R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-RI_OUT','ALU_B_DBUS_L8IN'],['ALU_AND','ADT_L8E','ACC_IN']],
#59,   1,   ANL,      A, R1
-1,
#5A,   1,   ANL,      A, R2
-1,
#5B,   1,   ANL,      A, R3
-1,
#5C,   1,   ANL,      A, R4
-1,
#5D,   1,   ANL,      A, R5
-1,
#5E,   1,   ANL,      A, R6
-1,
#5F,   1,   ANL,      A, R7
-1,
#60,   2,   JZ,       offset
[['ACC_OUT','TMP_IN','NEXT_BYTE'],*PC_add_off_when('PC_ZFIN')],
#61,   2,   AJMP,     addr11
1,
#62,   2,   XRL,      direct, A
[*merge_first(['ACC_OUT','ALU_B_DBUS_L8IN'], STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_A_DBUS_L8IN'],['ALU_XOR','ADT_L8E','RAM_IN']],
#63,   3,   XRL,      direct, #immed
[*STEP_DIRECT_ADDRESS,['RAM_OUT','ALU_B_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_A_DBUS_L8IN'],['ALU_XOR','ADT_L8E','RAM_IN']],
#64,   2,   XRL,      A, #immed
[['ACC_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_XOR','ADT_L8E','ACC_IN']],
#65,   2,   XRL,      A, direct
[*merge_first(['ACC_OUT','ALU_A_DBUS_L8IN'],STEP_DIRECT_ADDRESS),['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_XOR','ADT_L8E','ACC_IN']],
#66,   1,   XRL,      A, @R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-@RI'],['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_XOR','ADT_L8E','ACC_IN']],
#67,   1,   XRL,      A, @R1
-1,
#68,   1,   XRL,      A, R0
[['ACC_OUT','ALU_A_DBUS_L8IN'],['RAR-RI_OUT','ALU_B_DBUS_L8IN'],['ALU_XOR','ADT_L8E','ACC_IN']],
#69,   1,   XRL,      A, R1
-1,
#6A,   1,   XRL,      A, R2
-1,
#6B,   1,   XRL,      A, R3
-1,
#6C,   1,   XRL,      A, R4
-1,
#6D,   1,   XRL,      A, R5
-1,
#6E,   1,   XRL,      A, R6
-1,
#6F,   1,   XRL,      A, R7
-1,
#70,   2,   JNZ,      offset
[['ACC_OUT','TMP_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#71,   2,   ACALL,    addr11
0X11,
#72,   2,   ORL,      C, bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['TMP_BOP_TMPN','PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['TMP_BOP_OR_TMPN'],['BOP_OUT','PSW_LOAD_BUS']],
#73,   1,   JMP,      @A+DPTR
[['ACC_OUT','ALU_A_DBUS_L8IN'],["ALU_B_S0","ALU_B_S1","ALUADDRTE","DPTR_OUT"],["ALU_ADD","ALUADDRTE","ALUTOADDR","PC_IN"]],
#74,   2,   MOV,      A, #immed
[['NEXT_BYTE'],['FLASH_OUT','ACC_IN']],
#75,   3,   MOV,      direct, #immed
[*STEP_DIRECT_ADDRESS,['NEXT_BYTE'],['FLASH_OUT','RAM_IN']],
#76,   2,   MOV,      @R0, #immed
[['NEXT_BYTE','RAR-@RI'],['FLASH_OUT','RAM_IN']],
#77,   2,   MOV,      @R1, #immed
-1,
#78,   2,   MOV,      R0, #immed
[['NEXT_BYTE'],['FLASH_OUT','RAR-RI_IN']],
#79,   2,   MOV,      R1, #immed
-1,
#7A,   2,   MOV,      R2, #immed
-1,
#7B,   2,   MOV,      R3, #immed
-1,
#7C,   2,   MOV,      R4, #immed
-1,
#7D,   2,   MOV,      R5, #immed
-1,
#7E,   2,   MOV,      R6, #immed
-1,
#7F,   2,   MOV,      R7, #immed
-1,
#80,   2,   SJMP,     offset
[['NEXT_BYTE'],*STEP_PC_ADD_OFFSET],
#81,   2,   AJMP,     addr11
1,
#82,   2,   ANL,      C, bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['TMP_BOP_TMPN','PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['TMP_BOP_AND_TMPN'],['BOP_OUT','PSW_LOAD_BUS']],
#83,   1,   MOVC,     A, @A+PC
[['ACC_OUT','ALU_A_DBUS_L8IN'],['PC_OUT','ALUADDRTE','ALU_B_IN'],['ALU_ADD','ALUADDRTE','ALUTOADDR','PAR_IN'],['FLASH_OUT','ACC_IN']],
#84,   1,   DIV,      AB
[['B_OUT','ALU_B_DBUS_H8IN','TMP_IN'],['PSW_OUT','TMP_IN','TMP_BOP_IDX_OV_IN','TMP_BOP_LOAD_TMP_ZF'],
['TMP_BOP_IDX_CY_IN','BOP_CLR_CY','BOP_OUT','PSW_LOAD_BUS'],['ACC_OUT','ALU_A_DBUS_L8IN','ALU_B_SHIFT_RIGHT'],
['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],
['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],
['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],
['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],['ALU_SUB','ALU_A_CNIN','TMP_SHIFT_CN','ALU_B_SHIFT_RIGHT'],
['TMP_OUT','ACC_IN'],['ALU_A_OUT','ADT_L8E','B_IN']],
#85,   3,   MOV,      direct, direct
[*STEP_DIRECT_ADDRESS,*merge_first(['RAM_OUT','TMP_IN'],STEP_DIRECT_ADDRESS),['TMP_OUT','RAM_IN']],
#86,   2,   MOV,      direct, @R0
[['RAR-@RI'],*merge_first(['RAM_OUT','TMP_IN'],STEP_DIRECT_ADDRESS),['TMP_OUT','RAM_IN']],
#87,   2,   MOV,      direct, @R1
-1,
#88,   2,   MOV,      direct, R0
[*merge_first(['RAR-RI_OUT','TMP_IN'],STEP_DIRECT_ADDRESS),['TMP_OUT','RAM_IN']],
#89,   2,   MOV,      direct, R1
-1,
#8A,   2,   MOV,      direct, R2
-1,
#8B,   2,   MOV,      direct, R3
-1,
#8C,   2,   MOV,      direct, R4
-1,
#8D,   2,   MOV,      direct, R5
-1,
#8E,   2,   MOV,      direct, R6
-1,
#8F,   2,   MOV,      direct, R7
-1,
#90,   3,   MOV,      DPTR, #immed
[['NEXT_BYTE'],['FLASH_OUT','ALU_A_DBUS_H8IN','NEXT_BYTE'],['FLASH_OUT','DTOALU','ADT_L8E','ALU_A_L8IN'],['ALU_A_OUT','ALUADDRTE','ALUTOADDR','DPTR_IN']],
#91,   2,   ACALL,    addr11
0x11,
#92,   2,   MOV,      bit, C
[['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN','NEXT_BYTE'],['TMP_BOP_TMPN','FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['BOP_OUT','RAM_IN']],
#93,   1,   MOVC,     A, @A+DPTR
[['ACC_OUT','ALU_A_DBUS_L8IN'],['DPTR_OUT','ALUADDRTE','ALU_B_IN'],['ALU_ADD','ALUADDRTE','ALUTOADDR','PAR_IN'],['FLASH_OUT','ACC_IN']],
#94,   2,   SUBB,     A, #immed
[],
#95,   2,   SUBB,     A, direct
[],
#96,   1,   SUBB,     A, @R0
[],
#97,   1,   SUBB,     A, @R1
[],
#98,   1,   SUBB,     A, R0
[],
#99,   1,   SUBB,     A, R1
[],
#9A,   1,   SUBB,     A, R2
[],
#9B,   1,   SUBB,     A, R3
[],
#9C,   1,   SUBB,     A, R4
[],
#9D,   1,   SUBB,     A, R5
[],
#9E,   1,   SUBB,     A, R6
[],
#9F,   1,   SUBB,     A, R7
[],
#A0,   2,   ORL,      C, /bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['TMP_BOP_TMPN'],['TMP_BOP_CPL','PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['TMP_BOP_OR_TMPN'],['BOP_OUT','PSW_LOAD_BUS']],
#A1,   2,   AJMP,     addr11
1,
#A2,   2,   MOV,      C, bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['TMP_BOP_IDX_CY_IN','TMP_BOP_TMPN','PSW_OUT','TMP_IN'],['BOP_OUT','PSW_LOAD_BUS']],
#A3,   1,   INC,      DPTR
[["DPTR_OUT","ALUADDRTE","ALU_A_IN"],['ALU_INC','ALUADDRTE','ALUTOADDR','DPTR_IN']],
#A4,   1,   MUL,      AB
[['ACC_OUT','ALU_B_DBUS_L8IN'],['B_OUT','TMP_IN','TMP_BOP_IDX_0_IN','ALU_A_IN'],
['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],
['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],
['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],
['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','TMP_SHIFT_RIGHT'],['ALU_A_BITIN','ALU_ADD','ALU_B_SHIFT_LEFT','PSW_OUT'],
['ALU_A_OUT','ADT_H8E','B_IN','TMP_IN'],['PSW_OUT','TMP_IN','TMP_BOP_LOAD_TMP_ZF','TMP_BOP_IDX_OV_IN'],
['TMP_BOP_CPL','ALU_A_OUT','ADT_L8E','ACC_IN'],['BOP_OUT','BOP_CLR_CY','PSW_LOAD_BUS','TMP_BOP_IDX_CY_IN']],
#A5,    ,   reserved,  
[['DEBUG_HALT']],
#A6,   2,   MOV,      @R0, direct
[*STEP_DIRECT_ADDRESS,['RAM_OUT','TMP_IN'],['RAR-@RI'],['TMP_OUT','RAM_IN']],
#A7,   2,   MOV,      @R1, direct
-1,
#A8,   2,   MOV,      R0, direct
[*STEP_DIRECT_ADDRESS,['RAM_OUT','TMP_IN'],['TMP_OUT','RAR-RI_IN']],
#A9,   2,   MOV,      R1, direct
-1,
#AA,   2,   MOV,      R2, direct
-1,
#AB,   2,   MOV,      R3, direct
-1,
#AC,   2,   MOV,      R4, direct
-1,
#AD,   2,   MOV,      R5, direct
-1,
#AE,   2,   MOV,      R6, direct
-1,
#AF,   2,   MOV,      R7, direct
-1,
#B0,   2,   ANL,      C, /bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['TMP_BOP_TMPN'],['TMP_BOP_CPL','PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['TMP_BOP_AND_TMPN'],['BOP_OUT','PSW_LOAD_BUS']],
#B1,   2,   ACALL,    addr11
0X11,
#B2,   2,   CPL,      bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN'],['TMP_BOP_TMPN'],['TMP_BOP_CPL'],['BOP_OUT','RAM_IN']],
#B3,   1,   CPL,      C
[['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['TMP_BOP_TMPN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS']],
#B4,   3,   CJNE,     A, #immed, offset
[['ACC_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#B5,   3,   CJNE,     A, direct, offset
[['ACC_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','RAR_IN'],['RAM_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#B6,   3,   CJNE,     @R0, #immed, offset
[['RAR-@RI'],['RAM_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#B7,   3,   CJNE,     @R1, #immed, offset
-1,
#B8,   3,   CJNE,     R0, #immed, offset
[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#B9,   3,   CJNE,     R1, #immed, offset
-1,
#BA,   3,   CJNE,     R2, #immed, offset
-1,
#BB,   3,   CJNE,     R3, #immed, offset
-1,
#BC,   3,   CJNE,     R4, #immed, offset
-1,
#BD,   3,   CJNE,     R5, #immed, offset
-1,
#BE,   3,   CJNE,     R6, #immed, offset
-1,
#BF,   3,   CJNE,     R7, #immed, offset
-1,
#C0,   2,   PUSH,     direct
[*merge_first(['SP_OUT','ALU_A_DBUS_L8IN'],STEP_DIRECT_ADDRESS),['RAM_OUT','TMP_IN'],['ALU_INC','ADT_L8E','RAR_IN','SP_IN'],['TMP_OUT','RAM_IN']],
#C1,   2,   AJMP,     addr11
1,
#C2,   2,   CLR,      bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN'],['RAM_OUT','TMP_IN','TMP_BOP_CLR'],['BOP_OUT','RAM_IN']],
#C3,   1,   CLR,      C
[['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN','TMP_BOP_CLR'],['BOP_OUT','PSW_LOAD_BUS']],
#C4,   1,   SWAP,     A
[['ACC_OUT','ALU_A_DBUS_H8IN'],['ALUEXT_SWAP','ADT_H8E','ACC_IN']],
#C5,   2,   XCH,      A, direct
[*merge_first(['ACC_OUT','TMP_IN'],STEP_DIRECT_ADDRESS),['RAM_OUT','ACC_IN'],['TMP_OUT','RAM_IN']],
#C6,   1,   XCH,      A, @R0
[['RAR-@RI'],['ACC_OUT','TMP_IN'],['RAM_OUT','ACC_IN'],['TMP_OUT','RAM_IN']],
#C7,   1,   XCH,      A, @R1
-1,
#C8,   1,   XCH,      A, R0
[['ACC_OUT','TMP_IN'],['RAR-RI_OUT','ACC_IN'],['TMP_OUT','RAR-RI_IN']],
#C9,   1,   XCH,      A, R1
-1,
#CA,   1,   XCH,      A, R2
-1,
#CB,   1,   XCH,      A, R3
-1,
#CC,   1,   XCH,      A, R4
-1,
#CD,   1,   XCH,      A, R5
-1,
#CE,   1,   XCH,      A, R6
-1,
#CF,   1,   XCH,      A, R7
-1,
#D0,   2,   POP,      direct
[['SP_OUT','RAR_IN','ALU_A_DBUS_L8IN'],*merge_first(['RAM_OUT','TMP_IN'],STEP_DIRECT_ADDRESS),['TMP_OUT','RAM_IN'],['ALU_DEC','ADT_L8E','SP_IN']],
#D1,   2,   ACALL,    addr11
0x11,
#D2,   2,   SETB,     bit
[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['TMP_BITADDR_OUT','BOP_IN','RAR_IN','TMP_BOP_CLR'],['RAM_OUT','TMP_IN','TMP_BOP_CPL'],['BOP_OUT','RAM_IN']],
#D3,   1,   SETB,     C
[['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN','TMP_BOP_CLR'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS']],
#D4,   1,   DA,       A
[['ACC_OUT','TMP_IN'],['TMP_DA_OUT','TMP_BOP_LOAD_DA_CF','ACC_IN'],['PSW_OUT','TMP_IN','TMP_BOP_IDX_CY_IN'],['BOP_OUT','PSW_LOAD_BUS']],
#D5,   3,   DJNZ,     direct, offset
[*STEP_DIRECT_ADDRESS,['RAM_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAM_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#D6,   1,   XCHD,     A, @R0
[['RAR-@RI'],['RAM_OUT','ALU_A_DBUS_L8IN'],['ACC_OUT','ALU_A_H8IN','ADT_H8E','DTOALU'],['ALUEXT_XCHD','ADT_L8E','RAM_IN'],['ALUEXT_XCHD','ADT_H8E','ACC_IN']],
#D7,   1,   XCHD,     A, @R1
-1,
#D8,   2,   DJNZ,     R0, offset
[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE'],*PC_add_off_when('PC_/ZFIN')],
#D9,   2,   DJNZ,     R1, offset
-1,
#DA,   2,   DJNZ,     R2, offset
-1,
#DB,   2,   DJNZ,     R3, offset
-1,
#DC,   2,   DJNZ,     R4, offset
-1,
#DD,   2,   DJNZ,     R5, offset
-1,
#DE,   2,   DJNZ,     R6, offset
-1,
#DF,   2,   DJNZ,     R7, offset
-1,
#E0,   1,   MOVX,     A, @DPTR
[],
#E1,   2,   AJMP,     addr11
1,
#E2,   1,   MOVX,     A, @R0
[],
#E3,   1,   MOVX,     A, @R1
[],
#E4,   1,   CLR,      A
[['ACC_IN']],
#E5,   2,   MOV,      A, direct
[*STEP_DIRECT_ADDRESS,['RAM_OUT','TMP_IN'],['TMP_OUT','ACC_IN']],
#E6,   1,   MOV,      A, @R0
[['RAR-@RI'],['RAM_OUT','TMP_IN'],['TMP_OUT','ACC_IN']],
#E7,   1,   MOV,      A, @R1
-1,
#E8,   1,   MOV,      A, R0
[['RAR-RI_OUT','ACC_IN']],
#E9,   1,   MOV,      A, R1
-1,
#EA,   1,   MOV,      A, R2
-1,
#EB,   1,   MOV,      A, R3
-1,
#EC,   1,   MOV,      A, R4
-1,
#ED,   1,   MOV,      A, R5
-1,
#EE,   1,   MOV,      A, R6
-1,
#EF,   1,   MOV,      A, R7
-1,
#F0,   1,   MOVX,     @DPTR, A
[],
#F1,   2,   ACALL,    addr11
0x11,
#F2,   1,   MOVX,     @R0, A
[],
#F3,   1,   MOVX,     @R1, A
[],
#F4,   1,   CPL,      A
[['ACC_OUT','ALU_A_DBUS_L8IN'],['ALU_NOT','ADT_L8E','ACC_IN']],
#F5,   2,   MOV,      direct, A
[*merge_first(['ACC_OUT','TMP_IN'],STEP_DIRECT_ADDRESS),['TMP_OUT','RAM_IN']],
#F6,   1,   MOV,      @R0, A
[['ACC_OUT','TMP_IN'],['RAR-@RI'],['TMP_OUT','RAM_IN']],
#F7,   1,   MOV,      @R1, A
-1,
#F8,   1,   MOV,      R0, A
[['ACC_OUT','TMP_IN'],['TMP_OUT','RAR-RI_IN']],
#F9,   1,   MOV,      R1, A
-1,
#FA,   1,   MOV,      R2, A
-1,
#FB,   1,   MOV,      R3, A
-1,
#FC,   1,   MOV,      R4, A
-1,
#FD,   1,   MOV,      R5, A
-1,
#FE,   1,   MOV,      R6, A
-1,
#FF,   1,   MOV,      R7, A
-1
]