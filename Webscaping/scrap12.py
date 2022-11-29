# Importar modulos
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
    'h2', string = lambda text: 'python' in text.lower()
    )
# Buscamos y mostramos informacion sobre los elemntos de python_jobs
# y almacenarlo en python_jobs_elements
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
] 
# Mostrar información de python_jobs_elements
# Kevin Yair Peña Salazar 
# 1827227
for job_element in job_elements:
    title_element = job_element.find('h2',class_='title')
    company_element = job_element.find('h3',class_='company')
    location_element = job_element.find('p',class_='location')
    # De la lista de elementos de la etiqueta 'a' buscamos 
    # el primer elemento que uncluya href
    link_url = job_element.find_all('a')[1]['href']
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    #Imprimimos la salida con el link_url
    print(f'Apply Here: {link_url} \n ')
    print()