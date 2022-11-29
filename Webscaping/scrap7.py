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
# Buscar todos los elementos que el class 'card-content'
job_elements = results.find_all('div', class_='card-content')
# Buscamos todps los elementos que el h2 contentga en su texto
# La palabra 'python'
python_jobs = results.find_all(
    'h2', string=lambda text: 'python' in text.lower()
)
# Mostramos la cantidad de elementos que cumplen con la busqueda
print(len(python_jobs))