import requests

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)
contenido = respuesta.text

# Tomo el archivo de la red y reescribo su contenido en un csv

with open('pelis.csv', 'w') as pelis:
    pelis.write(contenido)
    
    