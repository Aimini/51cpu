HEX_TO_NAME = {0x00:'NOP',0x01:'AJMP',0x02:'LJMP',0x03:'RR',0x04:'INC',0x05:'INC',0x06:'INC',0x07:'INC',0x08:'INC',0x09:'INC',0x0A:'INC',0x0B:'INC',0x0C:'INC',0x0D:'INC',0x0E:'INC',0x0F:'INC',0x10:'JBC',0x11:'ACALL',0x12:'LCALL',0x13:'RRC',0x14:'DEC',0x15:'DEC',0x16:'DEC',0x17:'DEC',0x18:'DEC',0x19:'DEC',0x1A:'DEC',0x1B:'DEC',0x1C:'DEC',0x1D:'DEC',0x1E:'DEC',0x1F:'DEC',0x20:'JB',0x21:'AJMP',0x22:'RET',0x23:'RL',0x24:'ADD',0x25:'ADD',0x26:'ADD',0x27:'ADD',0x28:'ADD',0x29:'ADD',0x2A:'ADD',0x2B:'ADD',0x2C:'ADD',0x2D:'ADD',0x2E:'ADD',0x2F:'ADD',0x30:'JNB',0x31:'ACALL',0x32:'RETI',0x33:'RLC',0x34:'ADDC',0x35:'ADDC',0x36:'ADDC',0x37:'ADDC',0x38:'ADDC',0x39:'ADDC',0x3A:'ADDC',0x3B:'ADDC',0x3C:'ADDC',0x3D:'ADDC',0x3E:'ADDC',0x3F:'ADDC',0x40:'JC',0x41:'AJMP',0x42:'ORL',0x43:'ORL',0x44:'ORL',0x45:'ORL',0x46:'ORL',0x47:'ORL',0x48:'ORL',0x49:'ORL',0x4A:'ORL',0x4B:'ORL',0x4C:'ORL',0x4D:'ORL',0x4E:'ORL',0x4F:'ORL',0x50:'JNC',0x51:'ACALL',0x52:'ANL',0x53:'ANL',0x54:'ANL',0x55:'ANL',0x56:'ANL',0x57:'ANL',0x58:'ANL',0x59:'ANL',0x5A:'ANL',0x5B:'ANL',0x5C:'ANL',0x5D:'ANL',0x5E:'ANL',0x5F:'ANL',0x60:'JZ',0x61:'AJMP',0x62:'XRL',0x63:'XRL',0x64:'XRL',0x65:'XRL',0x66:'XRL',0x67:'XRL',0x68:'XRL',0x69:'XRL',0x6A:'XRL',0x6B:'XRL',0x6C:'XRL',0x6D:'XRL',0x6E:'XRL',0x6F:'XRL',0x70:'JNZ',0x71:'ACALL',0x72:'ORL',0x73:'JMP',0x74:'MOV',0x75:'MOV',0x76:'MOV',0x77:'MOV',0x78:'MOV',0x79:'MOV',0x7A:'MOV',0x7B:'MOV',0x7C:'MOV',0x7D:'MOV',0x7E:'MOV',0x7F:'MOV',0x80:'SJMP',0x81:'AJMP',0x82:'ANL',0x83:'MOVC',0x84:'DIV',0x85:'MOV',0x86:'MOV',0x87:'MOV',0x88:'MOV',0x89:'MOV',0x8A:'MOV',0x8B:'MOV',0x8C:'MOV',0x8D:'MOV',0x8E:'MOV',0x8F:'MOV',0x90:'MOV',0x91:'ACALL',0x92:'MOV',0x93:'MOVC',0x94:'SUBB',0x95:'SUBB',0x96:'SUBB',0x97:'SUBB',0x98:'SUBB',0x99:'SUBB',0x9A:'SUBB',0x9B:'SUBB',0x9C:'SUBB',0x9D:'SUBB',0x9E:'SUBB',0x9F:'SUBB',0xA0:'ORL',0xA1:'AJMP',0xA2:'MOV',0xA3:'INC',0xA4:'MUL',0xA5:'reserved',0xA6:'MOV',0xA7:'MOV',0xA8:'MOV',0xA9:'MOV',0xAA:'MOV',0xAB:'MOV',0xAC:'MOV',0xAD:'MOV',0xAE:'MOV',0xAF:'MOV',0xB0:'ANL',0xB1:'ACALL',0xB2:'CPL',0xB3:'CPL',0xB4:'CJNE',0xB5:'CJNE',0xB6:'CJNE',0xB7:'CJNE',0xB8:'CJNE',0xB9:'CJNE',0xBA:'CJNE',0xBB:'CJNE',0xBC:'CJNE',0xBD:'CJNE',0xBE:'CJNE',0xBF:'CJNE',0xC0:'PUSH',0xC1:'AJMP',0xC2:'CLR',0xC3:'CLR',0xC4:'SWAP',0xC5:'XCH',0xC6:'XCH',0xC7:'XCH',0xC8:'XCH',0xC9:'XCH',0xCA:'XCH',0xCB:'XCH',0xCC:'XCH',0xCD:'XCH',0xCE:'XCH',0xCF:'XCH',0xD0:'POP',0xD1:'ACALL',0xD2:'SETB',0xD3:'SETB',0xD4:'DA',0xD5:'DJNZ',0xD6:'XCHD',0xD7:'XCHD',0xD8:'DJNZ',0xD9:'DJNZ',0xDA:'DJNZ',0xDB:'DJNZ',0xDC:'DJNZ',0xDD:'DJNZ',0xDE:'DJNZ',0xDF:'DJNZ',0xE0:'MOVX',0xE1:'AJMP',0xE2:'MOVX',0xE3:'MOVX',0xE4:'CLR',0xE5:'MOV',0xE6:'MOV',0xE7:'MOV',0xE8:'MOV',0xE9:'MOV',0xEA:'MOV',0xEB:'MOV',0xEC:'MOV',0xED:'MOV',0xEE:'MOV',0xEF:'MOV',0xF0:'MOVX',0xF1:'ACALL',0xF2:'MOVX',0xF3:'MOVX',0xF4:'CPL',0xF5:'MOV',0xF6:'MOV',0xF7:'MOV',0xF8:'MOV',0xF9:'MOV',0xFA:'MOV',0xFB:'MOV',0xFC:'MOV',0xFD:'MOV',0xFE:'MOV',0xFF:'MOV',}

NAME_TO_HEX = dict()
for hexadecimal, mnemonic in HEX_TO_NAME.items():
    # Create a  mnemonic to  hex  mapping
    try:
        values = NAME_TO_HEX[mnemonic]
        # if current mnemonic already has hex , add it to mnemonic list
        NAME_TO_HEX.update({mnemonic: values + (hex,)})
    except KeyError as e:
        NAME_TO_HEX.update({mnemonic: (hex,)})


def print_info():
    print("Hex to Mnemonic:")
    for k, v in HEX_TO_NAME.items():
        print("{:0>2X}  {}".format(k, v))

    print("Mnemonic to Hex:")
    for k, v in NAME_TO_HEX.items():
        print("{:<8}".format(k), end='  ')
        for hex in v:
            print("0x{:0<2X}".format(hex), end=', ')
        print()