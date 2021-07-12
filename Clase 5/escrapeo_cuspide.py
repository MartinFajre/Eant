from bs4 import BeautifulSoup as BS

import requests

url = 'https://www.cuspide.com/cienmasvendidos'

respuesta = requests.get(url)
respuesta.enconding = 'utf-8'
html = respuesta.text

dom = BS(html, features = 'html.parser')

articulos = dom.find_all('article')

for articulo in articulos:
    print(articulo.figure.div.a['title'])

print('Solo el TOP 100:')
for i in range(len(articulos)):
    print(i+1, articulos[i].figure.div.a['title'])