
# Si el archivo está en el mismo directorio del archivo py, entonces no hace falta la ruta

# con el newline logro quitar el espaciado entre linea y linea
archivo = open('frutas.txt', 'r', encoding = 'utf-8', newline = '\r')

# otra forma de quitar el espaciado entre lineas
archivo = open('frutas.txt', 'r', encoding = 'utf-8')

for linea in archivo:
    linea = linea[:-1]
    print(linea)
    
# otra forma de quitar el espaciado entre lineas usando strip()  
for linea in archivo:
    linea = linea.strip('\n')
    print(linea)
    
# otra forma de quitar el espaciado entre lineas usando replace() 
for linea in archivo:
    linea = linea.replace('\n','')
    print(linea)    