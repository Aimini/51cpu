M_CLR = 0
M_SET = 1
M_CPL = 2
M_CARRY = 3

def bitoperation_conuter(doit):
    for carry in range(2**1):
        for mode in range(2**2):
            for bs in range(2**3):
                for data in range(2**8):
                    doit(carry,mode,bs,data)


def bitop_gen(carry,mode,bitselect,data):
    lower_mask = 2**bitselect - 1
    high_mask =  ((~lower_mask) << 1)&0xff
    low = lower_mask & data
    high = high_mask & data
    bitq = (data >> bitselect) & 1
    
    if mode == M_CLR:
        q = 0
    elif mode== M_SET:
        q = 1
    elif mode == M_CPL:
        q = (~bitq) & 1
    elif mode == M_CARRY:
        q = carry & 1
    result =high + (q << bitselect) + low
    print('{} {} {} {:0>8b} {:0>8b}'.format(carry,mode,bitselect,data,result))

bitoperation_conuter(bitop_gen)