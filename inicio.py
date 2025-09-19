# Menú principal: contiene todo el inicio (y sus accesos a las distintas funciones).

import time
import os
from colorama import init, Fore, Back, Style
import usuario
import bibliotecario
import catalogo

"""
Biblioteca Virtual
------------------
Este programa permite acceder a una biblioteca digital con dos tipos de usuarios:
- Bibliotecarios: pueden gestionar el catálogo y ver la información de todos los usuarios.
- Usuarios: pueden registrarse, iniciar sesión, buscar libros, solicitar/renovar préstamos y consultar su información.
"""

# ----------------------------------------------------- #
#                  Funciones generales                  #
# ----------------------------------------------------- #

def clear():
    """Limpia la pantalla según el sistema operativo."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu_principal():
    """Muestra el menú principal."""
    print(Back.LIGHTCYAN_EX + Style.BRIGHT + "BIENVENIDO/A A LA BIBLIOTECA VIRTUAL".center(45))
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX + "-" * 45)
    print("Por favor elija una opción: \n[1] Iniciar sesión\n[2] Registrarse\n[3] Salir")
    print(Fore.LIGHTCYAN_EX + "-" * 45)

def mostrar_menu_login():
    """Muestra el menú de inicio de sesión."""
    print(Fore.LIGHTCYAN_EX + "-" * 45)
    print("Seleccione si es usuario o bibliotecaria.\n[1] Usuario\n[2] Bibliotecaria")
    print(Fore.LIGHTCYAN_EX + "-" * 45)

def inicio():
    """Función principal que organiza la ejecución del sistema."""
    variable = True
    while variable:
        mostrar_menu_principal()
        eleccion = input().strip()

        if eleccion == "1":
            mostrar_menu_login()
            tipo_de_usuario = input().strip()
            clear()

            if tipo_de_usuario == "1":  # Usuario
                print(Back.CYAN + Fore.BLACK + "Inicio de sesión: USUARIO".center(45))
                if usuario.iniciar_sesion_usuario():
                    time.sleep(1)
                    clear()
                    usuario.menu_usuario()

            elif tipo_de_usuario == "2":  # Bibliotecario
                print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "Inicio de sesión: BIBLIOTECARIO".center(45))
                if bibliotecario.iniciar_sesion_bibliotecario():
                    time.sleep(1)
                    clear()
                    bibliotecario.menu_bibliotecario()
            else:
                print(Fore.RED + "Ingrese una opción válida.")
                time.sleep(1)
                clear()

        elif eleccion == "2":  # Registro de usuario
            clear()
            print(Back.CYAN + Fore.BLACK + "REGISTRO".center(45))
            usuario.registro()

        elif eleccion == "3":
            print("Gracias por usar nuestro sistema.")
            variable = False

        else:
            print(Fore.RED + "Ingrese una opción válida.")
            time.sleep(1)
            clear()

# ----------------------------------------------------- #
#                     Punto de entrada                  #
# ----------------------------------------------------- #

if __name__ == "__main__":
    init(autoreset=True)
    inicio()
