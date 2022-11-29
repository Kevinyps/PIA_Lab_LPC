# Importar modulos
#Kevin Yair Peña Salazar 
#1827227
import requests
# Obtener la informacion HTML de la URL
URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
# Imprimir el texto de la peticion GET
print(page.text)