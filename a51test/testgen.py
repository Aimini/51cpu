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


