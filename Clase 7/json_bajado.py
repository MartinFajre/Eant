import json
from pprint import pprint
import requests
from io import StringIO
import csv

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'

contenido = requests.get(url).text

objeto = json.load(contenido) # esto no funciona ya que lo toma como string

objeto = json.loads(contenido) # de esta forma sí soluciona

# otra forma es usar el stringIO (variante)

objeto = json.load(StringIO(contenido))

pprint(objeto)
elementos = objeto['features'][0]['properties']

with open('hospitales_json.csv', 'w', encoding = 'utf-8') as archivo:
    salida = csv.writer(archivo, delimiter = ';')
    
    for elemento in elementos:
        nombre = elemento['¨NOMBRE']
        direccion = elemento['CALLE'] +' ' + elemento['ALTURA'] 
        telefono = elemento['TELEFONO']
        especialidad = elemento['TIPO_ESPEC']
        pag = elemento['WEB']
        archivo.writerow(nombre, direccion, telefono, especialidad, pag)
        
## REVISAR PORQUE NO ME SALE EL ULTIMO BLOQUE FOR
        