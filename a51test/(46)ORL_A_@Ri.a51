MOV 0x6E,#0x01
MOV 0x43,#0x02
MOV 0x3B,#0x04
MOV 0x67,#0x08
MOV 0x21,#0x10
MOV 0x6C,#0x20
MOV 0x3F,#0x40
MOV 0x4C,#0x80

MOV 0xD0,#0x00
MOV R0,#0x6E
MOV R1,#0x43

MOV 0xD0,#0x08
MOV R0,#0x3B
MOV R1,#0x67

MOV 0xD0,#0x10
MOV R0,#0x21
MOV R1,#0x6C

MOV 0xD0,#0x18
MOV R0,#0x3F
MOV R1,#0x4C

MOV 0xD0,#0x00
ORL A,@R0
ORL A,@R1

MOV 0xD0,#0x08
ORL A,@R0
ORL A,@R1

MOV 0xD0,#0x10
ORL A,@R0
ORL A,@R1

MOV 0xD0,#0x18
ORL A,@R0
ORL A,@R1