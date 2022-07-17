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
        self.__oled.FillMessage("Bienvenido a BE_AGRO!!!", 0 , 0)
        self.__oled.FillMessage("Procesando...", 0 , 16)
        self.__oled.FillMessage("_______________________", 0 , 32)
        self.__oled.show()
        time.sleep(2)
        self.__oled.FillMessage("____BE_AGRO____", 0 , 0)
        self.__oled.FillMessage("Procesando...", 0 , 16)
        self.__oled.clear()
        time.sleep(2)
        self.__oled.clear(1)
        time.sleep(2)
        self.__oled.clear(0)