# main.py
import time

# Models
from Models.SensorDht import SensorDHT
from Models.FireConnect import FirebaseConnect
from Models.PowerBomb import PowerBomb
from Models.SensorAnalogo import SensorAnalogo
from Models.Led import Led
from Models.Screen import Screen

#Package
from Shared.NetworkConnect import NetworkConnection

red = {'name': 'TP-Link_D54E', 'pass': '04577041'}

#Sensor de dht11
sensorDHT = SensorDHT(4)

#Conexion Internet
connection = NetworkConnection(red['name'], red['pass'])

#Conexion Firebase
fireDB = FirebaseConnect()

#Bomba de agua
powerBomb = PowerBomb(5)

#Sensor de humedad tierra (pin, minimo, maximo)
sensorFT = SensorAnalogo(36, 620, 1023)

#Sensor de luz (pin, minimo, maximo)
sensorLDR = SensorAnalogo(39, 65, 650)

#Pantalla oled (Pin scl, Pin sda)
screen = Screen(22, 21)

#Salidas led
ledBomb = Led(2)
ledHumidity = Led(4)

#Inicios de los procesos y recoleccion de datos de los dispositivos

#Record values send to cloud
valueDHT = [0, 0]
valueFC = 0
valueLDR = 0

def main():
    
    #Show init message
    screen.FillMessage("Bienvenido a BE_AGRO!!!", 0 , 10)
    screen.ShowMessage()
    
    try:
        if connection.conectaWifi():
            
            while True:
                proccessBomb(False)
                
                environment = proccessDHT()
                
                groundMoisture = proccessFC()
                
                light = proccessLDR()
                
                if (light > 80 and groundMoisture < 50):
                    proccessBomb(True)
                else:
                    
                    if (groundMoisture < 50 and environment > 33):
                        proccessBomb(True)
                    else:
                        proccessBomb(False)

                screen.ShowMessage()
                time.sleep(5)
                    
        else:
            print ("Imposible conectar")
            screen.FillMessage(0 , 20, "Imposible conectar!!!")
            screen.ShowMessage()
            connection.desactive()
    except:
        print ("Ocurrio un problema!!!")
        screen.FillMessage(0 , 20, "Ocurrio un problema!!!")
        screen.ShowMessage()


#Ejecucion proceso de sensor dht11
def proccessDHT():
    time.sleep(4)
    sensorDHT.getData()
    messageDHT = "T={:02.} ºC, H={:02d}%".format(sensorDHT.temperature, sensorDHT.humidity)
    screen.FillMessage(0, 20, messageDHT)
    
    if (valueDHT[0] != sensorDHT.humidity | valueDHT[1] != sensorDHT.temperature):
        valueDHT[0] = sensorDHT.humidity
        valueDHT[1] = sensorDHT.temperature
        fireDB.sendDHT(sensorDHT.humidity, sensorDHT.temperature)
    return sensorDHT.temperature
        

#Ejecucion proceso de bomba
def proccessBomb(state):
    time.sleep(4)
    if state == True:
        powerBomb.BombOn()
        screen.FillMessage(0, 60, "Bomba de agua activa")
        #print("Bomba de agua activa")
    else:
        powerBomb.BombOff()
        screen.FillMessage(0, 60, "Bomba Apagada")
        #print("Bomba Apagada")

#Ejecucion proceso de sensor de humedad de tierra
def proccessFC():
    time.sleep(4)
    stateSensor = sensorFT.map()
    
    if (stateSensor < 40):
        ledHumidity.ledOn()
    else:
        ledHumidity.ledOff()
        
    messageFC = "{}% Humedad de suelo".format(stateSensor)
    screen.FillMessage(0, 20, messageFC)
    
    if (valueFC != stateSensor):
        valueFC = stateSensor
        fireDB.SendFC(stateSensor)
    
    return stateSensor

#Ejecucion proceso de fotocelda
def proccessLDR():
    time.sleep(4)
    stateSensor = sensorLDR.map() 
    messageLDR = "{}% nivel de luz".format(stateSensor)
    screen.FillMessage(0, 50, messageLDR)
    
    if (valueLDR != stateSensor):
        valueLDR = stateSensor
        fireDB.SendLDR(stateSensor)

    return stateSensor


#Inicio del sistema
if __name__ == '__main__':
    main()