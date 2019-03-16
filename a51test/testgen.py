

sfr_addrs = {
    "P0" : 0x80,
    "TCON ": 0x88,
    "IE ": 0xA8,
    "IP ": 0xB8,
    "PSW ": 0xD0,
    "ACC ": 0xE0,
    "B ": 0xF0,
}



# MOV,      A, #immed
def X_74():
     for x in range(256):
        print("MOV A,#{}".format(x))

# MOV,      direct, #immed
def X_75():
     for x in range(256):
        print("MOV {0},#{0}".format(x))

#DJNZ,     direct, offset
def X_D5():
    print("$NOMOD51")
    for name,addr in sfr_addrs.items():
        print("{} EQU 0x{:0>2X}".format(name,addr))

    print()
    for x in sfr_addrs.keys():
        print("MOV {},0xFF".format(x))
        print("LOOP_{}:".format(x))
        print("DJNZ {},LOOP_{}".format(x,x))
        print()

def X_05():
    print("START:")
    for x in range(256):
	    print("INC {}".format(x))
    print("LJMP START")

# INC Ri
def X_08():
    for rs in range(4):
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        print("MOV 0xF0,#0xFF")
        print("START{}:".format(rs))
        for x in range(8):
            print("INC R{}".format(x))
        print("DJNZ 0xF0,START{}".format(rs))
        print()

def X_10():
    for x in range(16):
    	print("MOV 0x{:0>2X},#0x{:0>2X}".format(0x20 + x, (1 << (x%8))))
    print()
    print('SJMP L15')
    print()
    print('START:')
    for x in range(16):
        print("L{}: MOV A,#{}".format(x,x))
        print("JBC 0x{:0>2X},{}".format((x << 3) + (x%8), "L" + str(x - 1)  if x> 0 else "START"))
        
    print('MOV  A,#0xFF')

# ACALL addr11
def X_11():
    print('MOV 0X81,#0X07')#init SP
    for x in range(8):
        b = x+1
        print("MOV A,#{}".format(b))
        print("ACALL 0x{0:2>X}".format((x << 8) + b*2 + 0xa))
        print()
        print("CSEG AT 0x{0:2>X}".format((x << 8) + b*2 + 0xa))
    print('''MOV A,#0X0F
ACALL 0X7FF

CSEG AT 0X7FF
MOV A,#0XF0
ACALL 0X8FF

CSEG AT 0X8FF
MOV A,#0XFF
''')    


def X_15():
    print("START:")
    for x in range(256):
	    print("DEC {}".format(x))
    print("LJMP START")


# DEC Ri
def X_18():
    for rs in range(4):
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        print("MOV 0xF0,#0xFF")
        print("START{}:".format(rs))
        for x in range(8):
            print("DEC R{}".format(x))
        print("DJNZ 0xF0,START{}".format(rs))
        print()

# ADD A, Ri
def X_28():
    for x in range(32):
        print("mov {0},#{0}".format(x))
        
    for rs in range(4):
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(8):
            print("add A,R{}".format(x))
        print()

# MOV @Ri,A
def X_F6():
    for x in range(32):
        print("mov {},#0x{:0>2X}".format(x,0x20+x))

    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(2):
            print("INC A")
            print("MOV  @R{}, A".format(x))

# use
#   MOV direct,#immed
#   MOV direct,A
#   MOV direct,#immed
#   MOV @Ri,A
#   INC A
#   DJNZ direct,offset
def init_Ri():
    print("""
MOV 0xF0,#0x20
INIT:
	MOV 0x00,A ; use R0 to r/w indirect address 
	MOV @R0,A
	INC A
DJNZ 0xF0,INIT
MOV 0x00,#0x00
    """)
# MOV Rn,A
def X_F8():
    for rs in range(4):
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(8):
            print("INC A")
            print("MOV  R{}, A".format(x))


