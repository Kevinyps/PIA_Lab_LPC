# Importar modulos
# Kevin Yair Peña Salazar 
# 1827227
import requests
from bs4 import BeautifulSoup
# Obtener la informacion HTML de la URL
URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
# Analizamos el contenido HTML con BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='ResultsContainer')
# Formateamos la salida del objeto results de BeautifulSoup
print(results.prettify())