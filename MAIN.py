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
        self.memory = Memory()
        self.rom = Rom()
        self.registers = Registers()
        self.cu = CU()


    def main (self):
        execute = ' '
        PC = 0
        n = 0
        while (n == 0):
            fetch = self.cu.doFetch()
            for instructions in fetch:
                IAR = instructions.split()
                self.clock.sleepScreen()
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print("FETCH")
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Instruction:{IAR}\n")
                opcode, operand = self.cu.decode(IAR)
                self.clock.sleepScreen()
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print("DECODE")
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Opcode: {opcode}\nOperand: {operand}\n")
                execute = self.cu.execute(opcode, operand)
                self.clock.sleepScreen()
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"EXECUTE")
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print(f"{execute}\n")
                if (execute == 'HALT'):
                    n = 1
                else: 
                    continue



program1 = CPU()
if __name__ == "__main__":
    program1.main()
