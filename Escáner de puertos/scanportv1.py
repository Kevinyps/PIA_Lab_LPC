import socket
import os
import sys
up_ip =[] #Lista las Ips que estan respondiendo a PING
host = sys.argv[1]
rang = sys.argv[2]
for x in range(int(rang)):  #Rango de 0-254
    server_ip = host + str(x)
    print("Probando IP... \n")
    rep = os.system('ping -c 1 ' + server_ip)
    if rep == 0:
        up_ip.append(server_ip)
        print('******************* IP detectada como Up **************** \n')
    else:
        print('IP no responde \n')
print(up_ip)