MOV 0x00,#0x00
MOV 0x01,#0x01
MOV 0x02,#0x02
MOV 0x03,#0x03
MOV 0x04,#0x04
MOV 0x05,#0x05
MOV 0x06,#0x06
MOV 0x07,#0x07
MOV 0x08,#0x08
MOV 0x09,#0x09
MOV 0x0A,#0x0A
MOV 0x0B,#0x0B
MOV 0x0C,#0x0C
MOV 0x0D,#0x0D
MOV 0x0E,#0x0E
MOV 0x0F,#0x0F
MOV 0x10,#0x10
MOV 0x11,#0x11
MOV 0x12,#0x12
MOV 0x13,#0x13
MOV 0x14,#0x14
MOV 0x15,#0x15
MOV 0x16,#0x16
MOV 0x17,#0x17
MOV 0x18,#0x18
MOV 0x19,#0x19
MOV 0x1A,#0x1A
MOV 0x1B,#0x1B
MOV 0x1C,#0x1C
MOV 0x1D,#0x1D
MOV 0x1E,#0x1E
MOV 0x1F,#0x1F

MOV A,#0
LJMP STATE_31
STATE_0: 
    CJNE A,0x00,FINAL
    LJMP TEST_2
    


STATE_1: CJNE A,0x01,STATE_0
STATE_2: CJNE A,0x02,STATE_1
STATE_3: CJNE A,0x03,STATE_2
STATE_4: CJNE A,0x04,STATE_3
STATE_5: CJNE A,0x05,STATE_4
STATE_6: CJNE A,0x06,STATE_5
STATE_7: CJNE A,0x07,STATE_6
STATE_8: CJNE A,0x08,STATE_7
STATE_9: CJNE A,0x09,STATE_8
STATE_10: CJNE A,0x0A,STATE_9
STATE_11: CJNE A,0x0B,STATE_10
STATE_12: CJNE A,0x0C,STATE_11
STATE_13: CJNE A,0x0D,STATE_12
STATE_14: CJNE A,0x0E,STATE_13
STATE_15: CJNE A,0x0F,STATE_14
STATE_16: CJNE A,0x10,STATE_15
STATE_17: CJNE A,0x11,STATE_16
STATE_18: CJNE A,0x12,STATE_17
STATE_19: CJNE A,0x13,STATE_18
STATE_20: CJNE A,0x14,STATE_19
STATE_21: CJNE A,0x15,STATE_20
STATE_22: CJNE A,0x16,STATE_21
STATE_23: CJNE A,0x17,STATE_22
STATE_24: CJNE A,0x18,STATE_23
STATE_25: CJNE A,0x19,STATE_24
STATE_26: CJNE A,0x1A,STATE_25
STATE_27: CJNE A,0x1B,STATE_26
STATE_28: CJNE A,0x1C,STATE_27
STATE_29: CJNE A,0x1D,STATE_28
STATE_30: CJNE A,0x1E,STATE_29
STATE_31: CJNE A,0x1F,STATE_30

TEST_2:
    MOV A,#0x10
    MOV 0xF0, #0x10
    MOV 0x80, #0xF0
    MOV 0xD0, #0x0F
    SJMP CH_3
    CH_1: CJNE A,0xF0,FINAL
    SJMP DNOTHING
    CH_2: CJNE A,0xD0,CH_1
    CH_3: CJNE A,0x80,CH_2
FINAL: 
    MOV A,0xFF
DNOTHING:
    NOP
    