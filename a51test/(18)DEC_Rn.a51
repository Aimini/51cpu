MOV 0xD0,#0x00
MOV 0xF0,#0xFF
START0:
DEC R0
DEC R1
DEC R2
DEC R3
DEC R4
DEC R5
DEC R6
DEC R7
DJNZ 0xF0,START0

MOV 0xD0,#0x08
MOV 0xF0,#0xFF
START1:
DEC R0
DEC R1
DEC R2
DEC R3
DEC R4
DEC R5
DEC R6
DEC R7
DJNZ 0xF0,START1

MOV 0xD0,#0x10
MOV 0xF0,#0xFF
START2:
DEC R0
DEC R1
DEC R2
DEC R3
DEC R4
DEC R5
DEC R6
DEC R7
DJNZ 0xF0,START2

MOV 0xD0,#0x18
MOV 0xF0,#0xFF
START3:
DEC R0
DEC R1
DEC R2
DEC R3
DEC R4
DEC R5
DEC R6
DEC R7
DJNZ 0xF0,START3