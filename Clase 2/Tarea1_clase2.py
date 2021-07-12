# LATITUD, LONGITUD, DIRECCION, NOMBRE
# tomar del archivo estos campos y generar un nuevo csv
import csv

with open('hospitales.csv', encoding = 'utf-8', newline = '') as archivo_input, open('hospitales_salida.csv' , 'w', encoding = 'utf-8') as archivo_out:
    

    entrada = csv.reader(archivo_input, delimiter = ',')
  
      
    
    i = 0
    
    for linea in entrada:
        linea = linea[0].strip('"')
        if i<1:
            lista = linea.split(';')
            lista[5] = 'DIRECCION'
            archivo_out.write(lista[0] +' / ' + lista[5] +' / ' + lista[2] + '\n')
        else:    
            lista = linea.split(',')
            lista[5] = ' '.join([lista[5],lista[6]])
            archivo_out.write(lista[0] +' / ' + lista[5] + ' / ' + lista[2] + '\n')
        i += 1

