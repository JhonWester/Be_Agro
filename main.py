# main.py
import time

# Package
from Models.SensorDht import SensorDHT
from Shared.NetworkConnect import NetworkConnection

red = {'name': 'TP-Link_D54E', 'pass': '04577041'}
sensorDHT = SensorDHT(15)
connection = NetworkConnection(red['name'], red['pass'])


# Proceso de datos de los dispositivos
def main():
    print('test')
    if connection.conectaWifi():
        while True:
            proccessDHT()
            data = [sensorDHT.temperatura, sensorDHT.humedad]
            connection.sendData(data)
    else:
        print ("Imposible conectar")
        #oled.text("Imposible conectar!!!", 0 , 1) # columna ---- fila
        #oled.show()
        connection.desactive()

def proccessDHT():
    time.sleep(4)
    sensorDHT.getData()
    print("T={:02.} ºC, H={:02d} %".format(sensorDHT.temperatura, sensorDHT.humedad))


if __name__ == '__main__':
    main()