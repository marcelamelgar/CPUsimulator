from ROM import Rom
import random

class Ram:

    def __init__(self):
        self.instructions = open("cpufm.txt", "r")
        self.code = []
        for line in self.instructions: 
            if not line.strip().startswith(";"):
                instruction = line.strip()
                self.code.append(instruction)      
        self.rom = Rom()
        self.data = self.rom.getData()        
    
    def getInstruction(self):
        return self.code

    def getData(self):
        return self.data

    def getDataBits(self):
        bitsData = []
        for val in self.data:
            bits = self.rom.radixConverter(val)
            bitsData.append(bits)
        return bitsData

    def getValue (self, position):
        position = int(position)
        return self.data[position]

    def changeValue (self, position, value):
        position = int(position)
        value = int(value)
        newVal = self.data[position] = value
        return newVal

    def InsAddReg (self):
        number = random.randint(1, 15)
        insAddReg = self.rom.radixConverter(number)
        return insAddReg

      
