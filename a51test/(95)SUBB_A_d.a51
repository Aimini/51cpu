MOV 0x43,#0x58
MOV 0x7D,#0x6D
MOV 0x5B,#0x24
MOV 0x3F,#0x63
MOV 0x22,#0x47
MOV 0x46,#0x42
MOV 0x6A,#0x79
MOV 0x4E,#0x30
MOV 0x15,#0xFE
DB 0xA5
SUBB A,0x43 ;A8 C=1 AC=1
SUBB A,0x7D ;3A OV=1 AC=1
SUBB A,0x5B ;16
SUBB A,0x3F ;B3 C=1
SUBB A,0x22 ;6B	AC=1 OV=1
SUBB A,0x46 ;29 
SUBB A,0x6A ;B0 C=1
SUBB A,0x4E ;7F AC=1 OV=1
SUBB A,0x;0x81 C = 1 AC = 0 OV = 1
