# Controller.py
import time

# Models
from Models.SensorDht import SensorDHT
from Models.FireConnect import FirebaseConnect
from Models.PowerBomb import PowerBomb
from Models.SensorAnalogo import SensorAnalogo
from Models.Led import Led
from Models.Screen import Screen
import ujson

#Package
from Shared.NetworkConnect import NetworkConnection

with open("./Shared/config.json") as config_file:
    data = ujson.load(config_file)

red = data["wifiConnect"]

pines = data["pines"]

#Sensor de dht11
sensorDHT = SensorDHT(pines["dth"])

#Conexion Internet
connection = NetworkConnection(red['name'], red['pass'])

#Conexion Firebase
fireDB = FirebaseConnect()

#Bomba de agua
powerBomb = PowerBomb(pines["bomb"])

#Sensor de humedad tierra (pin, minimo, maximo)
sensorFT = SensorAnalogo(pines["ft"], 620, 1023)

#Sensor de luz (pin, minimo, maximo)
sensorLDR = SensorAnalogo(pines["ldr"], 65, 650)

#Pantalla oled (Pin scl, Pin sda)
screen = Screen(pines["screen"]["scl"], pines["screen"]["sda"])

#Salidas led
ledBomb = Led(pines["ledBomb"])
ledHumidity = Led(pines["ledHum"])

#Inicios de los procesos y recoleccion de datos de los dispositivos

#Record values send to cloud
valueDHT = [0, 0]
valueFC = 0
valueLDR = 0
contIndex = 0
ListFT = []
ListLDR = []


def initBeAgro():
    global contIndex
    #Init message oled
    screen.MessagesInitOled()
    
    if connection.conectaWifi():
        
        while True:
            
            environment = proccessDHT()
            
            groundMoisture = proccessFC()
            
            light = proccessLDR()
            
            proccessIndex(groundMoisture, light)
            
            if (light > 80 and groundMoisture < 50):
                proccessBomb(True)
            else:
                
                if (groundMoisture < 50 and environment > 33):
                    proccessBomb(True)
                else:
                    proccessBomb(False)

            screen.ShowMessage()
            contIndex += 1
            time.sleep(5)
                
    else:
        messageLed("Imposible conectar!!!", 0, 16)
        connection.desactive()



#Ejecucion proceso de sensor dht11
def proccessDHT():
    global valueDHT
    sensorDHT.getData()
    messageDHT = "T={:02.} ºC, H={:02d}%".format(sensorDHT.temperature, sensorDHT.humidity)
    screen.FillMessage(0, 0, messageDHT)
    
    if (valueDHT[0] != sensorDHT.humidity | valueDHT[1] != sensorDHT.temperature):
        valueDHT[0] = sensorDHT.humidity
        valueDHT[1] = sensorDHT.temperature
        fireDB.sendDHT(sensorDHT.humidity, sensorDHT.temperature)
    return sensorDHT.temperature
        

#Ejecucion proceso de bomba
def proccessBomb(state):
    if state == True:
        powerBomb.BombOn()
        ledBomb.ledOn()
        screen.FillMessage(0, 48, "Bomba Activa")
        print("Bomba de agua activa")
    else:
        powerBomb.BombOff()
        screen.FillMessage(0, 48, "Bomba Apagada")
        print("Bomba Apagada")

#Ejecucion proceso de sensor de humedad de tierra
def proccessFC():
    global valueFC
    stateSensor = sensorFT.map()
    
    if (stateSensor < 40):
        ledHumidity.ledOn()
    else:
        ledHumidity.ledOff()
        
    messageFC = "{}% Hum suelo".format(stateSensor)
    screen.FillMessage(0, 16, messageFC)
    
    if (valueFC != stateSensor):
        valueFC = stateSensor
        fireDB.SendFC(stateSensor)
    
    return stateSensor

#Ejecucion proceso de fotocelda
def proccessLDR():
    global valueLDR
    stateSensor = sensorLDR.map() 
    messageLDR = "{}% de luz".format(stateSensor)
    screen.FillMessage(0, 32, messageLDR)
    
    if (valueLDR != stateSensor):
        valueLDR = stateSensor
        fireDB.SendLDR(stateSensor)

    return stateSensor

def messageLed(message, colum, file):
    print(message)
    screen.FillMessage(colum , file, message)
    screen.ShowMessage()
    
def proccessError():
    connection.desactive()
    proccessBomb(False)
    
def proccessIndex(FT, LDR):
    global contIndex
    global ListFT
    global ListLDR
    
    if (contIndex == 0):
        ListFT = []
        ListLDR = []
        
    if (contIndex < 7):    
        ListLDR.append(LDR)
        ListFT.append(FT)
    
    if (contIndex == 6):
        fireDB.SendIndexSensor(ListLDR, 'Luz')
        fireDB.SendIndexSensor(ListFT, 'Humedad')
        contIndex = -1