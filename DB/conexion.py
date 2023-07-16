import mysql.connector
from mysql.connector import Error
import validaciones.iniciarSesion as iniciarSesion

#DATA ACCESS OBJECT
class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                    host = 'localhost',
                    user = 'graciany',
                    password = 'Informatica2022',
                    database = 'prueba'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
            
    def ValidarSesion(self,nombre,contraseña):
        validacion = False
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT * FROM usuario WHERE nombre_usuario = %s AND passsword = %s"
                values = (nombre,contraseña )
                cursor.execute(query, values)
                resultados = cursor.fetchall()
                if resultados:
                    print("Acceso concedido")
                    validacion = True
                else:
                    print("Acceso denegado")
                    validacion = False
                cursor.close()
                return validacion
        
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    def entregarNombre(self,nombre_usuario, password):
        cursor = self.conexion.cursor()
        consulta_usuario = "SELECT id_usuario FROM usuario WHERE nombre_usuario = %s AND passsword = %s"
        parametros_usuario = (nombre_usuario, password)
        cursor.execute(consulta_usuario, parametros_usuario)
        resultado_usuario = cursor.fetchone()

        # Verificar si las credenciales son válidas
        if resultado_usuario:
            id_usuario = resultado_usuario[0]
            consulta_trabajador = "SELECT nombre FROM trabajador WHERE id_usuario = %s"
            parametros_trabajador = (id_usuario,)
            cursor.execute(consulta_trabajador, parametros_trabajador)
            resultado_trabajador = cursor.fetchone()

            if resultado_trabajador:
                nombre_trabajador = resultado_trabajador[0]
                print("Hola '", nombre_trabajador, "' bienvenido a tu portal!")
        
            else:
                print("No se encontró un trabajador asociado al usuario")
            
    def traerCargoUsuario(self,nombre_usuario, password):
        cursor = self.conexion.cursor()       
        consulta = """SELECT dl.cargo
                    FROM usuario u
                    JOIN trabajador t ON u.id_usuario = t.id_usuario
                    JOIN datos_laborales dl ON t.id_cargo = dl.id_cargo
                    WHERE u.nombre_usuario = %s AND u.passsword = %s"""

        parametros_usuario = (nombre_usuario, password)
        cursor.execute(consulta, parametros_usuario)

            
        resultado = cursor.fetchone()
            
        if resultado:
            nombre_cargo = resultado[0]
            str(nombre_cargo)
            return nombre_cargo
        else:
            print("No se encontró ningun cargo para el usuario y contraseña proporcionados.")

        # Cerrar la conexión a la base de datos
        cursor.close()
        
    def traerId(self,nombre_usuario,password):
        cursor = self.conexion.cursor()  
        consulta = "SELECT id_usuario FROM usuario WHERE nombre_usuario = %s AND passsword = %s"
        valores = (nombre_usuario, password)
        cursor.execute(consulta, valores)

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        if resultado:
            id_usuario = resultado[0]
            int(id_usuario)
            return id_usuario
        else:
            print("No se encontró ningún id_usuario con los valores proporcionados.")

        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()


