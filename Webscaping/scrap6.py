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
#Por cada elemento encontrado job_elements imprimimos 
for job_element in job_elements:
    title_element = job_element.find('h2',class_='title')
    company_element = job_element.find('h3',class_='company')
    location_element = job_element.find('p',class_='location')
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()