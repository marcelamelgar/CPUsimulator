from ROM import Rom
import random

class Ram:

    def __init__(self): 
        self.rom = Rom()
        self.data = self.rom.getData()        
        self.code = []
        
        string = """
        What file '.cpufm' do you want to use?\n
        1. ejemplo1.cpufm
        2. ejemplo2.cpufm
        3. ejemplo3.cpufm
        4. ejemplo4.cpufm
        5. ejemplo5.cpufm
        6. ejemplo6.cpufm
        7. ejemplo7.cpufm 
            """
        print(string)
        files = input("Enter the name of the file of your choice: ")

        self.instructions = open(files, "r")
        for line in self.instructions: 
            if not line.strip().startswith(";"):
                instruction = line.strip()
                self.code.append(instruction)

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

      
