import yaml
from Registers import Registers

class Rom:

    def __init__(self):
        self.opcode = str
        self.operand = int
        self.registers = Registers()
        with open ('bios.yaml', 'r') as bios:
            self.bios = yaml.full_load(bios)
        
        for toDo in self.bios:
            self.clock = self.bios["clock"]
            self.visual = self.bios["visualization"]
            self.Ram = self.bios["RAM"]
            self.instructions = self.Ram["instructions"]
            self.data = self.Ram.get("data")

    def getClock(self):
        return self.clock

    def getVisualization(self):
        return self.visual

    def getRam (self):
        return self.Ram

    def getInstructions (self):
        return self.instructions

    def getData(self):
        return self.data





        


    """def ramtable (self):
        p0 = self.bios['RAM']['data'][0]
        p1 = self.bios['RAM']['data'][1]
        p2 = self.bios['RAM']['data'][2]
        p3 = self.bios['RAM']['data'][3]
        p4 = self.bios['RAM']['data'][4]
        p5 = self.bios['RAM']['data'][5]
        p6 = self.bios['RAM']['data'][6]
        p7 = self.bios['RAM']['data'][7]
        p8 = self.bios['RAM']['data'][8]
        p9 = self.bios['RAM']['data'][9]
        p10 = self.bios['RAM']['data'][10]
        p11 = self.bios['RAM']['data'][11]
        p12 = self.bios['RAM']['data'][12]
        p13 = self.bios['RAM']['data'][13]
        p14 = self.bios['RAM']['data'][14]
        p15 = self.bios['RAM']['data'][15]

        self.data = {}
        self.data['0'] = p0
        self.data['1'] = p1
        self.data['2'] = p2
        self.data['3'] = p3
        self.data['4'] = p4
        self.data['5'] = p5
        self.data['6'] = p6
        self.data['7'] = p7
        self.data['8'] = p8
        self.data['9'] = p9
        self.data['10'] = p10
        self.data['11'] = p11
        self.data['12'] = p12
        self.data['13'] = p13
        self.data['14'] = p14
        self.data['15'] = p15

        print(self.data)"""


    def istOpcode (self, opcode):
        self.opcode = opcode
        while (True):
            if (self.opcode == '0000' or self.opcode == 'OUTPUT' or self.opcode == 'OUT'):
                instruct = 'OutputToRam'
            elif (self.opcode == '0001' or self.opcode == 'LOAD_R0' or self.opcode == 'LD_R0'):
                instruct = 'RamToR0'
            elif (self.opcode == '0010' or self.opcode == 'LOAD_R1' or self.opcode == 'LD_R1'):
                instruct = 'RamToR1'
            elif (self.opcode == '0011' or self.opcode == 'AND'):
                instruct = 'DoesAND'
            elif (self.opcode == '0100' or self.opcode == 'ILD_R0'):
                instruct = 'ReadConstantToR0'
            elif (self.opcode == '0101' or self.opcode == 'STR_R0' or self.opcode == 'STORE_R0'):
                instruct = 'FromR0ToRAM'
            elif (self.opcode == '0110' or self.opcode == 'STR_R1' or self.opcode == 'STORE_R1'):
                instruct = 'FromR1ToRAM'
            elif (self.opcode == '0111' or self.opcode == 'OR'):
                instruct = 'PerformsOR'  
            elif (self.opcode == '1000' or self.opcode == 'ILD_R1'):
                instruct = 'ReadContantToR1'
            elif (self.opcode == '1001' or self.opcode == 'ADD'):
                instruct = 'AddTwoRegs'
            elif (self.opcode == '1010' or self.opcode == 'SUB'):
                instruct = 'SubstractTwoRegs'
            elif (self.opcode == '1011' or self.opcode == 'JMP' or self.opcode == 'JUMP'):
                instruct = 'Jump'
            elif (self.opcode == '1100' or self.opcode == 'JMP_N' or self.opcode == 'JUMP_NEG'):
                instruct = 'NegativeAluJump'
            elif (self.opcode == '1101'):
                instruct = 'Multiply'
            elif (self.opcode == '1110'):
                instruct = 'Divide'
            elif (self.opcode == '1111' or self.opcode == 'HALT' or self.opcode == 'HLT'):
                instruct = 'ProgramDone'
            return instruct


    def convertOperand(self, operand):
        self.operand = operand
        if (self.operand == '0000' or self.operand == '0'):
            location = self.data[0]
        elif (self.operand == '0001' or self.operand == '1'):
            location = self.data[1]
        elif (self.operand == '0010' or self.operand == '2'):
            location = self.data[2]
        elif (self.operand == '0011' or self.operand == '3'):
            location = self.data[3]
        elif (self.operand == '0100' or self.operand == '4'):
            location = self.data[4]
        elif (self.operand == '0101' or self.operand == '5'):
            location = self.data[5]
        elif (self.operand == '0110' or self.operand == '6'):
            location = self.data[6]
        elif (self.operand == '0111' or self.operand == '7'):
            location = self.data[7]
        elif (self.operand == '1000' or self.operand == '8'):
            location = self.data[8]
        elif (self.operand == '1001' or self.operand == '9'):
            location = self.data[9]
        elif (self.operand == '1010' or self.operand == '10' or self.operand == 'A'):
            location = self.data[10]
        elif (self.operand == '1011' or self.operand == '11' or self.operand == 'B'):
            location = self.data[11]
        elif (self.operand == '1100' or self.operand == '12' or self.operand == 'C'):
            location = self.operand
        elif (self.operand == '1101' or self.operand == '13' or self.operand == 'D'):
            location = self.data[13]
        elif (self.operand == '1110' or self.operand == '14' or self.operand == 'E'):
            location = self.data[14]
        elif (self.operand == '1111' or self.operand == '15' or 'F'):
            location = self.data[15]
        elif (self.operand == 'R0' or self.operand == 'R1' or self.operand == 'R2' or self.operand == 'R3'):
            location = self.operand
        return location

    def radixConverter (self, operand):
        if (operand > 1 and operand < 15):
            return bin(operand).replace("0b", "")


    def binaryToDecimal (self, operand):
        return int(operand,2)

operand = "11"
ejemplo = Rom()
print(ejemplo.binaryToDecimal(operand))
