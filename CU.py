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
        self.IAR = ''
        self.ram = Ram()
        self.registers = Registers()
        self.rom = Rom()
        self.alu = Alu()

        
    def getInsAddReg (self):
        return self.InsAddReg

    def doFetch (self):
        fetch = self.ram.getInstruction()
        return fetch

    def decode(self, instruction):
        getOpcode = instruction[0]
        opcode = self.rom.istOpcode(getOpcode)

        if (len(instruction) == 1):
            operand = '0'
        elif (len(instruction) < 3):
            operand = self.rom.convertOperand(instruction[1])
        else:
            operand1 = self.rom.convertOperand(instruction[1])
            operand2 = self.rom.convertOperand(instruction[2])
            operand = [operand1, operand2]
        data = self.ram.getData()
        return opcode, operand

    def execute(self, opcode, operand):
        if (opcode == 'OutputToRam'):
            return "OUTPUT TO RAM DONE"
        elif (opcode == 'RamToR0'):
            value = self.ram.getValue(operand)
            r0 = self.registers.reg0(value)
            return f"RAM value | {value} | moved to R0"
        elif (opcode == 'RamToR1'):
            value = self.ram.getValue(operand)
            r1 = self.registers.reg1(value)
            return f"RAM value | {value} | moved to R1"
        elif (opcode == 'DoesAND'):
            id1, id2 = self.rom.registerID(operand)
            AND = self.alu.logicand(id1, id2)
            return f""" 
AND BETWEEN {operand}
RESULT: {AND}
            """
        elif (opcode == 'ReadConstantToR0'):
            value = self.ram.getValue(operand)
            r0 = self.registers.reg0(value)
            return f"RAM value | {value} | moved to R0"
        elif (opcode == 'FromR0ToRAM'):
            r0 = self.registers.getReg0()
            newVal = self.ram.changeValue(operand, r0)
            return f"""
VALUE R0: {r0}
MOVED TO RAM LOCATION: {operand}
            """
        elif (opcode == 'FromR1ToRAM'):
            r1 = self.registers.getReg1()
            newPosition = self.ram.changeValue(operand, r1)
            return f"""
VALUE R0: {r1}
MOVED TO RAM LOCATION: {operand}
            """
        elif (opcode == 'PerformsOR'):
            id1, id2 = self.rom.registerID(operand)
            OR = self.alu.logicor(id1, id2)
            return f"""
OR BETWEEN {operand}
RESULT: {OR}
            """
        elif (opcode == 'ReadConstantToR1'):
            value = self.ram.getValue(operand)
            r1 = self.registers.reg1(value)
            return f"RAM value | {value} | moved to R1"
        elif (opcode == 'AddTwoRegs'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.add(val1, val2)
            r2 = self.registers.reg2(answer)
            return f"""
SUM BETWEEN {operand[0]} - {operand[0]}
RESULT: {answer}
STORED IN R2
            """
        elif (opcode == 'SubstractTwoRegs'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.sub(val1, val2)
            r2 = self.registers.reg2(answer)
            return f"""
SUBTRACTION BETWEEN {operand[0]} - {operand[0]}
RESULT: {answer}
STORED IN R2
            """
        elif (opcode == 'Jump'):
            InsAddReg = self.ram.InsAddReg()
            self.InsAddReg = InsAddReg
            return f"""
NEW INSTANT ADDRESS REGISTER
{self.InsAddReg}
            """
        elif (opcode == 'NegativeAluJump'):
            InsAddReg = self.ram.InsAddReg()
            self.InsAddReg = InsAddReg
            return f"""
ALU: NEGATIVE
INSTANT ADDRESS REGISTER 
UPDATED TO {self.InsAddReg}
            """
        elif (opcode == 'Multiply'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.multiply(val1, val2)
            r2 = self.registers.reg2(answer)
            return f"""
MULTIPLICATION BETWEEN {operand[0]} - {operand[0]}
RESULT: {answer}
STORED IN R2
            """
        elif (opcode == 'Divide'):
            val1 = self.registers.getRegValue(operand[0])
            val2 = self.registers.getRegValue(operand[1])
            answer = self.alu.divide(val1, val2)
            r2 = self.registers.reg2(answer)
            return f"""
DIVISION BETWEEN {operand[0]} - {operand[0]}
RESULT: {answer}
STORED IN R2
            """
        elif (opcode == 'ProgramDone'):
            return "HALT"
            

    def InstructionAddressRegister(self):
        return self.InsAddReg
