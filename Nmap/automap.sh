#!/bin/bash
# Script superscan.sh Kevin Yair Pena Salazar 1827227
#
# Ejemplo de Menu en BASH
#
date
    echo "---------------------------"
    echo "   Menu Principal"
    echo "---------------------------"
    echo "1. Escaneo de red "
    echo "2. Escaneo Individual"
    echo "3. Escaneo de udp"
    echo "4. Escaneo de script"
    echo "5. Exit"
#read -p "Ingresar una ip " ip
read -p "Opción  [ 1 - 5 ] " c
case $c in
        1) read -p "Ingresar una ip: " ip
           nmap $ip > resultados1.txt;;
        2) read -p "Ingresar una ip: " ip
           nmap -A $ip > resultados2.txt;;
        3) read -p "Ingresar una ip: " ip
           nmap -n -Pn -sU -v $ip > resultados3.txt;;
        4) read -p "Ingresar una ip: " ip
           read -p "Ingresar nombre del script: " script
           nmap --script=$script, -sV  $ip > resultados4.txt;;
        5) echo "Bye!"; exit 0;;
esac