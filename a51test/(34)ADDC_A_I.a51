ADDC A,#0xFF ; CY = 0,AC = 0,OV = 0 ;A = 0xFF
ADDC A,#0x01 ;CY = 1,AC = 1, OV = 0 ;A = 0
ADDC A,#0x00 ;CY = 0,AC = 0, OV = 0 ;A = 1
ADDC A,#0xFF ;CY = 1,AC = 1, OV = 0; A = 0
ADDC A,#0x0F ;CY = 0,AC = 1, OV = 0; A= 0x10