#CLASE TRABAJADOR
class Trabajador(DAO):
    def __init__(self):
        super().__init__()

    def leerInformacion(self,id_usuario):
        cursor = self.conexion.cursor()  
        consulta = "select * from trabajador where id_usuario=%s;"
        valores = (id_usuario,)
        cursor.execute(consulta, valores)

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        return resultado
    
    def leerInformacionTrabajador(self, id_usuario):
        cursor = self.conexion.cursor()  
        consulta = "SELECT cargo, area, fecha_ingreso FROM datos_laborales where id_cargo = %s;"
        valores = (id_usuario,)
        cursor.execute(consulta, valores)

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        return resultado

    def leerCargaFamiliar(self, id_usuario):
        cursor = self.conexion.cursor()  
        consulta = "SELECT nombre_carga, parentesco, sexo FROM cargas_familiares where id_carga = %s;"
        valores = (id_usuario,)
        cursor.execute(consulta, valores)

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        return resultado
    
    def leerContactoEmergencia(self, id_usuario):
        cursor = self.conexion.cursor()  
        consulta = "SELECT nombre_contacto, relacion, telefono_contacto FROM contacto_emergencia where id_emergencia = %s;"
        valores = (id_usuario,)
        cursor.execute(consulta, valores)

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        return resultado
    
    def modDatPersonales(self, id_usuario, datos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE trabajador SET 
                        nombre = '{0}',
                        apellido_mat = '{1}',
                        apellido_pat = '{2}',
                        direccion = '{3}',
                        telefono ='{4}',
                        sexo = '{5}'
                        WHERE id_usuario = '{6}'"""
                        
                cursor.execute(sql.format(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], id_usuario))
                self.conexion.commit()
                print("¡Datos actualizados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            
    def modContacEmergencia(self, id_usuario, datosEmergencia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE contacto_emergencia SET 
                        nombre_contacto = '{0}',
                        relacion = '{1}',
                        telefono_contacto ='{2}'
                        WHERE id_emergencia = '{3}'"""
                        
                cursor.execute(sql.format(datosEmergencia[0], datosEmergencia[1], datosEmergencia[2], id_usuario))
                self.conexion.commit()
                print("¡Datos actualizados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            
    def modCargaFamiliar(self, id_usuario, datosCarga):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE cargas_familiares SET 
                        nombre_carga = '{0}',
                        parentesco = '{1}',
                        sexo ='{2}'
                        WHERE id_carga = '{3}'"""
                        
                cursor.execute(sql.format(datosCarga[0], datosCarga[1], datosCarga[2], id_usuario))
                self.conexion.commit()
                print("¡Datos actualizados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            
    def eliminarDatPersonales(self,id_usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE trabajador SET nombre = NULL,
                    apellido_mat = NULL, apellido_pat = NULL,
                    direccion = '',telefono = NULL,
                    sexo = NULL WHERE id_usuario = '{}'"""                       
                cursor.execute(sql.format(id_usuario,))
                self.conexion.commit()
                print("¡Datos Borrados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
    
    def eliminarContacEmergencia(self, id_usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE contacto_emergencia SET nombre_contacto = NULL,
                    relacion = NULL, telefono_contacto = NULL WHERE id_emergencia = '{}'"""                       
                cursor.execute(sql.format(id_usuario,))
                self.conexion.commit()
                print("¡Datos Borrados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
    
    def eliminarCargaFamiliar(self, id_usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE cargas_familiares SET nombre_carga = NULL,
                    parentesco = NULL, sexo = NULL WHERE id_carga = '{}'"""                       
                cursor.execute(sql.format(id_usuario,))
                self.conexion.commit()
                print("¡Datos Borrados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            

#CLASE Jefe
class Jefe(DAO):
    def __init__(self):
        super().__init__()
        
    def leerInformacionSexo(self):
        cursor = self.conexion.cursor()  
        consulta = """SELECT nombre, apellido_mat, apellido_pat, sexo
                    FROM trabajador;"""
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    
    def leerInformacionCargo(self):
        cursor = self.conexion.cursor()  
        consulta = """ SELECT t.nombre, t.apellido_mat, t.apellido_pat, dl.area, d.nombre_depto
                    FROM trabajador t
                    JOIN datos_laborales dl ON t.id_cargo = dl.id_cargo
                    JOIN departamento d ON t.id_departamento = d.id_departamento;"""
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    

class Rrhh(DAO):
    def __init__(self):
        super().__init__()
        
    def insertarDatosInicioSesion(self,datos1):
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """INSERT INTO usuario (nombre_usuario, passsword) VALUES ('{0}', '{1}');"""                    
                cursor.execute(sql.format(datos1[0], datos1[1]))
                self.conexion.commit()
                print("¡Datos Ingresados")
                
                consulta = "SELECT id_usuario FROM usuario WHERE nombre_usuario = %s AND passsword = %s"
                
                #extrayendo id 
                valores = (datos1[0], datos1[1])
                cursor.execute(consulta, valores)

                # Obtener el resultado de la consulta
                resultado = cursor.fetchone()

                if resultado:
                    id_usuario = resultado[0]
                    int(id_usuario)
                    return id_usuario
                else:
                    print("No se encontró ningún id_usuario con los valores proporcionados.")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            
    def insertarDatPersonales(self, datos2, traerID):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """INSERT INTO trabajador (idRelacion, id_cargo, id_usuario, id_departamento, nombre, apellido_mat, apellido_pat, direccion, telefono, sexo)
                VALUES ( null, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')"""
                        
                cursor.execute(sql.format(traerID, traerID, traerID, datos2[0],datos2[1],datos2[2],datos2[3],datos2[4],datos2[5]))
                self.conexion.commit()

            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            
    def insertarDatLaborales(self,datos3):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """ INSERT INTO datos_laborales (cargo, area, fecha_ingreso) VALUES ('trabajador','{0}','{1}')"""
                        
                cursor.execute(sql.format(datos3[0],datos3[1]))
                self.conexion.commit()
                print("¡Datos Ingresados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
    
    def insertarDatDepartamento(self, datos4):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """ INSERT INTO departamento (nombre_depto) VALUES ('{0}');"""
                cursor.execute(sql.format(datos4[0]))
                self.conexion.commit()
                print("¡Datos Ingresados!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
            
    def insertarContacEmergencia(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """ INSERT  contacto_emergencia (nombre_contacto, relacion, telefono_contacto) values ('', '', 0);"""
                cursor.execute(sql)
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")
    
    def insertarCargaFamiliar(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """INSERT  cargas_familiares (nombre_carga, parentesco, sexo) values ('', '', '');"""
                cursor.execute(sql)
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No hay conexion")