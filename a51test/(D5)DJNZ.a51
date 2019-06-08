; test for      DJNZ,     direct, offset(D5)
$NOMOD51
P0 EQU 0x80
SP EQU 0x81
DPL EQU 0x82
DPH EQU 0x83
TCON EQU 0x88
IE EQU 0xA8
IP EQU 0xB8
PSW EQU 0xD0
ACC EQU 0xE0
B EQU 0xF0
MOV P0,#0
LOOP_P0:
DJNZ P0,LOOP_P0

MOV SP,#0
DJNZ SP,$

MOV DPL,#0
DJNZ DPL,$

MOV DPH,#0
DJNZ DPH,$

MOV TCON,#0
LOOP_TCON:
DJNZ TCON,LOOP_TCON

MOV IE,#0
LOOP_IE:
DJNZ IE,LOOP_IE

MOV IP,#0
LOOP_IP:
DJNZ IP,LOOP_IP

MOV ACC,#0
LOOP_ACC:
DJNZ ACC,LOOP_ACC

MOV B,#0
LOOP_B:
DJNZ B,LOOP_B

MOV PSW,#0
LOOP_PSW:
DJNZ PSW,LOOP_PSW