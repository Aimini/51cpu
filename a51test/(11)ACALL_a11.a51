// ACALL addr11 (0x11,0x31,0x51,0x71,0x91,0xb1,0xd1,0xf1)
MOV 0X81,#0x07
MOV A,#1
ACALL 0xC

CSEG AT 0xC
MOV A,#2
ACALL 0x10E

CSEG AT 0x10E
MOV A,#3
ACALL 0x210

CSEG AT 0x210
MOV A,#4
ACALL 0x312

CSEG AT 0x312
MOV A,#5
ACALL 0x414

CSEG AT 0x414
MOV A,#6
ACALL 0x516

CSEG AT 0x516
MOV A,#7
ACALL 0x618

CSEG AT 0x618
MOV A,#8
ACALL 0x71A

CSEG AT 0x71A
MOV A,#0X0F
ACALL 0X7FF

CSEG AT 0X7FF
MOV A,#0XF0
ACALL 0X8FF

CSEG AT 0X8FF
MOV A,#0XFF