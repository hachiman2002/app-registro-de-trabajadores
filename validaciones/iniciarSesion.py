from DB.conexion import DAO
import submenu
from validaciones import validaciones


def credenciales():
    while True:
        nombre_usuario = input("Ingresa tu nombre de usuario: ")
        contrasena = input("Ingresa tu contraseña: ")
        lista_credenciales = [nombre_usuario, contrasena]

        
        if validaciones.validar_credenciales(nombre_usuario, contrasena):
            return lista_credenciales
            break
        else:
            print("Credenciales inválidas. El nombre de usuario y la contraseña deben tener al menos un carácter y contener solo letras y números.")


def inicioSesion():
    dao = DAO()
    
    lista = credenciales()
    vSesion = dao.ValidarSesion(lista[0], lista[1])
    
    if vSesion == True:
        #en conexion en la funcion entregar nombre llama a elegir opciones
        eNombre = dao.entregarNombre(lista[0], lista[1])
        tCargoUsuario = dao.traerCargoUsuario(lista[0], lista[1])
        idUsuario = dao.traerId(lista[0], lista[1])
        if tCargoUsuario == 'trabajador':
            submenu.menuTrabajador(idUsuario)
        elif tCargoUsuario == 'jefe':
            submenu.menuJefe()
        elif tCargoUsuario == 'rrhh':
            submenu.menuRRHH()
        else:
            print("Error al traer cargo, intente de nuevo")
    else:
        print("Error de inicio de sesion")


