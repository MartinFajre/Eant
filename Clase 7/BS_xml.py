# XML
from bs4 import BeautifulSoup as BS

archivo = open('books.xml', encoding ='utf-8')

xml = BS(archivo, features = 'lxml')

print(xml.prettify())

fechas = xml.find_all('publishdate')
precios = xml.find_all('price')

for fecha in fechas:
    print('Fecha de publicacion: ', fecha.text)
    
# si quiero recorrer ambos elementos con un solo for, como tienen mismo largo:
    
for i in range(len(fechas)):
    print('Fecha de publicacion: ', fechas[i].text)
    print('Precios: ', precios[i].text)


