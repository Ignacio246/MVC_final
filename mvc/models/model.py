import mysql.connector

class Alumnos():

    " METODO PARA CONECTAR "
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='figiefgmi0ira4d3', 
                password='sb7dkrboc0apu3ua',
                host='thh2lzgakldp794r.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='lwlq4ui1z45n2fln'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    " METODO PARA SELECCIONAR "
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "apellido_paterno":row[3],
                    "apellido_materno":row[4],
                    "edad":row[5],
                    "fecha_nacimiento":row[6],
                    "sexo":row[7],
                    "estado_civil":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    " METODO DE BUSQUEDA/VIEW "
    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "apellido_paterno":row[3],
                    "apellido_materno":row[4],
                    "edad":row[5],
                    "fecha_nacimiento":row[6],
                    "sexo":row[7],
                    "estado_civil":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)

    " METODO DE INSERT "
    def insert(self, matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil):
        try:
            self.connect()
            query = ("INSERT INTO alumnos (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil) values (%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    " METODO DE ACTUALIZAR "
    def update(self, matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil):
        try:
            self.connect()
            query = ("UPDATE alumnos SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, edad=%s, fecha_nacimiento=%s, sexo=%s, estado_civil=%s WHERE matricula=%s;")
            values = (nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil, matricula)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    " METODO DE ELIMINAR "
    def delete(self, matricula):
        try:
            self.connect()
            query = ("DELETE  FROM alumnos WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False


object = Alumnos()
object.connect()
#object.insert("1718110989","Ignacio","Candia","Ibarra",21,"1998/12/06","Masculino","Soltero")
#object.update('1718110394', 'Alexa', 'Marquez', 'Jardinez', '19', '1997/07/16', 'Femenino', 'Soltera')

for row in object.select():
    print(row)