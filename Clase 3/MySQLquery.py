import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base018',
                                   user = 'pdp_usuario018',
                                   password = 'eantpass')

cursor = conexion.cursor()

#Dentro del execute se pone el Query que se quiera realizar


query = "SELECT * FROM alumnos"
cursor.execute(query)

for alumno in cursor:
    print(alumno[3])

cursor.close()
conexion.close()
