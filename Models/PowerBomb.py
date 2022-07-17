from machine import Pin

class PowerBomb:
    
    def __init__(self, pin) -> None:
        self.__state = Pin(pin, Pin.OUT)
        self.doPowerBomb()
        
    def doPowerBomb(self):
        actuallyValue = not self.__state.value()
        self.__state.value(actuallyValue)
        return not actuallyValue