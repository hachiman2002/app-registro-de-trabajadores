from DB.conexion import Trabajador
from DB.conexion import Jefe
from DB.conexion import Rrhh

import funciones.funciones as funciones

def menuTrabajador(id_usuario):
    conexion = Trabajador()
    menu = (""""
                ╔═════════════════════════════════════════╗
                ║             Menu Trabajador             ║
                ╠═════════════════════════════════════════╣
                ║  1. Leer información                    ║
                ║  2. Actualizar información              ║
                ║  3. Eliminar información                ║
                ║  4. Agregar datos                       ║
                ║  5. Salir                               ║
                ╚═════════════════════════════════════════╝
        """)
    print(menu)
    while True:
        while True:
            opTrabajador = input("Escoja una opción:")
            if opTrabajador.strip():  # Verifica que la entrada no esté vacía después de eliminar espacios en blanco
                try:
                    opTrabajador = int(opTrabajador)
                    break
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")
            else:
                print("La opción no puede estar vacía. Intente nuevamente.")
            
        #Leer informacion
        if opTrabajador == 1:
            #mostrar datos trabjador
            trabajador = conexion.leerInformacion(id_usuario)
            listarTrabajador = funciones.listarTrabajador(trabajador)
            
            #mostrar cargo, departamento, area, fecha ingreso
            infoTrabajador = conexion.leerInformacionTrabajador(id_usuario)
            listarTrabajador = funciones.listarInformacionTrabajador(infoTrabajador)
            
            #mostrar carga familiar
            infoCargaFamiliar = conexion.leerCargaFamiliar(id_usuario)
            listarCargaFamiliar = funciones.listarCargaFamiliar(infoCargaFamiliar)

            #mostrar contacto emergencia
            infoContactoEmergencia = conexion.leerContactoEmergencia(id_usuario)
            listarContactoEmergencia = funciones.listarContactoEmergencia(infoContactoEmergencia)
            
            print(menu)
        #actualizar informacion
        elif opTrabajador == 2:
            while True:
                print("Info: No se puede actualizar el Rut y los datos laborales")
                menu_mod = ("""
                    ╔═════════════════════════════════════════╗
                    ║        Menú de Modificación Trabajador  ║
                    ╠═════════════════════════════════════════╣
                    ║  1. Modificar datos personales          ║
                    ║  2. Modificar contacto de emergencia    ║
                    ║  3. Modificar cargas familiares         ║
                    ║  4. Volver atrás                        ║
                    ╚═════════════════════════════════════════╝
                    """)
                print(menu_mod)
                opc = int(input("Escoja opcion:"))
                
                if opc == 1:
                    datos = funciones.pedirDatPersonales()
                    conexion.modDatPersonales(id_usuario,datos)
                elif opc == 2:
                    datosEmergencia = funciones.pedirContacEmergencia()
                    conexion.modContacEmergencia(id_usuario, datosEmergencia)
                elif opc == 3:
                    datosCarga = funciones.pedirCargaFamiliar()
                    conexion.modCargaFamiliar(id_usuario, datosCarga)
                elif opc == 4:
                    break
                else:
                    print("opcion incorrecta intente denuevo")
            print(menu)
        #Eliminar informacion    
        elif opTrabajador == 3:
            while True:
                menu_eli = ("""
                    ╔═════════════════════════════════════════╗
                    ║           Menú de Eliminación           ║
                    ╠═════════════════════════════════════════╣
                    ║  1. Eliminar datos personales           ║
                    ║  2. Eliminar contacto de emergencia     ║
                    ║  3. Eliminar cargas familiares          ║
                    ║  4. Volver atrás                        ║
                    ╚═════════════════════════════════════════╝
                    """)
                print(menu_eli)
                opcE = int(input("Escoja opcion:"))
                
                if opcE == 1:
                    conexion.eliminarDatPersonales(id_usuario)
                elif opcE == 2:
                    conexion.eliminarContacEmergencia(id_usuario)
                elif opcE == 3:
                    conexion.eliminarCargaFamiliar(id_usuario)
                elif opcE == 4:
                    break
                else:
                    print("opcion incorrecta intente denuevo")
            print(menu)
        #Agregar informacion 
        elif opTrabajador == 4:
            while True:
                menu_agregar = ("""
                        ╔═════════════════════════════════════════╗
                        ║             Menú de Inserción           ║
                        ╠═════════════════════════════════════════╣
                        ║  Info: Si hay datos insertados, serán   ║
                        ║        actualizados                     ║
                        ║  1. Insertar contacto de emergencia     ║
                        ║  2. Insertar cargas familiares          ║
                        ║  3. Volver atrás                        ║
                        ╚═════════════════════════════════════════╝
                    """)
                print(menu_agregar)
                opcI = int(input("Escoja opcion:"))
                if opcI == 1:
                    datosEmergencia = funciones.pedirContacEmergencia()
                    conexion.modContacEmergencia(id_usuario, datosEmergencia)
                elif opcI == 2:
                    datosCarga = funciones.pedirCargaFamiliar()
                    conexion.modCargaFamiliar(id_usuario, datosCarga)
                elif opcI == 3:
                        break
                else:
                    print("opcion incorrecta intente denuevo")
            print(menu)

        #Cerrar sesion 
        elif opTrabajador == 5:
            print("Sesion cerrada exitosamente")
            break
        else:
            print("Opcion invalida, intente de nuevo")
            print(menu)


