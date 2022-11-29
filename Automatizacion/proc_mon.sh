#!/bin/bash
#
# Script par listar procesos ejecutandos
# en el servidor
#
## Variables 
TIME=`date +%d-%m-%Y_%H:%M:%S`
FECHA=`date +%d-%m-%Y`
## Creando directorio de Log 
#
if [ ! -d "$HOME/log" ]
then
        mkdir $HOME/log
fi
#
## Listando Procesos
#
echo "#" >> $HOME/log/procesos_${FECHA}.log
echo "###############################" >> $HOME/log/procesos_${FECHA}.log
echo "#" >> $HOME/log/procesos_${FECHA}.log
echo "Hora:"$TIME >> $HOME/log/procesos_${FECHA}.log
ps -ef >> $HOME/log/procesos_${FECHA}.log
echo "TOTAL DE PROCESOS: "`ps -ef` >> $HOME/log/procesos_${FECHA}.log
echo "Hora:"$TIME >> $HOME/log/procesos_${FECHA}.log