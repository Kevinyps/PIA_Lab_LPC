#!/bin/bash
# Script superscan.sh Kevin Yair Pena Salazar 1827227
#
# Ejemplo de Menu en BASH
#
date
    echo "---------------------------"
    echo "   Menu Principal"
    echo "---------------------------"
    echo "1. Net Discover"
    echo "2. Portscanv1"
    echo "3. Welcome"
    echo "4. Exit"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) /home/dev/Desktop/netdiscover.sh;;
        2) /home/dev/Desktop/portscanv1.sh;;
        3) /home/dev/Desktop/welcome.sh;; 
        4) echo "Bye!"; exit 0;;
esac