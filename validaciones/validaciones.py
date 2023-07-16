#validar menu principal
def validar_opcion(opcion):
    if opcion.isdigit():
        return True
    else:
        return False

#validar credenciales
def validar_credenciales(nombre_usuario, contrasena):
    if len(nombre_usuario) > 1 and nombre_usuario.isalnum() and len(contrasena) > 1 and contrasena.isalnum():
        return True
    else:
        return False
    
#trabajor 
def validar_caracter(variable):
    if len(variable) > 0:
        return True
    else:
        return False