AJMP 0X04

CSEG AT 0X04
AJMP 0X7FF

CSEG AT 0x07FF
DB 1,0X0F
CSEG AT 0X080F
	MOV A,#0Xff