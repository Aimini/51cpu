FLAG = ['Carry','TMP_ZF','BIT']

STEP_DIRECT_ADDRESS = [['NEXT_BYTE'],['FLASH_OUT','RAR_IN']]
STEP_PC_ADD_OFFSET = [['FLASH_OUT','ALU_A_DBUS_L8IN'],["ALUEXT_TWO_CMP","ALU_B_IN"],["PC_OUT","ALUADDRTE","ALU_A_IN"],['ALU_ADD','ALUADDRTE','ALUTOADDR','PC_IN']]
FLAG_INSTRUCTION ={
    'Carry':{
	#2	ADDC	A, #immed
    0x34:[['PC_OUT','PAR_IN','ACC_OUT','ALU_A_IN'],['FLASH_OUT','ALU_B_IN'],['ALU_ADDD','ALU_OUT','ACC_IN']],
	#2	ADDC	A, direct
    0x35:[[]],
	#1	ADDC	A, @R0
    0x36:[[]],
	#1	ADDC	A, @R1
    0x37:[[]],
	#1	ADDC	A, R0
    0x38:[[]],
	#1	ADDC	A, R1
    0x39:[[]],
	#1	ADDC	A, R2
    0x3A:[[]],
	#1	ADDC	A, R3
    0x3B:[[]],
	#1	ADDC	A, R4
    0x3C:[[]],
	#1	ADDC	A, R5
    0x3D:[[]],
	#1	ADDC	A, R6
    0x3E:[[]],
	#1	ADDC	A, R7
    0x3F:[[]],
    #JC	offset
    0x40:[[]],
    #JNC	offset
    0x50:[[]],
	#2	SUBB	A, #immed
    0x94:[],
	#2	SUBB	A, direct
    0x95:[],
	#1	SUBB	A, @R0
    0x96:[],
	#1	SUBB	A, @R1
    0x97:[],
	#1	SUBB	A, R0
    0x98:[],
	#1	SUBB	A, R1
    0x99:[],
	#1	SUBB	A, R2
    0x9A:[],
	#1	SUBB	A, R3
    0x9B:[],
	#1	SUBB	A, R4
    0x9C:[],
	#1	SUBB	A, R5
    0x9D:[],
	#1	SUBB	A, R6
    0x9E:[],
	#1	SUBB	A, R7
    0x9F:[],
    },
    'TMP_ZF':{
    #2	JZ	offset
    0x60:[],
    #2	JNZ	offset
    0x70:[],
    #3	DJNZ	direct, offset
    0xD5:[*STEP_DIRECT_ADDRESS,['RAM_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAM_IN','NEXT_BYTE']],
    #2	DJNZ	R0, offset
    0xD8:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R1, offset
    0xD9:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R2, offset
    0xDA:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R3, offset
    0xDB:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R4, offset
    0xDC:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R5, offset
    0xDD:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R6, offset
    0xDE:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
    #2	DJNZ	R7, offset
    0xDF:[['RAR-RI_OUT','ALU_A_DBUS_L8IN'],['ALU_DEC','ADT_L8E','TMP_IN','RAR-RI_IN','NEXT_BYTE']],
	#3	CJNE	A, #immed, offset
    0XB4:[],
	#3	CJNE	A, direct, offset
    0XB5:[],
	#3	CJNE	@R0, #immed, offset
    0XB6:[],
	#3	CJNE	@R1, #immed, offset
    0XB7:[],
	#3	CJNE	R0, #immed, offset
    0XB8:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R1, #immed, offset
    0XB9:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R2, #immed, offset
    0XBA:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R3, #immed, offset
    0XBB:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R4, #immed, offset
    0XBC:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R5, #immed, offset
    0XBD:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R6, #immed, offset
    0XBE:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
	#3	CJNE	R7, #immed, offset
    0XBF:[['RAR-RI_OUT','ALU_A_DBUS_L8IN','NEXT_BYTE'],['FLASH_OUT','ALU_B_DBUS_L8IN'],['ALU_SUB','ADT_H8E','TMP_IN'],['TMP_BOP_LOAD_TMP_ZF','PSW_OUT','TMP_BOP_IDX_CY_IN','TMP_IN'],['TMP_BOP_CPL'],['BOP_OUT','PSW_LOAD_BUS'],['ALU_SUB','ADT_L8E','TMP_IN','NEXT_BYTE'],[],[],[],[]],
    },
    'BIT':{
    #JBC	bit, offset
    0x10:[['NEXT_BYTE'],['FLASH_OUT','TMP_IN'],['BOP_IN','TMP_BITADDR_OUT','RAR_IN'],['RAM_LATCH_OUT','TMP_IN'],['NEXT_BYTE'],*STEP_PC_ADD_OFFSET,['TMP_BOP_CLR'],['BOP_OUT','RAM_IN']],
    #JB	    bit, offset
    0x20:[],
    #JNB    bit, offset
    0x30:[],
    }   
}