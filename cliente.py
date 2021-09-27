import socket 

ipServidor = "127.0.0.1" 
puertoServidor = 9797
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ipServidor, puertoServidor))
print("Conectado con el servidor ---> %s:%s" %(ipServidor, puertoServidor))

def ramKill():
    while True:
        data = cliente.recv(1024)
        print(data)

while True:
    msg = input("> ")
    if len(msg) == 0:
        print("Secuencia vacía")
        continue
    if msg == "runEver":
        while True:
            cliente.send("running")
            respuesta = cliente.recv(4096)
            print(respuesta)
    cliente.send(msg)
    respuesta = cliente.recv(4096)
    if respuesta == "RAMKILLER01":
        print("Inicie secuencia")
        msg = input("> ")
        if  msg == "start":
            cliente.send(msg)
            ramKill()
        elif len(msg) == 0 or msg != "start":
            print("No se iniciará ramKiller")
            cliente.send("noStart")
        continue
    print(respuesta)
    if respuesta == "exit":
        break;

print("------- CONEXIÓN CERRADA ---------")
cliente.close()
