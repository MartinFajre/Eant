import requests
import json
from pprint import pprint

# Abro el archivo donde tengo el key para no pasarlo

claves = open('C:/Users\MARTIN\OneDrive\Escritorio\CURSO EANT PYTHON\Data Analytics\Clase 8\claves.txt')

lista_claves = [clave.strip('\n') for clave in claves]
key = lista_claves[0]

ciudad = 'San Juan, Argentina'

#Codifico espacios y comas para que la API lo interprete bien
ciudad_cod = requests.utils.quote(ciudad)

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad_cod + '&appid=' + key

objeto = json.loads(requests.get(url).text)

pprint(objeto)

# Quiero la descripcion, en castellano, y la temp en °C

url2 = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad_cod + '&units=metric&lang=es&appid=' + key

objeto2 = json.loads(requests.get(url2).text)
pprint(objeto2)

ciudades = open('C:/Users\MARTIN\OneDrive\Escritorio\CURSO EANT PYTHON\Data Analytics\Clase 8\sucursales_sol_360.csv')
ciudades

lista_ciudades = [ciudad.strip('\n') for ciudad in ciudades]
for i in range(len(lista_ciudades)):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + requests.utils.quote(lista_ciudades[i]) + '&units=metric&lang=es&appid=' + key 
    lista_desc = json.loads(requests.get(url).text)['weather'][0]['description']
    