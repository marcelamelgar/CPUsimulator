from ROM import Rom
from CU import CU
from ALU import Alu
from clock import CPUclock
from Registers import Registers
from RAM import Ram
class PrettyPrint():

    def __init__(self):
        self.pprint =''
        self.registers = Registers()
        self.rom = Rom()
        self.alu = Alu()
        self.clock = CPUclock()
        self.cu = CU()
        self.ram = Ram()
    

    def drawing(self):
        r0 = self.registers.getReg0()
        r1 = self.registers.getReg1()
        r2 = self.registers.getReg2()
        rout = self.registers.outputreg()
        clck = self.clock.getClock()
        data = self.ram.getDataBits()
        insar = self.ram.InsAddReg()
        self.pprint = input("Press 1 to print the CPU's current state")
        if(self.pprint == '1'):
            print("     ----------     ----------    -----------    -----------                                         ~R A M~")
            print("     |   R0   |     |   R1   |    |   R2    |    |   OUT   |------------------------------------|adress  data |")
            print(f"     |  {r0}     |     |  {r1}     |    |  {r2}      |    |  {rout}      |                                    | 0000 | {data[0]} |")
            print(f"     ----------     ----------    -----------    -----------                                    | 0001 | {data[1]} |")
            print(f"         |              |                 |           |                                         | 0010 | {data[2]} |")
            print(f"         |               --------------¬   ---¬       |                                         | 0011 | {data[3]} |")
            print(f"         ---------------------------¬  |      |       |                                         | 0100 | {data[4]} |")
            print(f"                                     | |      |       |                                         | 0101 | {data[5]} |")
            print(f"                                    **************************************                      | 0110 | {data[6]} |")
            print(f"                                    * Control Unit                       *                      | 0111 | {data[7]} |")
            print(f"                ------------------- *                                    *                      | 1000 | {data[8]} |")
            print(f"                |    |              *             --------------         *                      | 1001 | {data[9]} |")
            print(f"        -------------------         *            | opcode|operand |      *                      | 1010 | {data[10]} |")
            print(f"         \     ALU       /          *            |       |        |      *                      | 1011 | {data[11]} |")
            print(f"          \             /           *             ---------------        *                      | 1100 | {data[12]} |")
            print(f"           \   + -     /            *                                    *                      | 1101 | {data[13]} |")
            print(f"            \  &  *   /             *            -----------------       *                      | 1110 | {data[14]} |")
            print(f"             \       /              *           |  inst.addr.reg  |      *                      | 1111 | {data[15]} |")
            print(f"              \     /               *            |    {insar}         |      *                     ---------------")
            print("               \___/                **************************************")
            print("                  |                        |                           |")
            print("                   ------------------------                            |")
            print("                                                                 ------------")
            print("                                                                | clock      |")
            print(f"                                                               |    {clck}  |")
            print("                                                                 ------------")
        else:
            print("Program has come to an end")