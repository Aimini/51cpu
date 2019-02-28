
def ControlHex():
    n = 1
    while True:
        yield n
        n = n << 1
        

MICRO_INSTRCUTON_COUNTER_CLR = ControlHex()
INTERRUPT_CHECK = ControlHex()
ALU_O = ControlHex()
ALU_M = ControlHex()
ALU_S0 = ControlHex()
ALU_S1 = ControlHex()
ALU_S2 = ControlHex()
ALU_S3 = ControlHex()
ALU_CN = ControlHex()
ALU_FUNCTION_ADD  = ALU_CN | ALU_S3 | ALU_S0
ALU_FUCTION_ADDD  = ALU_S3 | ALU_S0
ALU_FUNCTION_SUB  = ALU_CN | ALU_S2 | ALU_S1  
ALU_FUNCTION_SUBB = ALU_S2 | ALU_S1  
ALU_FUNCTION_AND  = ALU_M | ALU_S3 | ALU_S1 | ALU_S0
ALU_FUNCTION_OR   = ALU_M | ALU_S3 | ALU_S2 | ALU_S1
ALU_FUNCTION_NOT  = ALU_M
ALU_FUNCTION_XOR  = ALU_M | ALU_S2 | ALU_S1
ACC_OUT = ControlHex()
ACC_IN = ControlHex()
B_OUT = ControlHex()
B_IN = ControlHex()




    

