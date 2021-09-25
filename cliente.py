#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Ejemplo cliente - servidor en python
# Programa Cliente
# www.elfreneticoinformatico.com

import socket #utilidades de red y conexion

#declaramos las variables
print("direccion del servidor publico--> 185.116.156.172")
print("puerto del servidor publico--> 32170")
ipServidor  = input("dirreccion del servidor:")
puertoServidor = input("puerto del servidor:")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ipServidor, puertoServidor))
print("Conectado con el servidor ---> %s:%s" %(ipServidor, puertoServidor))
while True:
    msg = input("> ")
    cliente.send(msg)
    respuesta = cliente.recv(4096)
    print(respuesta)
    if respuesta == "exit":
        break;

print("------- CONEXIÓN CERRADA ---------")
cliente.close()

