import Package.ufirebase as firebase
import ujson

class FirebaseConnect:
    
    url = 'https://agro-app-2aa55-default-rtdb.firebaseio.com/'
    path = '/Sensores/dht11'
    
    def __init__(self) -> None:
        firebase.setURL(self.__class__.url)
    
    def sendDHT(self, hum, temp):
        
        message = ujson.dumps({
            "Humedad": hum,
            "Temperatura": temp,
            })
        print(message)
        
         
        firebase.put("Estacion/sensorDHT", message, bg = 0 )
        print("Enviado...", message)