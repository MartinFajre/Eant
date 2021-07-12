import csv
from datetime import datetime

def normalizadorFecha(fecha, patron_in, patron_out = '%d-%m-%Y'):
    
    objeto_fecha = datetime.strptime(fecha, patron_in)
    fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
    print(fecha, objeto_fecha, fecha_normalizada)
    
fecha = '13/02/2019'

with open('formatos_fechas.txt', encoding = 'utf-8') as fechas:

    fechas_in = csv.reader(fechas, delimiter = '"')
    for linea in fechas:
        print(linea[0])

fecha1 = '13/2/2019'
fecha2 = '2/13/2019'
fecha3 = '02/19'
fecha4 = '20191302'
fecha5 = '2019-13-02 14:23:33'
fecha6 = '13/Feb/2019'
fecha7 = '13/February/2019'
fecha8 = '13 days after February 2019'
fecha9 = '13/Febrero/2019'

normalizadorFecha(fecha1,'%d/%m/%Y')
normalizadorFecha(fecha2,'%m/%d/%Y')
normalizadorFecha(fecha3,'%m/%y', '%m/%Y')
normalizadorFecha(fecha4,'%Y%d%m')
normalizadorFecha(fecha5,'%Y-%d-%m %H:%M:%S')
normalizadorFecha(fecha6,'%d/%b/%Y')
normalizadorFecha(fecha7,'%d/%B/%Y')
normalizadorFecha(fecha8,'%d days after %B %Y')

# Para la fecha9 debo primero transformar ya que "Febrero" esta en español

meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']

lista = fecha9.split('/')
mes=lista[1].upper()

nro_mes = meses.index(mes)+1

fecha_aux = lista[0] + str(nro_mes) + lista[2]

normalizadorFecha(fecha_aux, '%d%m%Y')





