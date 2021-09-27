import socket
#hola que tal estas?
ip = "0.0.0.0"
puerto = 9797
d = (ip, puerto)
conexionesMaximas = 5 
#Creamos el servidor.
#socket.AF_INET para indicar que utilizaremos Ipv4
#socket.SOCK_STREAM para utilizar TCP/IP (no udp)
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor.bind(d) #Asignamos los valores del servidor
servidor.listen(conexionesMaximas) 

print("Esperando conexiones en %s:%s" %(ip, puerto))
cliente, direccion = servidor.accept()
print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))

def ramKill():
    print("iniciando Ramkill...")
    estructura = []
    contador = 0
    while True:
        estructura.append("Insertado %s" %contador)
        cliente.send("Insertado %s\n" %contador)
        contador += 1
    return 

while True:
    datos = cliente.recv(1024)
    if datos == "exit":
        cliente.send("exit")
        break
    if datos == "running":
        print("Recibido: %s" %datos)
        cliente.sendall("me too")
        continue
    if datos == "ramKiller":
        print("Recibido: %s" %datos)
        print("Iniciando ramKiller")
        cliente.send("RAMKILLER01")
        print("Esperando mensaje de inicio")
        datos = cliente.recv(1024)
        if datos == "start":
            ramKill()
        else:
            print("ramKiller cancelado por el cliente")
            continue
    print("RECIBIDO: %s" %datos)
    cliente.sendall("-- Recibido --")

print("------- CONEXIÓN CERRADA ---------")
servidor.close()
