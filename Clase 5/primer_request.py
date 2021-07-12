

import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'
respuesta = requests.get(url)

# Codigo de respuesta (status_code) debe ser 200.

print('Código de respuesta:', respuesta.status_code)
print('URL de origen:', respuesta.url)
print('Contenido:', respuesta.content)
print('Contenido como texto:', respuesta.text)
print('Codificación:', respuesta.encoding)

respuesta.encoding = 'utf-8'

