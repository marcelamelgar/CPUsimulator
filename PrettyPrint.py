from ROM import Rom
from CU import CU
from ALU import Alu
from clock import CPUclock
from Registers import Registers

class PrettyPrint():

    def __init__(self):
        self.pprint =''
        self.registers = Registers()
        self.rom = Rom()
        self.alu = Alu()
        self.clock = CPUclock()
        self.cu = CU()

    

    def drawing(self):
        r0 = self.registers.getReg0()
        r1 = self.registers.getReg1()
        r2 = self.registers.getReg2()
        rout = self.registers.outputreg()
        clck = self.clock.sleepScreen()
        self.pprint = input("press 1 to print the CPU's current state")
        if(self.pprint == '1'):
            print("     ----------     ----------    -----------    -----------                                         ~R A M~")
            print("     |   R0   |     |   R1   |    |   R2    |    |   OUT   |------------------------------------|adress  data |")
            print(f"     |  {r0}     |     |  {r1}     |    |  {r2}      |    |  {rout}      |                                    | 0000 |      |")
            print(f"     ----------     ----------    -----------    -----------                                    | 0001 |      |")
            print(f"         |              |                 |           |                                         | 0010 |      |")
            print(f"         |               --------------¬   ---¬       |                                         | 0011 |      |")
            print(f"         ---------------------------¬  |      |       |                                         | 0100 |      |")
            print(f"                                     | |      |       |                                         | 0101 |      |")
            print(f"                                    **************************************                      | 0110 |      |")
            print(f"                                    * Control Unit                       *                      | 0111 |      |")
            print(f"                ------------------- *                                    *                      | 1000 |      |")
            print(f"                |    |              *             --------------         *                      | 1001 |      |")
            print(f"        -------------------         *            | opcode|operand |      *                      | 1010 |      |")
            print(f"         \     ALU       /          *            |       |        |      *                      | 1011 |      |")
            print(f"          \             /           *             ---------------        *                      | 1100 |      |")
            print(f"           \   + -     /            *                                    *                      | 1101 |      |")
            print(f"            \  &  *   /             *            -----------------       *                      | 1110 |      |")
            print(f"             \       /              *           |  inst.addr.reg  |      *                      | 1111 |      |")
            print("              \     /               *           |                 |      *                      ---------------")
            print("               \___/                **************************************")
            print("                  |                        |                           |")
            print("                   ------------------------                            |")
            print("                                                                 ------------")
            print("                                                                | clock      |")
            print(f"                                                                |    {clck}    |")
            print("                                                                 ------------")

ejemplo = PrettyPrint()
print(ejemplo.drawing())