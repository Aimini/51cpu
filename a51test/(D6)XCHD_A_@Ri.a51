MOV 0x6E,#0x00
MOV 0x43,#0x11
MOV 0x3B,#0x22
MOV 0x67,#0x33
MOV 0x21,#0x44
MOV 0x6C,#0x55
MOV 0x3F,#0x66
MOV 0x4C,#0x77

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
MOV A,#0xFF

MOV 0xD0,#0x00
XCHD A,@R0
XCHD A,@R1

MOV 0xD0,#0x08
XCHD A,@R0
XCHD A,@R1

MOV 0xD0,#0x10
XCHD A,@R0
XCHD A,@R1

MOV 0xD0,#0x18
XCHD A,@R0
XCHD A,@R1