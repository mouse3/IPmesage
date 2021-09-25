import socket
def Publico():
        print("0.0.0.0:9797")
        ip = "0.0.0.0"
        puerto = 9797
        conexionesMaximas = input("conexiones maximas:")
        dataConection = (ip, puerto)
        conexionesMaximas = 5 #Podrán conectarse 5 clientes como máximo
        socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
        socketServidor.bind(dataConection) #Asignamos los valores del servidor
        socketServidor.listen(conexionesMaximas) #Asignamos el número máximo de conexiones
        print("Esperando conexiones en %s:%s" %(ip, puerto))
        cliente, direccion = socketServidor.accept()
        print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))
        while True:
            datos = cliente.recv(1024) #El número indica el número maximo de bytes
            if datos == "exit":
                cliente.send("exit")
                break
            print("RECIBIDO: %s" %datos)
            cliente.sendall("-- Recibido --")
            print("------- CONEXIÓN CERRADA ---------")
            socketServidor.close()
def Privado():
            print("0.0.0.0:9797")
            ip = input("direccion del servidor:")
            puerto = input("puerto del servidor:")
            conexionesMaximas = input("conexiones maximas:")
            dataConection = (ip, puerto)
            conexionesMaximas = 5 #Podrán conectarse 5 clientes como máximo
            socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
            socketServidor.bind(dataConection) #Asignamos los valores del servidor
            socketServidor.listen(conexionesMaximas) #Asignamos el número máximo de conexiones
            print("Esperando conexiones en %s:%s" %(ip, puerto))
            cliente, direccion = socketServidor.accept()
            print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))
            while True:
                datos = cliente.recv(1024) #El número indica el número maximo de bytes
                if datos == "exit":
                    cliente.send("exit")
                    break
                print("RECIBIDO: %s" %datos)
                cliente.sendall("-- Recibido --")
                print("------- CONEXIÓN CERRADA ---------")
                socketServidor.close()

option = input("-->>")
if option == "1":
    Privado()
if option == "2":
    Publico()
