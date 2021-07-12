# La idea ahora es insertar filas en la tabla pero mediante ingreso externo.

import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base018',
                                   user = 'pdp_usuario018',
                                   password = 'eantpass')

cursor = conexion.cursor()

# Si quisiera tomar un campo de alguna tabla de SQL

cursor.execute('SELECT dni FROM alumnos')
lista_dnis = [dni[0] for dni in cursor]

while True:
    respuesta = input('Desea ingresar un nuevo registro? (Y/N): ').upper()
    if respuesta == 'Y':
        dni = input('Ingrese DNI del alumno: ')
        if int(dni) in lista_dnis: print('Este DNI ya fue ingresado.')
        else:
            lista_dnis.append(int(dni))
            nombre = input('Ingrese nombre del alumno: ')
            apellido = input('Ingrese apellido del alumno: ')
            email = input('Ingrese email del alumno: ')
            fecha_nac = input('Ingrese fecha nacimiento (YYY-MM-DD): ')
    elif respuesta.upper() == 'N':
        break
    else:
        print('Ha ingresado un valor erroneo')
    
    query = 'INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES (%s,%s,%s,%s,%s)'
    cursor.execute(query, (nombre,apellido,dni,email,fecha_nac))







conexion.commit()
cursor.close()
conexion.close()


