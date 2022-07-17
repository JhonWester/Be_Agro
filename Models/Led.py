from machine import Pin

class Led:
    
    def __init__(self, pin) -> None:
        self.__light = Pin(pin, Pin.OUT)
    
    def ledOff(self):
        self.__light.off()
    
    def ledOn(self):
        self.__light.on()


    def stateLed(self):
        return self.__light.value()