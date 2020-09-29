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

        

    def doFetch (self):
        fetch = self.ram.getInstruction()
        for self.PC in fetch:
            self.IAR = self.PC.split()
            self.PC =+ 1
            return self.IAR
    


    def decode(self, instruction):
        getOpcode = instruction[0]
        opcode = self.rom.istOpcode(getOpcode)
        if (len(instruction) < 3):
            operand = self.rom.convertOperand(instruction[1])
        else:
            operand1 = self.rom.convertOperand(instruction[1])
            operand2 = self.rom.convertOperand(instruction[2])
            operand = [operand1, operand2]
        data = self.ram.getData()
        return opcode, operand

    def execute(self, opcode, operand):
        if (opcode == 'OutputToRam'):
            print("no entendi que hace")
        elif (opcode == 'RamToR0'):
            value = self.ram.getValue(operand)
            r0 = self.registers.reg0(value)
            return r0
        elif (opcode == 'RamToR1'):
            value = self.ram.getValue(operand)
            r1 = self.registers.reg1(value)
            return r1
        elif (opcode == 'DoesAND'):
            id1, id2 = self.rom.registerID(operand)
            AND = self.alu.logicand(id1, id2)
            return AND
        elif (opcode == 'ReadConstantToR0'):
            Do = 'no entendi que hace'
        elif (opcode == 'FromR0ToRAM'):
            r0 = self.registers.reg0()
            return self.ram.changeValue(operand, r0)
        elif (opcode == 'FromR1ToRAM'):
            r1 = self.registers.reg1()
            return self.ram.changeValue(operand, r1)
        elif (opcode == 'PerformsOR'):
            id1, id2 = self.rom.registerID(operand)
            OR = self.alu.logicor(id1, id2)
            return OR
        elif (opcode == 'ReadConstantToR1'):
            Do = 'no entendi'
        elif (opcode == 'AddTwoRegs'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.add(val1, val2)
            r2 = self.registers.reg2(answer)
            return r2
        elif (opcode == 'SubstractTwoRegs'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.sub(val1, val2)
            r2 = self.registers.reg2(answer)
            return r2
        elif (opcode == 'Jump'):
            Do = 'no entendi'
        elif (opcode == 'NegativeAluJump'):
            Do = 'negativealu'
        elif (opcode == 'Multiply'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.multiply(val1, val2)
            r2 = self.registers.reg2(answer)
            return r2
        elif (opcode == 'Divide'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.divide(val1, val2)
            r2 = self.registers.reg2(answer)
            return r2
        elif (opcode == 'ProgramDone'):
            return "The program has come to an End"
            

    def InstructionAddressRegister(self):
        return self.InsAddReg




ins = ['LOAD_R0', 'F']
ejemplo = CU()
print(ejemplo.decode(ins))
