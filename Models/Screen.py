from machine import Pin, I2C
from Package.ssd1306 import SSD1306_I2C
import time

class Screen:
    
    height = 128
    width = 64
    
    def __init__(self, scl, sda) -> None:
        self.__i2c = I2C(0, scl = Pin(scl), sda = Pin(sda))
        self.__oled = SSD1306_I2C(self.__class__.width, self.__class__.height, self.__i2c)
        
    def FillMessage(self, colum, file, message):
        self.__oled.text(message, colum, file)
        
    def clear(self, value):
        self.__oled.fill(value)
    
    def ShowMessage(self):
        self.__oled.show()
        
    def MessagesInitOled(self):
        #Show init message
        self.FillMessage(0 , 0, "Bienvenido a BE_AGRO!!!")
        self.FillMessage(0 , 16, "Procesando...")
        self.FillMessage(0 , 32, "_______________________")
        self.__oled.show()
        time.sleep(2)
        self.FillMessage(0 , 0, "____BE_AGRO____")
        self.FillMessage(0 , 16, "Procesando...")
        self.__oled.show()
        time.sleep(2)
        self.clear(1)
        time.sleep(2)
        self.clear(0)