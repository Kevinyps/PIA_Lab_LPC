from ftplib import FTP
ftp = FTP('<ip servidor>')  #colocas la ip del servidor ftp
ftp.login(user='<user>', passwd='<pswd>')     

ftp.cwd('upload')               # carpeta destino
with open('ADVERTENCIA.txt', "rb") as file: #Archivo a s
    # use FTP's STOR  para subir archivo
    ftp.storbinary(f'STOR ADVERTENCIA.txt', file)
ftp.quit() #Cierre de sesion 