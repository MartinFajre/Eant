# La idea es normalizar todas las fechas del archivo, con los distintos formatos, al formato final dd/mm/yyyy

from datetime import datetime
import csv

# Funcion para transformar el formato de fecha que viene en español

def traduceFecha(fecha):
    meses =  ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO',  'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    lista = fecha.split(' de ')
    mes2 = lista[1].upper()
    numero_mes = meses.index(mes2) + 1
    return lista[0] +'-'+ str(numero_mes) +'-'+ lista[2]

# Genera un nuevo archivo reclamos_salida con mismos campos y la fecha normalizada, y genera una lista con las fechas normalizadas (lista_fecha)

with open('reclamos.csv', encoding = 'ANSI') as archivo_in, open('reclamos_salida.csv', 'w', encoding = 'ANSI', newline = '') as archivo_out:
    
    entrada = csv.reader(archivo_in, delimiter = ';')
    
    tipos_fechas = ['%d/%m/%y','%d/%m/%Y','%Y-%d-%m','%d-%m-%Y']    
    formato_elegido = '%d/%m/%Y'
    i = 0
    lista_fechas = []
    for linea in entrada:
        if i > 0:
            print(linea[3])
            try:
                objeto_fecha = datetime.strptime(linea[3], tipos_fechas[0])
                fecha_norm = datetime.strftime(objeto_fecha, formato_elegido)
                linea[3]=fecha_norm
            except:
                try:
                    objeto_fecha = datetime.strptime(linea[3], tipos_fechas[1])
                    fecha_norm = datetime.strftime(objeto_fecha, formato_elegido)
                    linea[3]=fecha_norm
                except:
                    try:
                        objeto_fecha = datetime.strptime(linea[3], tipos_fechas[2])
                        fecha_norm = datetime.strftime(objeto_fecha, formato_elegido)
                        linea[3]=fecha_norm
                    except:
                        try:
                            objeto_fecha = datetime.strptime(linea[3], tipos_fechas[3])
                            fecha_norm = datetime.strftime(objeto_fecha, formato_elegido)
                            linea[3]=fecha_norm
                        except:
                            objeto_fecha = datetime.strptime(traduceFecha(linea[3]),'%d-%m-%Y')
                            fecha_norm = datetime.strftime(objeto_fecha,formato_elegido)
                            linea[3]=fecha_norm                    
            lista_fechas.append(linea[3])
        i += 1
        salida = csv.writer(archivo_out, delimiter = ';')
        salida.writerow([linea[0]+' - '+linea[1]+' - '+linea[2]+' - '+linea[3]])
