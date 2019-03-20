MOV 0xF0,#0x20
INIT:
	MOV 0x00,A ; use R0 to r/w indirect address 
	MOV @R0,A
	INC A
DJNZ 0xF0,INIT
MOV 0x00,#0x00
    
MOV A,#0xFF

MOV 0xD0,#0x00
XCH A,R0
XCH A,R1
XCH A,R2
XCH A,R3
XCH A,R4
XCH A,R5
XCH A,R6
XCH A,R7

MOV 0xD0,#0x08
XCH A,R0
XCH A,R1
XCH A,R2
XCH A,R3
XCH A,R4
XCH A,R5
XCH A,R6
XCH A,R7

MOV 0xD0,#0x10
XCH A,R0
XCH A,R1
XCH A,R2
XCH A,R3
XCH A,R4
XCH A,R5
XCH A,R6
XCH A,R7

MOV 0xD0,#0x18
XCH A,R0
XCH A,R1
XCH A,R2
XCH A,R3
XCH A,R4
XCH A,R5
XCH A,R6
XCH A,R7