from machine import Pin, I2C
from Package.ssd1306 import SSD1306_I2C
import ujson
import time

class Screen:
    
    with open("./Shared/config.json") as config_file:
        data = ujson.load(config_file)
        
    height = data["oled"]["height"]
    width = data["oled"]["width"]
    
    def __init__(self, scl, sda) -> None:
        self.__i2c = I2C(0, scl = Pin(scl), sda = Pin(sda))
        self.__oled = SSD1306_I2C(self.__class__.width, self.__class__.height, self.__i2c)
        print(self.__i2c.scan())

        
    def FillMessage(self, colum, file, message):
        self.__oled.text(message, colum, file)
        
    def clear(self, value):
        self.__oled.fill(value)
    
    def ShowMessage(self):
        self.__oled.show()
        
    def MessagesInitOled(self):
        #Show init message
        self.__oled.fill(0)
        self.__oled.text("Bienvenido a BE_AGRO!!!", 0, 0)
        self.__oled.text("Procesando...", 0, 10)
        self.__oled.text("________________", 0, 20)
        self.__oled.show()
        time.sleep(2)
        self.__oled.fill(0)
        self.__oled.text("__BE_AGRO__", 0, 0)
        self.__oled.text("Procesando...", 0, 10)
        self.__oled.show()
        self.__oled.fill(0)
        time.sleep(2)