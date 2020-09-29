from ROM import Rom

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

    def getValue (self, position):
        position = int(position)
        return self.data[position]

    def changeValue (self, position, value):
        position = int(position)
        value = int(value)
        newVal = self.data[position] = value
        return newVal

#ejemplo = Ram()
#print(ejemplo.getData())
#print(ejemplo.changeValue('4', '14'))
#print(ejemplo.getData())
      
