import Package.controller as Control

def main():
    
    try:
        Control.initBeAgro()
    except:
        Control.messageLed(0, 16, "Ocurrio un problema!!!")
        Control.proccessError()



#Inicio del sistema
if __name__ == '__main__':
    main()