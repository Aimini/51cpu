FLAG = ['Carry','TMP_ZF','BIT']

STEP_DIRECT_ADDRESS = [['NEXT_BYTE'],['FLASH_OUT','RAR_IN']]
STEP_PC_ADD_OFFSET = [['FLASH_OUT','ALU_A_DBUS_L8IN'],["ALUEXT_TWO_CMP","ALU_B_IN"],["PC_OUT","ALUADDRTE","ALU_A_IN"],['ALU_ADD','ALUADDRTE','ALUTOADDR','PC_IN']]
FLAG_INSTRUCTION ={
    'Carry':{
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
    },
    'BIT':{
    }   
}