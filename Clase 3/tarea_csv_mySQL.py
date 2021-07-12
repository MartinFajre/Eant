# TAREA:  agarrar el csv, agarrar unos campos y armar una tabla en la base de datos. 
import csv
import mysql.connector


#Primero tomo el csv y armo las listas a partir de las cuales armare la tabla
with open('oferta_gastronomica.csv', encoding = 'utf-8') as archivo_in:
    
    entrada = csv.reader(archivo_in)
    next(entrada)    
    
    nombre = []
    direccion = []
    comuna = []
        
    for linea in entrada:
        nombre.append(linea[3])        
        direccion.append(linea[13])        
        comuna.append(linea[15])        
        
#Ahora paso a la parte del armado de tabla
        
conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                           database = 'pdp_base018',
                           user = 'pdp_usuario018',
                           password = 'eantpass')
cursor = conexion.cursor()

for i in range(len(nombre)):
    
    nombre_ = nombre[i]
    direccion_ = direccion[i]
    comuna_ = comuna[i]
    
    query = "INSERT INTO bares (nombre, direccion, comuna) VALUES (%s, %s,%s)"
    
    cursor.execute(query, (nombre_, direccion_, comuna_))
    conexion.commit()

# Usando cursor.executemany() te permite cargarle una lista/tupla, haciendo muchisimo mas rapido el llenado de la tabla. Lo correcto es cargarle una tupla.

cursor.close()
conexion.close()
