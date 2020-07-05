
# 51cpu
## The design of the project from the beginning did not consider hardware implementation, so that it was too complicated to be implemented with simple hardware, so the project was no longer maintained.

Using 74ls chip to create a 51 cpu
(completing school final project now, I will write the document soon(After July))
## what you need(software)
1. Digital circuit foundation
2. Proteus (EDA simulate)
3. Python3 (generate LUT)
4. 51 instruction document

## recommeded
This project are inspired by Ben Eater,he is a amazing man. you can watch his [video](https://www.youtube.com/watch?v=HyznrdDSSGM&list=PLowKtXNTBypGqImE405J2565dvjafglHU "Building an 8-bit breadboard computer!") or visit his [website](https://eater.net/8bit "Build an 8-bit computer | Ben Eater")  to learning build a breadboard 8 bit cpu.

You can find the instruction document from keil [website](http://www.keil.com/dd/docs/datashts/intel/ism51.pdf), but I prefer this [electronic version](http://ww1.microchip.com/downloads/en/DeviceDoc/doc0509.pdf), it's more clear.

# compatibility
I use this book[website](http://www.keil.com/dd/docs/datashts/intel/ism51.pdf) as reference when I build this project, thus, all behavior   of these instructions are followed by it.
## include
1.  almost all instuction (view "exclude" to get unimplemented instrcution).
2.  two external interrupts.
3.  one simplify IO port (P0)
4.  UART, send only.
## exclude
1. external memory, all MOVX associated instructions.
  - MOVX A,@DPTR (0xE0)
  - MOVX A,@Ri   (0xE2,0xE3)
  - MOVX @Ri,A   (0xF2,0xF3)
2.  configureable clock(include clock interrupt).
3.  UART interrupt.
4.  three IO port (P1,P2,P3)
5.  power control.
