
MOV 0xD0,#0x00
MOV R0,#0x00
MOV A,#0x02
MOVX @R0,A
MOV R1,#0x03
MOV A,#0x03
MOVX @R1,A

MOV 0xD0,#0x08
MOV R0,#0x08
MOV A,#0x04
MOVX @R0,A
MOV R1,#0x0F
MOV A,#0x05
MOVX @R1,A

MOV 0xD0,#0x10
MOV R0,#0x18
MOV A,#0x06
MOVX @R0,A
MOV R1,#0x23
MOV A,#0x07
MOVX @R1,A

MOV 0xD0,#0x18
MOV R0,#0x30
MOV A,#0x08
MOVX @R0,A
MOV R1,#0x3F
MOV A,#0x09
MOVX @R1,A

MOV 0xD0,#0x00
MOVX A,@R0
MOVX A,@R1

MOV 0xD0,#0x08
MOVX A,@R0
MOVX A,@R1

MOV 0xD0,#0x10
MOVX A,@R0
MOVX A,@R1

MOV 0xD0,#0x18
MOVX A,@R0
MOVX A,@R1
