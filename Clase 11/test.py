# Utilizamos la libreria Flask
# El Flask tiene que estar corriendo para funcione la pag, sino queda "apagado"

pip install flask

from flask import Flask

app = Flask(__name__)   # Toma el nombre del archivo, que en este caso es test.py

@app.route('/')     # Así accedo a la pagina principal o raiz.
@app.route('/institucional/sobre-nosotros')     #Asi accedo a una ruta específica de ese dominio


@app.route('/')
def hello_flask():
    return '<h1>Hola Mundo</h1>'




# De esta forma habilito que cualquier dispositivo de mi intranet pueda acceder a mi maquina utilizando la IP que identifica mi maquina
app.run( port = 3030, host = '0.0.0.0' )    

 

app.run( port = 3030 )