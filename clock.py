import time
from ROM import Rom

class CPUclock:
    clock = Rom() 
    hrtz = 0
    frecuencia = clock.getClock()
    hrtz = 1/frecuencia
    
    def getClock(self):
        return self.hrtz

    def sleepScreen(self):
        time.sleep(self.hrtz) 
