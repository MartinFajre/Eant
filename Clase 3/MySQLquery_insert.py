import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base018',
                                   user = 'pdp_usuario018',
                                   password = 'eantpass')

cursor = conexion.cursor()

#Dentro del execute se pone el Query que se quiera realizar


query = '''INSERT INTO alumnos (nombre, apellido, email, dni, fecha_nac)
           VALUES ('Angel', 'Nadie','angel@nadie.com','34345035','1915-02-10') '''

cursor.execute(query)
conexion.commit()       #Para que se graben los cambios al insertar o eliminar campos

nombre = 'Martha'
apellido = 'Gutierrez'
dni = '14315226'
email = 'mirtha@nada.com'
fecha_nac = '1980-12-3'

query = "INSERT INTO alumnos (nombre, apellido, email, dni, fecha_nac) VALUES (%s, %s,%s,%s,%s)"

cursor.execute(query, (nombre, apellido, email, dni, fecha_nac))
conexion.commit()

cursor.close()
conexion.close()
