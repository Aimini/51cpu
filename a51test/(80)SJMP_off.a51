; SJMP    offset(0x80) test
STEP0:
	MOV A,#0
	SJMP STEP1
STEP2:
	MOV A,#2
	SJMP STEP0
STEP1:
	MOV A,#1
	SJMP STEP2
