import Package.controller as Control

def main():
    
    try:
        Control.initBeAgro()
    except Exception as e:
        print('Error durante la ejecucion '+ str(e))
        Control.messageLed("Ocurrio un problema!!!", 0, 16)
        Control.proccessError()



#Inicio del sistema
if __name__ == '__main__':
    main()