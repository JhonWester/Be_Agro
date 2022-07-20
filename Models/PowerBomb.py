from machine import Pin

#Modulo relee
class PowerBomb:
    
    def __init__(self, pin) -> None:
        self.__state = Pin(pin, Pin.OUT)
        self.BombOff()
        
    def BombOn(self):
        self.__state.value(0)
        
    def BombOff(self):
        self.__state.value(1)
        