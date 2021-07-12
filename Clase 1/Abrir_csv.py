archivo = open('subtes.csv', encoding = 'utf-8')

for linea in archivo:
    linea = linea.strip('\n')
    print(linea)
    
# Que hago si quisiera imprimir solo el precio? debere guardar info en una lista
    
for linea in archivo:
    linea = linea.strip('\n')
    lista = linea.split(',')
    print(lista[2])
    
