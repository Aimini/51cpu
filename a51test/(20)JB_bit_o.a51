MOV 0x20,#0x01
MOV 0x21,#0x02
MOV 0x22,#0x04
MOV 0x23,#0x08
MOV 0x24,#0x10
MOV 0x25,#0x20
MOV 0x26,#0x40
MOV 0x27,#0x80
MOV 0x28,#0x01
MOV 0x29,#0x02
MOV 0x2A,#0x04
MOV 0x2B,#0x08
MOV 0x2C,#0x10
MOV 0x2D,#0x20
MOV 0x2E,#0x40
MOV 0x2F,#0x80
LJMP L15
L0:
    MOV A,#00
    LJMP FINAL

    
L1:
MOV A,#0x01
JB 0x21.1,L0
    
L2:
MOV A,#0x02
JB 0x22.2,L1
    
L3:
MOV A,#0x03
JB 0x23.3,L2
    
L4:
MOV A,#0x04
JB 0x24.4,L3
    
L5:
MOV A,#0x05
JB 0x25.5,L4
    
L6:
MOV A,#0x06
JB 0x26.6,L5
    
L7:
MOV A,#0x07
JB 0x27.7,L6
    
L8:
MOV A,#0x08
JB 0x28.0,L7
    
L9:
MOV A,#0x09
JB 0x29.1,L8
    
L10:
MOV A,#0x0A
JB 0x2A.2,L9
    
L11:
MOV A,#0x0B
JB 0x2B.3,L10
    
L12:
MOV A,#0x0C
JB 0x2C.4,L11
    
L13:
MOV A,#0x0D
JB 0x2D.5,L12
    
L14:
MOV A,#0x0E
JB 0x2E.6,L13
    
L15:
MOV A,#0x0F
JB 0x2F.7,L14
    FINAL:
    MOV 0xF0,#0xFF
    JB 0x2F.0,L0