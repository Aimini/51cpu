MOV 0x70,#0x40 ;direct start address
MOV 0x71,#0x20 ;direct start value
MOV	0x72,#0x00 ;R0~R7 start addrss
MOV	0x73,#0x20 ;target address for @Ri
MOV	0xF0,#0x20 ; count

MOV 0x7F,0x73
INIT:
	MOV A, 0x71
    MOV	0x00,0x70
	MOV @R0,A
	MOV	A, 0x73
	MOV	0x00,0x72
	MOV @R0,A
	INC 0x70
	INC 0x71
	INC 0x72
	INC 0x73
DJNZ 0xF0,INIT
MOV 0x00,0x7F


MOV 0xD0,#0x00
MOV @R0,#0x30
MOV @R1,#0x31

MOV 0xD0,#0x08
MOV @R0,#0x38
MOV @R1,#0x39

MOV 0xD0,#0x10
MOV @R0,#0x40
MOV @R1,#0x41

MOV 0xD0,#0x18
MOV @R0,#0x48
MOV @R1,#0x49