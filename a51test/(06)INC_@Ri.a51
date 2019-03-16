MOV 0xD0,#0x00
MOV R0,#0x20
MOV R1,#0x21

MOV 0xD0,#0x08
MOV R0,#0x30
MOV R1,#0x31

MOV 0xD0,#0x10
MOV R0,#0x40
MOV R1,#0x41

MOV 0xD0,#0x18
MOV R0,#0x50

MOV R1,#0x51

MOV 0x7F,#0xFF
MOV 0xD0,#0x00
RS_0:
INC @R0
INC @R1
DJNZ 0x7F,RS_0

MOV 0x7F,#0xFF
MOV 0xD0,#0x08
RS_1:
INC @R0
INC @R1
DJNZ 0x7F,RS_1

MOV 0x7F,#0xFF
MOV 0xD0,#0x10
RS_2:
INC @R0
INC @R1
DJNZ 0x7F,RS_2

MOV 0x7F,#0xFF
MOV 0xD0,#0x18
RS_3:
INC @R0
INC @R1
DJNZ 0x7F,RS_3
