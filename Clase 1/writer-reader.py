# UNA MEJOR FORMA DE DIVIDIR EL TEXTO ES UTILIZANDO LIBRERIA CSV Y METODO READER.
 

import csv 

    
archivo_in = open('peliculas.csv', encoding = 'utf-8')
archivo_out = open('peliculas_salida.csv', 'w', encoding = 'utf-8')
tabla = csv.reader(archivo_in)

for linea in tabla:
    unidos = ','.join([linea[2],linea[1],linea[0]])
    archivo_out.write(unidos + '\n')
    
archivo_in.close()
archivo_out.close()


# Otra forma de abrir los archivos

with open('peliculas.csv', encoding = 'utf-8') as archivo_in, open('peliculas_salida2.csv', 'w', newline = '', encoding = 'utf-8') as archivo_out:
    
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out, delimiter = ';')
    salida.writerow(['Director','Año','Pelicula'])
    
    for linea in entrada:
        salida.writerow([linea[2],linea[1],linea[0]])