def menuRRHH():
    conexion = Rrhh()
    menu = (""""
            ╔═════════════════════════════════════════╗
            ║                Menu RRHHH               ║
            ╠═════════════════════════════════════════╣
            ║  1. Registrar Trabajador                ║
            ║  2. Salir                               ║
            ╚═════════════════════════════════════════╝

        """)

    print(menu)
    while True:
        while True:
            opRRHH = input("Escoja una opción:")
            if opRRHH.strip():  # Verifica que la entrada no esté vacía después de eliminar espacios en blanco
                try:
                    opRRHH = int(opRRHH)
                    break
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")
            else:
                print("La opción no puede estar vacía. Intente nuevamente.")

        if opRRHH == 1:
            print("Formulario de trabajadores:")
            print("Parte 1: Ingreso datos de inicio de sesion")
            datos1 = funciones.pedirDatosInicioSesion()
            #esta funcion se encarga de ingresar los datos y traer el id
            traerID = conexion.insertarDatosInicioSesion(datos1)
            print("--------------------------------------------")
            print("Parte 2: Ingreso datos personales")
            datos2 = funciones.pedirDatPersonales()
            print("Datos ingresados!")
            print("--------------------------------------------")
            print("Parte 3: Ingreso datos laborales")
            datos3 = funciones.pedirDatLaborales()
            conexion.insertarDatLaborales(datos3)
            print("--------------------------------------------")
            print("Parte 4: Ingreso datos departamento")
            datos4 = funciones.pedirDatDepartamento()
            conexion.insertarDatDepartamento(datos4)
            print("--------------------------------------------")
            conexion.insertarDatPersonales(datos2,traerID)
            
            conexion.insertarContacEmergencia()
            conexion.insertarCargaFamiliar()
            print(menu)
        elif opRRHH == 2:
            print("Sesion cerrada exitosamente")
            break
        else:
            print("Opcion invalida, intente de nuevo")


def menuJefe():
    menu = (""""
            ╔═════════════════════════════════════════╗
            ║                Menu Jefe                ║
            ╠═════════════════════════════════════════╣
            ║  1. Listar trabajadores por sexo        ║
            ║  2. Listar trabajadores por área y/o    ║
            ║     departamento                        ║
            ║  3. Salir                               ║
            ╚═════════════════════════════════════════╝
        """)
    print(menu)
    while True:
        conexion = Jefe()
        while True:
            opJefe = input("Escoja una opción:")
            if opJefe.strip():  # Verifica que la entrada no esté vacía después de eliminar espacios en blanco
                try:
                    opJefe = int(opJefe)
                    break
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")
            else:
                print("La opción no puede estar vacía. Intente nuevamente.")

        if opJefe == 1:
            trabajadoresSexo = conexion.leerInformacionSexo()
            listarTrabajadorSexo = funciones.listarTrabajadoresSexo(trabajadoresSexo)
            print(menu)
        elif opJefe == 2:
            trabajadores = conexion.leerInformacionCargo()
            listarTrabajador = funciones.listarTrabajadoresCargo(trabajadores)
            print(menu)
        elif opJefe == 3:
            print("Sesion cerrada exitosamente")
            break
        else:
            print("Opcion invalida, intente de nuevo")
            