def init_all():
    print("""MOV 0xF0,#0x00
INIT:
	MOV R0,A
	MOV @R0,A
	INC A
DJNZ 0xF0,INIT
""")

def X_E5():
    init_all()
    for x in range(256):
        print("MOV  A, 0x{:0>2X}".format(x))


# MOV A, @Ri
def X_E6():
    init_Ri()
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(2):
            print("MOV  A,@R{}".format(x))
            print("NOP")
            print("NOP")

# MOV A, @Ri
def X_E8():
    init_Ri()
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(8):
            print("MOV  A,R{}".format(x))


# DJNZ Ri,offset
def X_D8():
    init_Ri()
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(8):
            label = "START_{}_{}".format(rs,x)
            print("{}:\n DJNZ R{},{}".format(label,x,label))

#MOV    @R0, direct
def X_A6():
    print("""
MOV 0x70,#0x40 ;direct start address
MOV 0x71,#0x20 ;direct start value
MOV	0x72,#0x00 ;R0~R7 start addrss
MOV	0x73,#0x20 ;target address for @Ri
MOV	0xF0,#0x20 ; count

MOV 0x7F,0x73
INIT:
	MOV A, 0x71
    MOV	0x00,0x70
	MOV @R0,A
	MOV	A, 0x73
	MOV	0x00,0x72
	MOV @R0,A
	INC 0x70
	INC 0x71
	INC 0x72
	INC 0x73
DJNZ 0xF0,INIT
MOV 0x00,0x7F
""")
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(2):
            print("MOV @R{},#0x{:0>2X}".format(x,0x30 + x + rs*8))

#MOV    @R0, #immed
def X_76():
    init_Ri()
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(2):
            print("MOV @R{},#0x{:0>2X}".format(x,0x25 + x))


#MOV    R0, #immed
def X_78():
    init_Ri()
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3))
        for x in range(8):
            print("MOV R{},#0x{:0>2X}".format(x,0x80 - rs*0x10 - x))


#MOV    INC,@Ri
def X_06():
    for rs in range(4):
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(2):
            print("MOV R{},#0x{:0>2X}".format(x,0x20 +rs*0x10 + x))  
        print()
    
    for rs in range(4):
        label = "RS_{}".format(rs)
        print("MOV 0x7F,#0xFF")
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        print(label+":")
        for x in range(2):
            print("INC @R{}".format(x))
        print("DJNZ 0x7F,{}".format(label))
        print()


# MOV Rn,direct
def X_A8():
    ADDR = 0X40
    for x in range(0x20):
        print("MOV 0x{:0>2X},#0x{:0>2X}".format(x+ADDR,x+0x10))
    print()

    for rs in range(4):
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(8):
            print("MOV R{},0x{:0>2X}".format(x,ADDR))
            ADDR += 1
        print()
    
# MOV direct,@Ri
def X_86():
    print("""
MOV	0x70,#0x00 ;R0~R7 start addrss
MOV	0x71,#0x20 ;indirect address for @Ri
MOV 0x72,#0x40 ;indirect start value
MOV	0xF0,#0x20 ; count

MOV 0x7F,0x71
INIT:
    MOV	R0,0x70
	MOV @R0,0x71
    MOV R0,0x71
    MOV @R0,0x72
	INC 0x70
	INC 0x71
	INC 0x72
DJNZ 0xF0,INIT
MOV R0,0x7F
""")
    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(2):
            print("MOV 0x{:0>2X},@R{}".format(0x60 + x + rs*8,x))


# MOV direct,Rn
def X_88():
    start = 0x20
    for  x in range(0x20):
        print("MOV 0x{:0>2X},#0x{:0>2X}".format(x, start + x))

    for rs in range(4):
        print()
        print("MOV 0xD0,#0x{:0>2X}".format(rs << 3 ))
        for x in range(8):
            print("MOV 0x{:0>2X},R{}".format(0x40 + rs*8 + x,x))


