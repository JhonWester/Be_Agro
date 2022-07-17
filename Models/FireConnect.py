import Package.ufirebase as firebase
import ujson

class FirebaseConnect:
    
    url = 'https://agro-app-2aa55-default-rtdb.firebaseio.com/'
    pathDht = '/Sensors/Environment'
    pathFC =  '/Sensors/Humidity'
    pathLDR = '/Sensors/Light'
    
    def __init__(self) -> None:
        firebase.setURL(self.__class__.url)
    
    #Send to cloud DHT
    def sendDHT(self, hum, temp):
        
        message = ujson.dumps({
            "Humidity": hum,
            "Temperature": temp,
            })
        
        print(message)       
        firebase.put(self.__class__.pathDht, message, bg = 0 )
        
    #Send to cloud Humidity
    def SendFC(self, GroundMoisture):
        
        message = ujson.dumps({
            "GroundMoisture": GroundMoisture
            })
        
        print(message)
        firebase.put(self.__class__.pathFC, message, bg = 0 )
    
    #Send to cloud LDR
    def SendLDR(self, LightLevel):
        message = ujson.dumps({
            "LightLevel": LightLevel
            })
        firebase.put(self.__class__.pathLDR, message, bg = 0 )