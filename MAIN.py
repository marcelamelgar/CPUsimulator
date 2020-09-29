from ALU import Alu
from CU import CU
from Registers import Registers
from clock import CPUclock
from Memory import Memory
from RAM import Ram
from ROM import Rom

class CPU:
    clock = CPUclock()
    def __init__ (self):
        self.alu = Alu()
        #self.clock = CPUclock()
        self.memory = Memory()
        self.ram = Ram()
        self.rom = Rom()
        self.registers = Registers()
        self.cu = CU()


    def main (self):
        execute = ' '
        PC = 0
        n = 0
        while (n == 0):
            self.clock.sleepScreen()
            fetch = self.cu.doFetch()
            for instructions in fetch:
                IAR = instructions.split()
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print("FETCH")
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Instruction:\n{IAR}\n")
                self.clock.sleepScreen()
                opcode, operand = self.cu.decode(IAR)

                print("~~~~~~~~~~~~~~~~~~~~~~")
                print("DECODE")
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Opcode: {opcode}\nOperand: {operand}\n")
                self.clock.sleepScreen()
                execute = self.cu.execute(opcode, operand)
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"EXECUTE")
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\n{execute}\n")
                if (execute == 'HALT'):
                    n = 1
                else: 
                    continue



program1 = CPU()
if __name__ == "__main__":
    program1.main()