from dht import DHT11
from machine import Pin

class SensorDHT:
    
    def __init__(self, puerto):
        self.__sensor = DHT11(Pin(puerto))
        self.temperature = 0
        self.humidity = 0
        
    def getData(self):
        self.__sensor.measure()
        self.temperature = self.__sensor.temperature()
        self.humidity = self.__sensor.humidity()