from IntegratedCircuit import IntegratedCircuit

class Registers(IntegratedCircuit):

    def __init__ (self):
        self.place = ''
        self.r0 = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.iar = 0
        self.inpt = 0
        self.outpt = 0
        #self.regAdress = [r0, r1, r2, r3]
    

    def getRegAdress (self, operand):
        if (operand == "R0"):
           address = 0
        elif (operand == "R1"):
            address = 1
        elif (operand == "R2"):
            address = 2
        if (operand == "R3"):
            address = 4
        return address

    def getRegValue (self, operand):
        if (operand == "R0"):
           return self.r0
        elif (operand == "R1"):
            return self.r1
        elif (operand == "R2"):
            return self.r2
        elif (operand == "R3"):
            return self.r3


    def getReg0 (self):
        return self.r0

    def reg0 (self, val):
        self.r0 = val
        return self.r0

    def getReg1(self):
        return self.r1

    def reg1(self, val):
        self.r1 = val
        return self.r1

    def getReg2(self):
        return self.r2

    def reg2(self, val):
        self.r2 = val
        return self.r2

    def getReg3(self):
        return self.r3

    def reg3(self, val):
        self.r3 = val
        return self.r3

    def pc(self):
        return self.iar

    def pc(self, val):
        self.iar = val
        return self.iar    
    
    def inputreg(self):
        return self.inpt

    def outputreg(self):
        return self.outpt