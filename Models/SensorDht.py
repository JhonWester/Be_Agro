from dht import DHT11
from machine import Pin

class SensorDHT:
    
    def __init__(self, puerto):
        self.__sensor = DHT11(Pin(puerto))
        self.temperatura = 0
        self.humedad = 0
        
    def getData(self):
        self.__sensor.measure()
        self.temperatura = self.__sensor.temperature()
        self.humedad = self.__sensor.humidity()