START:
MOV A,#0x00
JNZ FINAL
MOV A,#0x0F
JNZ TO_2
FINAL:
	MOV A,#0xAA
	JNZ START
	
TO_2:
	MOV A,#0xFF
	JNZ FINAL