import json
from pprint import pprint

with open('amo.json', encoding = 'utf-8') as archivo:
    objeto = json.load(archivo)
    
pprint(objeto['amo']['mascota']['loro']['nombre'])

