MOV 0xD0,#0x00
MOV 0xF0,#0xFF
START0:
INC R0
INC R1
INC R2
INC R3
INC R4
INC R5
INC R6
INC R7
DJNZ 0xF0,START0

MOV 0xD0,#0x08
MOV 0xF0,#0xFF
START1:
INC R0
INC R1
INC R2
INC R3
INC R4
INC R5
INC R6
INC R7
DJNZ 0xF0,START1

MOV 0xD0,#0x10
MOV 0xF0,#0xFF
START2:
INC R0
INC R1
INC R2
INC R3
INC R4
INC R5
INC R6
INC R7
DJNZ 0xF0,START2

MOV 0xD0,#0x18
MOV 0xF0,#0xFF
START3:
INC R0
INC R1
INC R2
INC R3
INC R4
INC R5
INC R6
INC R7
DJNZ 0xF0,START3