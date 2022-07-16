import network, time, urequests
import json

class NetworkConnection:
    
    url = "https://api.thingspeak.com/update?api_key=LCSJ5M98PSD7T1YT"
    
    def __init__(self, red, password):
        self.__red = red
        self.__password = password

    def conectaWifi(self):
        global miRed
        miRed = network.WLAN(network.STA_IF)     
        if not miRed.isconnected():              #Si no está conectado…
            miRed.active(True)                   #activa la interface
            miRed.connect(self.__red, self.__password)         #Intenta conectar con la red
            print('Conectando a la red', self.__red +"…")
            timeout = time.time ()
            while not miRed.isconnected():           #Mientras no se conecte..
                if (time.ticks_diff (time.time (), timeout) > 10):
                    return False
        self.successConnection()
        return True
    
    def successConnection(self):
        print("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

    def sendData(self, info):
        fields = '&field'
        address = ''
        cont = 1
        for data in info:
            address += fields + str(cont) + '=' + str(data)
            cont += 1
        print(address)
        #respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum))
        respuesta = urequests.get(self.__class__.url + address)
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close ()
        time.sleep(1)
    
    def desactive():
        miRed.active(False)


