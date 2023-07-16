import validaciones.iniciarSesion as iniciarSesion
from datetime import datetime

import pygame 
def reproducir_sonido_error():
    pygame.mixer.init()
    pygame.mixer.music.load('sonidos/error.mp3')
    pygame.mixer.music.play()
    
def reproducir_sonido_encendido():
    pygame.mixer.init()
    pygame.mixer.music.load('sonidos/encendido.mp3')
    pygame.mixer.music.play()

def reproducir_sonido_apagado():
    pygame.mixer.init()
    pygame.mixer.music.load('sonidos/apagar.mp3')
    pygame.mixer.music.play()
    
# Obtener la hora actual
hora_actual = datetime.now().time()

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print(f"""
                {hora_actual}
                ╔═════════════════════════════════════════╗
                ║             MENU PRINCIPAL              ║
                ║             CORREO DE YURY              ║
                ╠═════════════════════════════════════════╣
                ║  1. Iniciar sesión                      ║
                ║  2. Términos y condiciones              ║
                ║  3. Salir                               ║
                ╚═════════════════════════════════════════╝
            """)
            while True:
                opcion = str(input("Seleccione una opcion:"))
                if len(opcion)==1 :
                    break
                else:
                    print("Opcion invalida")
            
            opcion = int(opcion)
            if opcion <1 or opcion >3:
                print("Opcion incorrecta, ingrese nuevamente...")
                reproducir_sonido_error()
            elif opcion == 3:
                print("Ha salido del programa")
                continuar = False
                reproducir_sonido_apagado()
                time.sleep(2)
                break
            else:
                opcionCorrecta = True
                ejecutarOpcionPrincipal(opcion)



def ejecutarOpcionPrincipal(opcion):
    volver = False
    while (volver == False):
        if opcion == 1:
            iniciarSesion.inicioSesion()
            break
        elif opcion == 2:
            archivo = open('terminos y condiciones.txt', 'r')
            contenido = archivo.read()
            archivo.close()
            print(contenido)
            volver = True

        else:
            print("Opcion incorrecta intente denuevo")
            
            reproducir_sonido_error()

import time 
BAR_LEN = 24 
elements = ['-', '\\','|','/']
print("Cargando programa")
for i in range(BAR_LEN+1):
    frame = i % len(elements)
    print(f'\r[{elements[frame]*i:=<{BAR_LEN}}]', end='')
    time.sleep(0.1)
print("\nPrograma cargado con exito")
reproducir_sonido_encendido()
menuPrincipal()
