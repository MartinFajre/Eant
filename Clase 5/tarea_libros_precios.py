# Tarea clase5: armar tabla MYSQL con los top 100 mas vendidos, titulo y precio
from bs4 import BeautifulSoup as BS
import requests
import mysql.connector

url = 'https://www.cuspide.com/cienmasvendidos'

respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html, features = 'html.parser')
print(dom.text)
titulos = dom.find('article')

url2= titulos.a.get('href')

url_precio = 'https://www.cuspide.com/' + url2

respuesta2 = requests.get(url_precio)
respuesta2.econding = 'utf-8'
html2 = respuesta2.text
dom2 = BS(html2, features = 'html.parser')

print(dom2.section)

precio = dom2.find(class_='md-compra').div.div.div.div.text
