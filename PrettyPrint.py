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

    def getreg0(self):
        return self.registers.r0()
    def getreg1(self):
        return self.registers.reg1()
    def getreg2(self):
        return self.registers.reg2()
    def getregout(self):
        return self.registers.outputreg()
    #def getopcode(self):
        #return self.cu.decode()
    #def getoperand(self):
        #return self.execute.operand() ggffwweewedsweqaqweqweqweasddf
    #def getiar(self):
        #return self.cu.InstructionAddressRegister()
    #def getclock(self):
        #return self.clock.tiempo.frecuencia()
    

    def drawing(self):
        self.pprint = input("press 1 to print the CPU's current state")
        if(self.pprint == '1'):
            print("     ----------     ----------    -----------    -----------                                         ~R A M~")
            print("     |  R0    |     |   R1   |    |   R2    |    |   OUT   |------------------------------------|adress  data |")
            print("     |        |     |        |    |         |    |         |                                    | 0000 |      |")
            print("     ----------     ----------    -----------    -----------                                    | 0001 |      |")
            print("         |              |                 |           |                                         | 0010 |      |")
            print("         |               --------------¬   ---¬       |                                         | 0011 |      |")
            print("         ---------------------------¬  |      |       |                                         | 0100 |      |")
            print("                                     | |      |       |                                         | 0101 |      |")
            print("                                    **************************************                      | 0110 |      |")
            print("                                    * Control Unit                       *                      | 0111 |      |")
            print("                ------------------- *                                    *                      | 1000 |      |")
            print("                |    |              *             --------------         *                      | 1001 |      |")
            print("        -------------------         *            | opcode|operand |      *                      | 1010 |      |")
            print("         \     ALU       /          *            |       |        |      *                      | 1011 |      |")
            print("          \             /           *             ---------------        *                      | 1100 |      |")
            print("           \   + -     /            *                                    *                      | 1101 |      |")
            print("            \  &  *   /             *            -----------------       *                      | 1110 |      |")
            print("             \       /              *           |  inst.addr.reg  |      *                      | 1111 |      |")
            print("              \     /               *           |                 |      *                      ---------------")
            print("               \___/                **************************************")
            print("                  |                        |                           |")
            print("                   ------------------------                            |")
            print("                                                                 ------------")
            print("                                                                | clock      |")
            print("                                                                |            |")
            print("                                                                 ------------")

ejemplo = PrettyPrint()
print(ejemplo.drawing())