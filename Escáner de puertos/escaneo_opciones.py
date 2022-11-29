#Kevin Yair Peña Salazar 1827227
import sys
from socket import *
import nmap
import platform 
import os
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()
def menu_principal():
    print(" En opcion 1 y 2 los parametros necesarios son la ip a analizar <host> 192.164.1.85 \n Para la opcion 4 se debe ingresar <host> 192.164.1. <cnt puertos> 2   ")
    opciones = {
        '1': ('Escaneo UDP ', accion1),
        '2': ('Escaneo completo ', accion2),
        '3': ('Detección de sistema operativo', accion3),
        '4': ('Escaneo de red con ping ', accion4),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')
def accion1():
    host = sys.argv[1]           
    s = socket(AF_INET, SOCK_DGRAM)

    for port in range(0,255):
        try:
            data = "Hola"
            #print "Try "+str(port)
            s.sendto(data,(host,port))
            s.settimeout(1)
            print ((s.recvfrom(65507)))
        
            break
        except:
            pass
    if data != "hola" :
        print("No existen puertos UDP en esa ip")

def accion2():
    scaner = nmap.PortScanner()
    host = sys.argv[1]
    print(scaner.scan(host, '1-254'))

def accion3():
    print(platform.system())

def accion4():
    up_ip =[] #Lista las Ips que estan respondiendo a PING
    host = sys.argv[1]
    rang = sys.argv[2]
    for x in range(int(rang)):  #Rango Seleccionado por el usuario
        server_ip = host + str(x)
        print("Probando IP... \n")
        rep = os.system('ping -c 1 ' + server_ip)
        if rep == 0:
            up_ip.append(server_ip)
            print('******************* IP detectada como Up **************** \n')
        else:
            print('IP no responde \n')
    print(up_ip) 

def salir():
    print('Adios')

if __name__ == '__main__':
    menu_principal()