from machine import Pin, I2C
from Package.ssd1306 import SSD1306_I2C

class Screen:
    
    height = 128
    width = 64
    
    def __init__(self, scl, sda) -> None:
        self.__i2c = I2C(0, scl = Pin(scl), sda = Pin(sda))
        self.__oled = SSD1306_I2C(self.__class__.width, self.__class__.height, self.__i2c)
        
    def FillMessage(self, colum, file, message):
        self.__oled.text(message, colum, file)
    
    def ShowMessage(self):
        self.__oled.show()
        