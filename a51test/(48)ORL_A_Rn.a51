MOV 0xD0,#0x00
MOV R0,#0x01
MOV R1,#0x02
MOV R2,#0x04
MOV R3,#0x08
MOV R4,#0x10
MOV R5,#0x20
MOV R6,#0x40
MOV R7,#0x80

MOV 0xD0,#0x08
MOV R0,#0x01
MOV R1,#0x02
MOV R2,#0x04
MOV R3,#0x08
MOV R4,#0x10
MOV R5,#0x20
MOV R6,#0x40
MOV R7,#0x80

MOV 0xD0,#0x10
MOV R0,#0x01
MOV R1,#0x02
MOV R2,#0x04
MOV R3,#0x08
MOV R4,#0x10
MOV R5,#0x20
MOV R6,#0x40
MOV R7,#0x80

MOV 0xD0,#0x18
MOV R0,#0x01
MOV R1,#0x02
MOV R2,#0x04
MOV R3,#0x08
MOV R4,#0x10
MOV R5,#0x20
MOV R6,#0x40
MOV R7,#0x80

MOV A,#0x00
MOV 0xD0,#0x00
ORL A,R0
ORL A,R1
ORL A,R2
ORL A,R3
ORL A,R4
ORL A,R5
ORL A,R6
ORL A,R7
MOV A,#0x00
MOV 0xD0,#0x08
ORL A,R0
ORL A,R1
ORL A,R2
ORL A,R3
ORL A,R4
ORL A,R5
ORL A,R6
ORL A,R7
MOV A,#0x00
MOV 0xD0,#0x10
ORL A,R0
ORL A,R1
ORL A,R2
ORL A,R3
ORL A,R4
ORL A,R5
ORL A,R6
ORL A,R7
MOV A,#0x00
MOV 0xD0,#0x18
ORL A,R0
ORL A,R1
ORL A,R2
ORL A,R3
ORL A,R4
ORL A,R5
ORL A,R6
ORL A,R7