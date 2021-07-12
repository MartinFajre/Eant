from datetime import datetime

#Fecha de salida la quiero con el formato "DD-MM-AAAA"

fecha = '13/02/2019'
objeto_fecha = datetime.strptime(fecha, '%d/%m/%Y')
fecha_normalizada = datetime.strftime(objeto_fecha, '%d-%m-%Y')
print(fecha, objeto_fecha, fecha_normalizada)


fecha2 = '02/13/2019'
objeto_fecha2 = datetime.strptime(fecha2, '%m/%d/%Y')
fecha_normalizada2 = datetime.strftime(objeto_fecha2, '%d-%m-%Y')
print(fecha2, objeto_fecha2, fecha_normalizada2)


