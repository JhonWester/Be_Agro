# main.py
import time

# Package
from Models.SensorDht import SensorDHT
from Models.FireConnect import FirebaseConnect
from Models.PowerBomb import PowerBomb
from Models.SensorAnalogo import SensorAnalogo
from Shared.NetworkConnect import NetworkConnection

red = {'name': 'TP-Link_D54E', 'pass': '04577041'}

#Sensor de dht11
sensorDHT = SensorDHT(4)

#conexion Internet
connection = NetworkConnection(red['name'], red['pass'])

#Conexion Firebase
fireDB = FirebaseConnect()

#Bomba de agua
powerBomb = PowerBomb(5)

#Sensor de humedad tierra (pin, minimo, maximo)
sensorFT = SensorAnalogo(36, 620, 1023)

#Sensor de luz (pin, minimo, maximo)
sensorLDR = SensorAnalogo(39, 65, 650)

#Inicios de los procesos y recoleccion de datos de los dispositivos
def main():
    if connection.conectaWifi():
        while True:
            #proccessDHT()
            #data = [sensorDHT.temperatura, sensorDHT.humedad]
            #connection.sendData(data)
            #fireDB.sendDHT(sensorDHT.humedad, sensorDHT.temperatura)

            #proccessFC()
            proccessBomb()
            #proccessLDR()
    else:
        print ("Imposible conectar")
        #oled.text("Imposible conectar!!!", 0 , 1) # columna ---- fila
        #oled.show()
        connection.desactive()

#Ejecucion proceso de sensor dht11
def proccessDHT():
    time.sleep(4)
    sensorDHT.getData()
    print("T={:02.} ºC, H={:02d} %".format(sensorDHT.temperatura, sensorDHT.humedad))

#Ejecucion proceso de bomba
def proccessBomb():
    time.sleep(4)
    state = powerBomb.doPowerBomb()
    if state == True:
        print("Bomba de agua activa")
    else:
        print("Bomba Apagada")

#Ejecucion proceso de sensor de humedad de tierra
def proccessFC():
    time.sleep(4)
    print(sensorFT.map(), "%")

#Ejecucion proceso de fotocelda
def proccessLDR():
    time.sleep(4)
    print(sensorLDR.map(), "%")
if __name__ == '__main__':
    main()