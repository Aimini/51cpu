MOV 0X81,#0x07
MOV A,#1
LCALL 0xC

CSEG AT 0xC
MOV A,#2
LCALL 0x10E

CSEG AT 0x10E
MOV A,#3
LCALL 0x210

CSEG AT 0x210
MOV A,#4
LCALL 0x312

CSEG AT 0x312
MOV A,#5
LCALL 0x414

CSEG AT 0x414
MOV A,#6
LCALL 0x516

CSEG AT 0x516
MOV A,#7
LCALL 0x618

CSEG AT 0x618
MOV A,#8
LCALL 0x71A

CSEG AT 0x71A
MOV A,#0X0F
LCALL 0X7FF

CSEG AT 0X7FF
MOV A,#0XF0
LCALL 0X8FF

CSEG AT 0X8FF
MOV A,#0XFF