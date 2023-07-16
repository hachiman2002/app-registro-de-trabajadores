from validaciones import validaciones
#TRABAJADOR
def listarTrabajador(trabajador):
    
    print("Datos personales: ")
    contador = 1
    for c in trabajador:
        datos = "Nombre: {0} | Apellido P: {1} | Apellido M: {2} | Direccion: {3} | Tel: {4} | Sexo: {5}"
        print(datos.format(trabajador[5], trabajador[6], trabajador[7], trabajador[8], trabajador[9], trabajador[10]))
        contador = contador + 1
        if contador == 2:
            break
    print(" ")
    
def listarInformacionTrabajador(trabajador):
    print("Informacion Complementaria: ")
    contador = 1
    for c in trabajador:
        datos = "Cargo: {0} | Area: {1} | Fecha ingreso: {2} "
        print(datos.format(trabajador[0], trabajador[1], trabajador[2]))
        contador = contador + 1
        if contador == 2:
            break
    print(" ")
    
def listarCargaFamiliar(carga):
    print("Informacion Cargas Familiares: ")
    contador = 1
    for c in carga:
        datos = "Nombre carga: {0} | Parentesco: {1} | Sexo: {2} "
        print(datos.format(carga[0], carga[1], carga[2]))
        contador = contador + 1
        if contador == 2:
            break
    print(" ")

def listarContactoEmergencia(emergencia):
    print("Informacion Contacto Emergencia: ")
    contador = 1
    for c in emergencia:
        datos = "Nombre contacto: {0} | Relacion: {1} | Telefono: {2} "
        print(datos.format(emergencia[0], emergencia[1], emergencia[2]))
        contador = contador + 1
        if contador == 2:
            break
    print(" ")
    
def pedirDatPersonales():
    while True:
        nombre = str(input("Ingrese nombre:")).capitalize()
        if validaciones.validar_caracter(nombre):
            break
        else:
            print("El nombre debe contener al menos un carácter.")

    while True:
        apem = str(input("Ingrese apellido paterno:")).capitalize()
        if validaciones.validar_caracter(apem):
            break
        else:
            print("El apellido paterno debe contener al menos un carácter.")

    while True:
        apep = str(input("Ingrese apellido materno:")).capitalize()
        if validaciones.validar_caracter(apep):
            break
        else:
            print("El apellido materno debe contener al menos un carácter.")

    while True:
        direccion = str(input("Ingrese dirección:"))
        if validaciones.validar_caracter(direccion):
            break
        else:
            print("La direccion debe contener al menos un carácter.")
    

    while True:
        try:
            tel = int(input("Ingrese teléfono:"))
            break
        except ValueError:
            print("El teléfono debe ser un número entero.")

    while True:
        sexo = str(input("Ingrese sexo 'F, M':")).capitalize()
        if validaciones.validar_caracter(sexo) and (sexo=="F" or sexo=="M"):
            break
        else:
            print("El sexo debe ser 'F' o 'M'")

    list_datPersonales = [nombre, apem, apep, direccion, tel, sexo]
    return list_datPersonales


def pedirContacEmergencia():
    while True:
        nombre = str(input("Ingrese nombre:")).capitalize()
        if len(nombre) > 0:
            break
        else:
            print("El nombre debe contener al menos un carácter.")

    while True:
        relacion = str(input("Ingrese relación:")).capitalize()
        if len(relacion) > 0:
            break
        else:
            print("La relación debe contener al menos un carácter.")

    while True:
        try:
            tel = int(input("Ingrese teléfono:"))
            break
        except ValueError:
            print("El teléfono debe ser un número entero.")

    list_ContacEmergencia = [nombre, relacion, tel]

    return list_ContacEmergencia

def pedirCargaFamiliar():
    while True:
        nombre = str(input("Ingrese nombre:")).capitalize()
        if len(nombre) > 0:
            break
        else:
            print("El nombre debe contener al menos un carácter.")

    while True:
        parentesco = str(input("Ingrese parentesco:")).capitalize()
        if len(parentesco) > 0:
            break
        else:
            print("El parentesco debe contener al menos un carácter.")

    while True:
        sexo = str(input("Ingrese sexo 'F, M':")).capitalize()
        if len(sexo) > 0 and sexo in ['F', 'M']:
            break
        else:
            print("El sexo debe ser 'F' o 'M'")

    list_CargaFamiliar = [nombre, parentesco, sexo]

    return list_CargaFamiliar

#Funciones RRHH
def pedirDatosInicioSesion():
    while True:
        nombre = str(input("Ingrese nombre de usuario:"))
        if len(nombre) > 0:
            break
        else:
            print("El nombre de usuario debe contener al menos un carácter.")

    while True:
        password = str(input("Ingrese contraseña:"))
        if len(password) > 0:
            break
        else:
            print("La contraseña debe contener al menos un carácter.")

    list_inicio_sesion = [nombre, password]

    return list_inicio_sesion

def pedirDatLaborales():
    while True:
        area = str(input("Indique área:"))
        if len(area) > 0:
            break
        else:
            print("El área debe contener al menos un carácter.")

    import re

    while True:
        fechaIngreso = str(input("Indique fecha de ingreso (formato 'yyyy-mm-dd'):"))
        if re.match(r'^\d{4}-\d{2}-\d{2}$', fechaIngreso):
            break
        else:
            print("La fecha de ingreso debe tener el formato 'yyyy-mm-dd'.")


    list_laborales = [area, fechaIngreso]
    return list_laborales


def pedirDatDepartamento():
    while True:
        depto = str(input("Indique su departamento:"))
        if len(depto) > 0:
            break
        else:
            print("El nombre del departamento no puede estar vacío.")

    list_depto = [depto]
    return list_depto

#Funciones Jefe
def listarTrabajadoresSexo(trabajadores):
    print("Informacion Trabajador:")
    print("-----------------------------------------------------")
    print("| Nombre     | Apellido P   | Apellido M   | Sexo   |")
    print("-----------------------------------------------------")
    
    for trabajador in trabajadores:
        nombre = trabajador[0]
        apep = trabajador[1]
        apem = trabajador[2]
        sexo = trabajador[3]
        
        datos = "| {0} | {1} | {2} | {3} "
        print(datos.format(nombre.ljust(10), apep.ljust(12), apem.ljust(12), sexo.ljust(5)),"|")
    
    print("-----------------------------------------------------")


def listarTrabajadoresCargo(trabajadores):
    print("Informacion Trabajador:")
    print("-----------------------------------------------------------------------")
    print("| Nombre     | Apellido P   | Apellido M   | Area       | Depto       |")
    print("-----------------------------------------------------------------------")
    
    for trabajador in trabajadores:
        nombre = trabajador[0]
        apep = trabajador[1]
        apem = trabajador[2]
        area = trabajador[3]
        depto = trabajador[4]
        
        datos = "| {0} | {1} | {2} | {3} | {4} "
        print(datos.format(nombre.ljust(10), apep.ljust(12), apem.ljust(12), area.ljust(10), depto.ljust(10)),"|")
    
    print("-----------------------------------------------------------------------")
