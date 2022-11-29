# Importar modulos
#Kevin Yair Peña Salazar 
#1827227
import requests
import csv
from bs4 import BeautifulSoup
# Direccion de la pagina web 
url='http://quotes.toscrape.com'
# Ejecutar Get-Request
response = requests.get(url)
# Analizar sintacticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text,'html.parser')
# Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_='text')
authors_html = html.find_all('small', class_='author')
# Crear una lista de las citas 
quotes = list()
for quotes in quotes_html:
    quotes.append(quotes.text)
# Crear una lista de los autores
authors = list()
for author in authors_html:
    author.append(author.text)
# Para hacer el test: combinar y mostrar las entradas de ambas listas 
for t in zip(quotes,authors):
    print(t)
# Guardar las citas y los autores en un archivo CSV en el directorio actual
# Abrir el archivo con Excel / LibreOffice, etc.
with open('./citas_1827227.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes,authors))
