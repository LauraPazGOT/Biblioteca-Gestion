# bibliotecario.py
# Menú bibliotecario: inicio de sesión y menú de funciones

import time
import os
from colorama import init, Fore, Back
import catalogo
import usuario

init(autoreset=True)

# ----------------------------------------------------- #
#                   Funciones auxiliares               #
# ----------------------------------------------------- #

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def iniciar_sesion_bibliotecario():
    """Inicio de sesión para bibliotecarias."""
    print(Fore.MAGENTA + "-"*45)
    nombre = input(Fore.LIGHTMAGENTA_EX + "Ingrese su nombre: ").capitalize()
    contrasenia = input(Fore.LIGHTMAGENTA_EX + "Ingrese su contraseña: ")
    print(Fore.MAGENTA + "-"*45)

    usuario_valido = next((b for b in bibliotecarios if b["nombre"] == nombre), None)
    if usuario_valido:
        if usuario_valido["contraseña"] == contrasenia:
            print(Fore.LIGHTMAGENTA_EX + "Inicio de sesión exitoso")
            time.sleep(1)
            return True
        else:
            print(Fore.RED + "Contraseña incorrecta")
            time.sleep(1)
            return False
    else:
        print(Fore.RED + "Nombre de usuario inexistente")
        time.sleep(1)
        return False

# ----------------------------------------------------- #
#                    Menú bibliotecaria                #
# ----------------------------------------------------- #

def menu_bibliotecario():
    """Muestra el menú principal para bibliotecarias."""
    while True:
        print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "MENÚ".center(45))
        print(Fore.MAGENTA + "-"*45)
        print(Fore.MAGENTA + "[1] Ver catálogo")
        print(Fore.MAGENTA + "[2] Buscar en catálogo")
        print(Fore.MAGENTA + "[3] Modificar catálogo")
        print(Fore.MAGENTA + "[4] Ver información de usuarios")
        print(Fore.MAGENTA + "[5] Cerrar sesión")
        print(Fore.MAGENTA + "-"*45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            clear()
            catalogo.ver_catalogo()
            time.sleep(1)

        elif opcion == "2":
            clear()
            catalogo.buscar()
            time.sleep(1)

        elif opcion == "3":
            while True:
                clear()
                print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "MODIFICAR CATÁLOGO".center(45))
                print(Fore.LIGHTMAGENTA_EX + "-"*45)
                print(Fore.LIGHTMAGENTA_EX + "[1] Agregar libro")
                print(Fore.LIGHTMAGENTA_EX + "[2] Eliminar libro")
                print(Fore.LIGHTMAGENTA_EX + "[3] Modificar libro")
                print(Fore.LIGHTMAGENTA_EX + "[4] Volver al menú")
                print(Fore.LIGHTMAGENTA_EX + "-"*45)

                subopcion = input("Seleccione una opción: ").strip()
                if subopcion == "1":
                    catalogo.agregar_libro()
                elif subopcion == "2":
                    catalogo.quitar_libro()
                elif subopcion == "3":
                    catalogo.ver_catalogo()
                    catalogo.modificar_libro()
                elif subopcion == "4":
                    break
                else:
                    print(Fore.RED + "Opción inválida")
                    time.sleep(1)

        elif opcion == "4":
            clear()
            print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "USUARIOS".center(65))
            print(f"{'Nombre':<20}{'Apellido':<20}{'Edad':<5}{'Institución':<12}{'Mail':<10}")
            for u in usuario.ficha_de_usuarios:
                print(f"{u['nombre']:<20}{u['apellido']:<20}{u['edad']:<5}{u['institucion']:<12}{u['mail']:<10}")
            time.sleep(2)

        elif opcion == "5":
            print(Fore.LIGHTCYAN_EX + "Gracias por usar el sistema.")
            time.sleep(1)
            clear()
            break

        else:
            print(Fore.RED + "Ingrese una opción válida")
            time.sleep(1)
            clear()

#-----------------------------------------------------# 
# Se definen los datos de las bibliotecarias # 
#-----------------------------------------------------#

bibliotecaria_1 = {"nombre":"Araceli","contraseña":"2167"} 
bibliotecaria_2 = {"nombre":"Laura","contraseña":"9535"} 

bibliotecarios = [bibliotecaria_1,bibliotecaria_2] 
init(autoreset=True)
