##  Descripcion General
En este github vamos a ver diferentes ejercicios realizados durante el semestre y una breve descripcion de cada uno para que sean mas faciles de entender y utilizar

- [Manejo de APIs](https://github.com/Kevinyps/PIA_Lab_LPC/blob/main/Manejo%20de%20apis/Pokemon2.py)
- [Scripting en PowerShel](https://github.com/Kevinyps/PIA_Lab_LPC/blob/main/Scripting%20en%20Powershell/scan_alivev2.ps1 "Scripting en PowerShel")l
- [Scripting en Bash](https://github.com/Kevinyps/PIA_Lab_LPC/tree/main/Scripting%20en%20Bash "Scripting en Bash")
- [Encoding & Decoding](https://github.com/Kevinyps/PIA_Lab_LPC/tree/main/Encoding%20%26%20Decoding "Encoding & Decoding")
- [Webscraping](https://github.com/Kevinyps/PIA_Lab_LPC/tree/main/Webscaping "Webscraping")
- [Nmap](https://github.com/Kevinyps/PIA_Lab_LPC/blob/main/Nmap/automap.sh "Nmap")
- [FTP](https://github.com/Kevinyps/PIA_Lab_LPC/tree/main/FTP "FTP")
- [Escáner de Puertos](https://github.com/Kevinyps/PIA_Lab_LPC/tree/main/Esc%C3%A1ner%20de%20puertos "Escáner de Puertos")
- [Envió de Correos](https://github.com/Kevinyps/PIA_Lab_LPC/blob/main/Envio%20de%20correos/envio_correos.py "Envió de Correos")
- [Automatización de Tareas](https://github.com/Kevinyps/PIA_Lab_LPC/blob/main/Automatizacion/proc_mon.sh "Automatización de Tareas")

### Recursos

| Nombre | Descripcion |
|---|------|
|[Python](https://www.python.org/downloads/")  | Pagina oficial de descarga de python |
|[Postman](https://www.postman.com/downloads/ "Postman") | Postam se recomineda para ver el consumo de apis |
|[Powershell](https://learn.microsoft.com/es-es/powershell/scripting/overview?view=powershell-7.3 "powershell")  | Documentacion oficial de PowerShell |
|[Virtual-Box](https://download.virtualbox.org/virtualbox/7.0.4/VirtualBox-7.0.4-154605-Win.exe  "Virtual-Box")  | Link de descarga de virtual box |
|[ISO Debian 11](https://www.debian.org/distrib/netinst")  | Descargar ISO Debian11 |
|[Crear cuenta Gmail](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")  | En caso de no tener cuenta deberas crearte una|
|[Contraseña Gmail](https://myaccount.google.com/apppasswords")  | Aqui podras generar una contraseña que te va a servir cuando necesites mandar correos por medio de un script |




### Manejo de apis
---
En este script veremos el los principios del consumo de apis mediante un script en python, para el ejemplo usamos la api publica de pokemon y para hacegurarnos que el consumo se esta haciendo de manera correcta utilizamos [Postman](https://www.postman.com/downloads/ "Postman") para verificar lo que trae la api

[![pokemon-api.png](https://i.postimg.cc/Jh6HtNsH/pokemon-api.png)](https://postimg.cc/PLD5R8zd)

Como podemos ver postman nos permite ver ciertos pokemon reflejados en un json, te dejo el url del api para que lo pruebes por ti mismo : https://pokeapi.co/api/v2/pokemon-form/

<br>
### Scripting en PowerShel
---
Este script se utiliza para validar hosts activos en nuestra subred mediante diferentes comandos de [powershell](https://learn.microsoft.com/es-es/powershell/scripting/overview?view=powershell-7.3 "powershell") .

En caso de que queiras cambiar el color de cuando aparece el mensaje de host responde puedes hacerlo en la linea 6, en donde dice Green puedes poner el color que gustes por ejemplo Blue,Red, etc ...

```powershell
foreach( $r in $rango_ip){
    $actual = $rango + $r # se genera direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1 # Validamos conexion contra ip en $actual
    if ( $responde -eq "True"){
        Write-Output ""
        Write-Host "Host responde : " -NoNewLine; Write-Host $actual -ForegroundColor Green
    }
}
```
<br>
### Scripting en Bash
---
Aqui tendremos que concentrarnos en el script `portscanv1.sh` ya que este actuara como menú para utilizar los demas ejecutables de la carpeta, cabe aclarar que para poder ejecutar los scripts necesitaremos una terminal de linux para poder probarlo, te recomiendo utilizar una maquina virtual en mi caso utilice Virtual-Box[[link de descarga](https://download.virtualbox.org/virtualbox/7.0.4/VirtualBox-7.0.4-154605-Win.exe  "link de descarga")] pero tu puedes usar el que prefieras

Ya una vez entres en terminal y tengas los programas en linux deberas darle permiso de ejecucion al script con el comando  
<br>`chmod +x automap.sh` <br>
Una vez hecho esto solo queda correr el ejecutable, puedes hacerlo de varias forams, yo recomiendo estas dos
<br>`$ ./automap.sh` <br>
`$ bash automap.sh` <br>
Si seguiste los pasos al correrlo se vera algo parecido a lo de la imagen: <br>
[![superscan.png](https://i.postimg.cc/dty2XxLH/superscan.png)](https://postimg.cc/4mXHHwvV)
<br>
### Encoding & Decoding
---
En este script  de `encode_imageur.py`  podemos ver una manera de ecnriptar ya sea texto o incluso podríamos encriptar una imagen, para poder cambiar la imagen dentro del codigo hay que prestar atencion a este bloque de codigo, en la linea de url  y cambiar la url de la imagen

```python
if __name__ == '__main__':
    url="https://i.imgur.com/FdvXsgM.jpeg"
    
    Response: Response = requests.get(url, stream=True)
    with open('Kyrby.jpeg','wb') as file_down:
        for chunk in Response.iter_content(): #Descargando contenido poco a poco
            file_down.write(chunk)
    Response.close()
```
Para desencriptar la imagen podemos usar `decoding_uanl.py` ingresas la url que te arroja en el programa anterior y te la regresara desencriptada,en caso que quieras saber una frase encriptada en base 64  puedes utilizar `encode_text.py`  que te pide una frase y te la regresara en base64
<br>
### Webscraping
---
Si lo que buscas es hacer webscapping  aqui esta tu opcion ya que se cuentan con mas de 9 ejemplos de webscaping solo tendras que poner la url a la que quieres realizar este 'ataque', las posibilidades son infinitas pero en este ejemplo nos limitamos a mostrar texto de la pagina web como se puede ver en el ejemplo donde se le hizo webscrapping al sitio [https://realpython.github.io/fake-jobs/](https://realpython.github.io/fake-jobs/ "https://realpython.github.io/fake-jobs/")
<center>
[![powershell-scrap.png](https://i.postimg.cc/ZK42RxGQ/powershell-scrap.png)](https://postimg.cc/NLCpCmf8)
</center>
<br>
### Nmap
---
Para este script necesitamos tener una terminal de linux, como vimos anteriormente podemos utilizar [Virtual-Box](https://download.virtualbox.org/virtualbox/7.0.4/VirtualBox-7.0.4-154605-Win.exe  "Virtual-Box") pero lo dejo a tu preferencia ya en la terminal tendras que importar el `automap.sh` en ese codigo veras un menú en el cual vendras diferentes tipos de escanneo con nmap 

[![bash-nmap.png](https://i.postimg.cc/C10W0kkC/bash-nmap.png)](https://postimg.cc/KK99rK94)

Despues de seleccionar una opción se guardara en un archivo 
`resultados(opcion seleccionada).txt`  una vez que termine la ejecucion tendremos que ver el contenido del archivo donde guarda los resultados dependiendo de la opción como se puede ver en el ejemplo.
<br>
### FTP
---
Para utilizar este apartado primero deberas tener un servidor ftp activo (en mi caso yo tenia uno con linux) y saber la ip donde tienes el servidor ftp activo

[![ftpserver.png](https://i.postimg.cc/QtBp3R4G/ftpserver.png)](https://postimg.cc/TL6yjHvC)

Una vez hecho eso entras al archivo `FTP.py`

```python
from ftplib import FTP
ftp = FTP('<ip servidor>')  #colocas la ip del servidor ftp
ftp.login(user='<user>', passwd='<pswd>')     

ftp.cwd('upload')               # carpeta destino
with open('ADVERTENCIA.txt', "rb") as file: #Archivo a s
    # use FTP's STOR command to upload the file
    ftp.storbinary(f'STOR ADVERTENCIA.txt', file)
ftp.quit() #Cierre de sesion 
```
<br>
### Escáner de Puertos
---
Para el escaneo de puertos tambien se utilizara una terminal linux ya que el archivo es .sh en esta parte se hacen diferentes tipos de escaneos y tambien te puede decir los usuarios conectados, a diferencia de el apartado de NMAP este te lo muestra directo, ejecutas una opcion y te muestra el resultado de inmediato, aqui podemos ver un ejemplo de su ejecucion 

[![superscan.png](https://i.postimg.cc/bvVCmvhP/superscan.png)](https://postimg.cc/p98JTRrc)

### Envió de Correos
---
Para usar este script se necesitan 2 cosas :
- [Cuenta en Gmail](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp "Cuenta en Gmail")
- [Contraseña Especial](https://myaccount.google.com/apppasswords")

Una vez que se tenga esto se puede correr el script
`envio_correos.py` que enviara un correo y en caso de querer poner un adjunto deveras poner la ruta del archivo, por ejemplo:
` C:\Users\<tu usuario>\Desktop\adjunto.png` 

<br>
### Automatización de Tareas
---
La automatizacion de tareas se hará desde bash, desde este   [Pdf](https://drive.google.com/file/d/14W1df1VXLUC_VI5LM3jkq3SEkoY2EQSE/view?usp=share_link "giua") en el cual vendra como tendras que utilizar mas a detalle el script de `proc_mon.sh` este es solo un ejemplo de como automatizar tareas en linux claro que al ya saber este metodo podras hacerlo a tu manera 	😄
