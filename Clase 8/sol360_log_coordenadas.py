# combinacion de dos APIs para tomar info: de una API tomo las coordenadas de una cierta ciudad, y con esas coordenadas tomo el clima de la otra API

import requests
import json
from pprint import pprint
import csv

archivo = open('C:/Users\MARTIN\OneDrive\Escritorio\CURSO EANT PYTHON\Data Analytics\Clase 8\sucursales_sol_360.csv')
claves = open('C:/Users\MARTIN\OneDrive\Escritorio\CURSO EANT PYTHON\Data Analytics\Clase 8\claves.txt')
lista_claves = [clave.strip('\n') for clave in claves]
key_open_weather = lista_claves[0]
key_open_cage =  lista_claves[1]
log = open('log_errores.txt','w')   #para el log de errores
archivo_csv = csv.reader(archivo, delimiter=';')
ciudades = [linea[0] for linea in archivo_csv]

for ciudad in ciudades:
    ciudad_cod = requests.utils.quote(ciudad)
    url = 'https://api.opencagedata.com/geocode/v1/json?q='+ ciudad_cod + ',Argentina&key=' + key_open_cage
    objeto = json.loads(requests.get(url).text)
    latitud = objeto["results"][0]['geometry']['lat']
    longitud = objeto['results'][0]['geometry']['lng']
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(latitud) + '&lon=' + str(longitud) + '&units=metric&lang=es&appid=' + key_open_weather
    objeto = json.loads(requests.get(url).text)
    try:
        print('El clima en ' + ciudad + 'es: ' + objeto['weather'][0]['description'])
        print('La TEMPERATURA es de: ' + str(objeto['main']['temp']) + ' °C')
        print('La HUMEDAD es de: ' + str(objeto['main']['humidity']) + ' %')
    except:
        log.write(ciudad + ' - No se encontró\n')
log.close()

