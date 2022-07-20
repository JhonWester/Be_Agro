from machine import Pin, ADC

class SensorAnalogo:
    
    def __init__(self, pin, min, max) -> None:
        self.__state = ADC(Pin(pin))
        self.__state.atten(ADC.ATTN_11DB)
        self.__state.width(ADC.WIDTH_10BIT)
        self.__min = min
        self.__max = max
        self.Range = (self.__max - self.__min)
        
    def map(self):
        value = self.__state.read()
        if value > self.__max:
            return 0
        elif value < self.__min:
            return 100
        else:
            state = (value * 100) / self.__max
            return int(100 - state)
        
    def result(self):
        return self.__state.read()
        