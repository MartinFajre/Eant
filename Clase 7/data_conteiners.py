from pprint import pprint
import json

#VARIABLE
x = 0

#LISTA
lista = []

#TUPLA
tupla = ()

#DICCIONARIO
diccionario = {}

#################

edad = 5
le_gusta = ['comer', 'correr','ladrar']
perro = {'nombre':'Rocco',
         'tipo':'perro',
         'raza':'labrador'
         }

#Combinación
perro.update({'edad' : edad})
perro.update({'le_gusta' : le_gusta})


# para que lo imprima con estructura legible, uso libreria pprint
pprint.pprint(perro)

# Nuevo objeto amo

amo = {'nombre' : 'Roberto',
       'tipo' : 'humano',
       'le_gusta' : ['Una buena conversacion', 'los animales', 'jugar futbol'],
       'edad': 45,
       'mascota' : perro 
       }

gato = {'nombre':'Coco',
         'tipo':'gato',
         'color':'blanco'
         }

loro = {'nombre':'Pepe',
         'tipo':'loro',
         'color':'verde'
         }

mascotas = {'perro':perro, 
            'gato':gato,
            'loro':loro
            }

amo.update({'mascota': mascotas}) 

objeto = {'amo':amo}
with open('amo.json', 'w', encoding = 'utf-8') as archivo_json:
    json.dump(objeto, archivo_json, indent = 3)           

