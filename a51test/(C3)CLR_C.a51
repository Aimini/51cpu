MOV 0xD0, #0xFF
CLR	C
MOV A,#0x01
START:
	MOV 0xD0,A
	CLR	C
	RL A
SJMP START
