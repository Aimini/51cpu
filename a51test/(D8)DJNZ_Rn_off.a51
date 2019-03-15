MOV 0xF0,#0x20
INIT:
	MOV 0x00,A ; use R0 to r/w indirect address 
	MOV @R0,A
	INC A
DJNZ 0xF0,INIT
MOV 0x00,#0x00
    

MOV 0xD0,#0x00
START_0_0:
 DJNZ R0,START_0_0
START_0_1:
 DJNZ R1,START_0_1
START_0_2:
 DJNZ R2,START_0_2
START_0_3:
 DJNZ R3,START_0_3
START_0_4:
 DJNZ R4,START_0_4
START_0_5:
 DJNZ R5,START_0_5
START_0_6:
 DJNZ R6,START_0_6
START_0_7:
 DJNZ R7,START_0_7

MOV 0xD0,#0x08
START_1_0:
 DJNZ R0,START_1_0
START_1_1:
 DJNZ R1,START_1_1
START_1_2:
 DJNZ R2,START_1_2
START_1_3:
 DJNZ R3,START_1_3
START_1_4:
 DJNZ R4,START_1_4
START_1_5:
 DJNZ R5,START_1_5
START_1_6:
 DJNZ R6,START_1_6
START_1_7:
 DJNZ R7,START_1_7

MOV 0xD0,#0x10
START_2_0:
 DJNZ R0,START_2_0
START_2_1:
 DJNZ R1,START_2_1
START_2_2:
 DJNZ R2,START_2_2
START_2_3:
 DJNZ R3,START_2_3
START_2_4:
 DJNZ R4,START_2_4
START_2_5:
 DJNZ R5,START_2_5
START_2_6:
 DJNZ R6,START_2_6
START_2_7:
 DJNZ R7,START_2_7

MOV 0xD0,#0x18
START_3_0:
 DJNZ R0,START_3_0
START_3_1:
 DJNZ R1,START_3_1
START_3_2:
 DJNZ R2,START_3_2
START_3_3:
 DJNZ R3,START_3_3
START_3_4:
 DJNZ R4,START_3_4
START_3_5:
 DJNZ R5,START_3_5
START_3_6:
 DJNZ R6,START_3_6
START_3_7:
 DJNZ R7,START_3_7
 
MOV A,#0XFF