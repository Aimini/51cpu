MOV A,#0xFF
MOV 0x2A,#0xFE
MOV 0x33,#0xFD
MOV 0x44,#0xFB
MOV 0x6E,#0xF7
MOV 0x40,#0xEF
MOV 0x6A,#0xDF
MOV 0x63,#0xBF
MOV 0x3D,#0x7F

MOV 0xD0,#0x00
MOV R0,#0x2A
MOV R1,#0x33

MOV 0xD0,#0x08
MOV R0,#0x44
MOV R1,#0x6E

MOV 0xD0,#0x10
MOV R0,#0x40
MOV R1,#0x6A

MOV 0xD0,#0x18
MOV R0,#0x63
MOV R1,#0x3D

MOV 0xD0,#0x00
ANL A,@R0
ANL A,@R1

MOV 0xD0,#0x08
ANL A,@R0
ANL A,@R1

MOV 0xD0,#0x10
ANL A,@R0
ANL A,@R1

MOV 0xD0,#0x18
ANL A,@R0
ANL A,@R1