from ALU import Alu
from CU import CU
from Registers import Registers
from clock import CPUclock
from Memory import Memory
from RAM import Ram
from ROM import Rom
from PrettyPrint import PrettyPrint

class CPU:
    clock = CPUclock()
    def __init__ (self):
        self.alu = Alu()
        self.memory = Memory()
        self.rom = Rom()
        self.registers = Registers()
        self.cu = CU()
        self.ram = Ram()

    #hay un glitch que se repite el proceso
    #de seleccionar el file dos veces
    #no supimos como arreglarlo
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
        PrettyPrint.drawing(self)

program1 = CPU()
if __name__ == "__main__":
    program1.main()
