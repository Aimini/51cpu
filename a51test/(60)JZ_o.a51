START:
MOV A,#0xFF
JZ FINAL
MOV A,#0x00
JZ TO_2
FINAL:
	MOV A,#0x00
	JZ START
	
TO_2:
	MOV A,#0x00
	JZ FINAL