#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Ejemplo cliente - servidor en python
# Programa Servidor
# www.elfreneticoinformatico.com


#Importacines:
import socket #utilidades de red y conexion

#Definimos parámetros necesarios por defeccto
#temporal
print("0.0.0.0:9797")
ip = input("direccion del servidor:")
purto = input("puerto del servidor:")
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