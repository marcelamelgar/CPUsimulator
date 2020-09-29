from IntegratedCircuit import IntegratedCircuit
from RAM import Ram 
from Registers import Registers
from ROM import Rom
from ALU import Alu 
import sys


class CU(IntegratedCircuit):

    def __init__ (self):
        self.InsAddReg = ''
        self.opcode = " "
        self.operand = ''
        self.code = ''
        self.PC = 0
        self.IAR = ''
        self.ram = Ram()
        self.registers = Registers()
        self.rom = Rom()
        self.alu = Alu()

        

    #def __str__(self): 
        #return f"{fetch}"


    def doFetch (self):
        fetch = self.ram.getInstruction()
        for self.PC in fetch:
            self.IAR = self.PC.split()
            self.PC =+ 1
            return self.IAR
    


    def decode(self, instruction):
        getOpcode = instruction[0]
        if (len(instruction) < 3):
            getOperand = instruction[1]
        else:
            operand1 = instruction[1]
            operand2 = instruction[2]
        data = self.ram.getData()
        opcode = self.rom.istOpcode(getOpcode)
        operand = self.rom.convertOperand(getOperand)
        return opcode, operand

    def execute(self, opcode, operand):
        if (opcode == 'OutputToRam'):
            print("no entendi que hace")
        elif (opcode == 'RamToR0'):
            value = self.ram.getValue(operand)
            r0 = self.registers.reg0(value)
        elif (opcode == 'RamToR1'):
            value = self.ram.getValue(operand)
            r1 = self.registers.reg1(value)
        elif (opcode == 'DoesAND'):
            self.alu.logicand()
        elif (opcode == 'ReadConstantToR0'):
            Do = 'no entendi que hace'
        elif (opcode == 'FromR0ToRAM'):
            r0 = self.registers.reg0()
            self.ram.changeValue(operand, r0)
        elif (opcode == 'FromR1ToRAM'):
            r1 = self.registers.reg1()
            self.ram.changeValue(operand, r1)
        elif (opcode == 'PerformsOR'):
            self.alu.logicor()
        elif (opcode == 'ReadConstantToR1'):
            Do = 'no entendi'
        elif (opcode == 'AddTwoRegs'):
            answer = self.alu.add()
            r2 = self.registers.reg2(answer)
        elif (opcode == 'SubstractTwoRegs'):
            answer = self.alu.sub()
            r2 = self.registers.reg2(answer)
        elif (opcode == 'Jump'):
            Do = 'no entendi'
        elif (opcode == 'NegativaAluJump'):
            Do = 'negativealu'
        elif (opcode == 'Multiply'):
            Do = 'multiply'
        elif (opcode == 'Divide'):
            Do = 'divide'
        elif (opcode == 'ProgramDone'):
            Do = exit()
        return Do
            
        
        

    #def execute (self):
        #pass

    def InstructionAddressRegister(self):
        return self.InsAddReg

#ins = ['LOAD_R0', 'R0', 'R1']
#ejemplo = CU()
#print(ejemplo.decode(ins))
#print = ejemplo.execute(var)