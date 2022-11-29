#Kevin Yair Peña Salazar 1827227
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.encoders import encode_base64
print("**** Envio con Gmail ****")
user = input('Cuenta Gmail: ')
pswd = getpass.getpass('Contraseña')
#Para las cabeceras del email
remitente = input('Remitente: ')
destinatario = input('Para: ')
asunto = input('Asunto: ')
mensaje = input('Mensaje :')
archivo = input('Adjuntar archivo: ')
#Host y puerto smtp
conn = smtplib.SMTP('smtp.gmail.com', 587)
#Protocolo de cifrado
conn.starttls()
#Credenciales
conn.login(user, pswd)
header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario
mensaje = MIMEText(mensaje, 'html')
header.attach(mensaje)
if(os.path.isfile(archivo)):
adjunto = MIMEBase('aplication','octet-stream')
adjunto.set_payload(open(archivo,'rb').read())
encode_base64(adjunto)
adjunto.add_header('Content-Disposition','attachment; filename= "%s" ' %
os.path.basename(archivo))
header.attach(adjunto)
#Enviar Gmail
conn.sendmail(remitente,destinatario,header.as_string())
if conn.sendmail(remitente,destinatario,header.as_string()) == {}:
print('Envio exitoso')
#Cierre de conexion
conn.quit()