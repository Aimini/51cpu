;LJMP addr16
LJMP 0x10

cseg at 0x10
	mov a,#1
	LJMP 0xFF00
	
cseg at 0xF0
	mov a,#0xFF
	LJMP 0x10
	
cseg at 0xff00
	mov a,#0xF
	LJMP 0xFFFB

cseg at 0xFFFB
	mov a,#0xF0
	LJMP 0xF0
	