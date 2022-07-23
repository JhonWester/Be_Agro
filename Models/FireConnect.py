import Modules.ufirebase as firebase
import ujson

class FirebaseConnect:
    
    with open("./Shared/config.json") as config_file:
        data = ujson.load(config_file)
        
    url = data["urlFirebase"]
    pathDht = '/Sensors/Environment'
    pathFC =  '/Sensors/Humidity'
    pathLDR = '/Sensors/Light'
    pathIndex = '/Indices/'
    pathBomb = '/Bomb'
    
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
    
    #Send to cloud Index List
    def SendIndexSensor(self, list, path):
        firebase.put(self.__class__.pathIndex + path, list, bg = 0)
        
    #Send to cloud Active Bomb
    def SendDataBomb(self, data):
        firebase.put(self.__class__.pathBomb, data, bg = 0)