# usuario.py
# Menú usuario: incluye inicio de sesión, registro y menú con todas las funciones.

import os
import time
import json
from colorama import init, Fore, Back
import catalogo

# ----------------------------------------------------- #
#                  Funciones auxiliares                 #
# ----------------------------------------------------- #

def clear():
    """Limpia la pantalla según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")

def guardar_json(path, data):
    """Guarda datos en un archivo JSON."""
    try:
        with open(path, 'w', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error al guardar {path}: {e}")

def leer_json(path):
    """Lee datos desde un archivo JSON. Devuelve lista vacía si falla."""
    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (OSError, json.JSONDecodeError):
        return []

# ----------------------------------------------------- #
#                    Registro usuario                   #
# ----------------------------------------------------- #

def registro():
    """Registra un nuevo usuario en el sistema."""
    print(Fore.CYAN + "Complete los siguientes datos")
    
    while True:
        nombre = input("Ingrese su nombre: \n")
        apellido = input("Ingrese su apellido: \n")
        edad = input("Ingrese su edad: \n")
        institucion = input("Ingrese la institución a la que pertenece: \n")
        mail = input("Ingrese su mail: \n").lower()

        # Verifica si el correo ya está registrado
        if any(u["mail"] == mail for u in ficha_de_registro):
            print(Fore.RED + "Correo ya registrado, intente con otro.\n")
        else:
            break

    contrasenia = input("Genere una contraseña: \n")

    # Usuario completo
    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "institucion": institucion,
        "mail": mail,
        "contrasenia": contrasenia
    }
    ficha_de_registro.append(nuevo_usuario)
    guardar_json(ruta_usuarios, ficha_de_registro)

    # Usuario sin contraseña
    ficha_de_usuarios.append({k: v for k, v in nuevo_usuario.items() if k != "contrasenia"})
    guardar_json(ruta_usuarios_sin_contrasenia, ficha_de_usuarios)

    print(Fore.CYAN + "Registro OK")
    time.sleep(1)
    clear()
    return nuevo_usuario

# ----------------------------------------------------- #
#                 Inicio de sesión usuario             #
# ----------------------------------------------------- #

def iniciar_sesion_usuario():
    """Permite a un usuario iniciar sesión. Retorna True si tiene éxito."""
    print(Fore.CYAN + "-" * 45)
    mail_ingresado = input("Ingrese su mail: \n").lower()
    contrasenia_ingresada = input("Ingrese contraseña: \n")
    print(Fore.CYAN + "-" * 45)

    for usuario in ficha_de_registro:
        if usuario["mail"] == mail_ingresado and usuario["contrasenia"] == contrasenia_ingresada:
            ficha_usuario_activo.append(usuario)
            print(Fore.CYAN + f"Bienvenido/a, {usuario['nombre']}")
            return True, ficha_usuario_activo

    print(Fore.RED + "Usuario y/o contraseña inválidos")
    opcion = input("¿Desea registrarse? [s/n]: \n")    
    if opcion.lower() == 's':
        time.sleep(1)
        clear()
        registro()
    return False

# ----------------------------------------------------- #
#                  Menú del usuario                    #
# ----------------------------------------------------- #

def menu_usuario():
    """Muestra el menú de usuario y ejecuta la opción elegida."""
    print(Back.CYAN + Fore.BLACK + "MENÚ".center(45))
    print(Fore.CYAN + "-" * 45)
    print(Fore.CYAN + "[1] Ver catálogo.\n[2] Búsqueda en el catálogo. \n[3] Solicitar libro.\n[4] Renovar libro.\n[5] Devolver libro.\n[6] Acceder a mi información.\n[7] Cerrar sesión.")
    print(Fore.CYAN + "-" * 45)
    menu = input().strip()

    if menu == "1":
        clear()
        catalogo.ver_catalogo()
    elif menu == "2":
        clear()
        catalogo.buscar()
    elif menu == "3":
        clear()
        print(Back.CYAN + Fore.BLACK + "SOLICITAR LIBRO".center(45))
        catalogo.ver_catalogo()
        catalogo.solicitar_libro()
    elif menu == "4":
        clear()
        print(Back.CYAN + Fore.BLACK + "RENOVAR LIBRO".center(45))
        catalogo.ver_catalogo()
        catalogo.renovar_libro()
    elif menu == "5":
        clear()
        print(Back.CYAN + Fore.BLACK + "DEVOLVER LIBRO".center(45))
        catalogo.ver_catalogo()
        catalogo.devolver_libro()
    elif menu == "6":
        clear()
        print(Back.CYAN + Fore.BLACK + "MI INFORMACIÓN".center(45))
        print(f"{'Nombre':<20}{'Apellido':<20}{'Edad':<5}{'Institución':<12}{'Mail':<10}")
        for usuario_activo in ficha_usuario_activo:
            print(f"{usuario_activo['nombre']:<20}{usuario_activo['apellido']:<20}{usuario_activo['edad']:<5}{usuario_activo['institucion']:<12}{usuario_activo['mail']:<10}")
    elif menu == "7":
        print("Gracias por usar nuestro sitio.")
        if ficha_usuario_activo:
            ficha_usuario_activo.pop()
        time.sleep(1)
        clear()
        return
    else:
        print(Back.RED + "Ingrese una opción válida\n")

    time.sleep(1)
    menu_usuario()  # vuelve al menú principal
    catalogo.guardar_json_catalogo()  # guarda cualquier cambio

# ----------------------------------------------------- #
#                    Datos de usuarios                #
# ----------------------------------------------------- #

ruta_usuarios = 'usuarios.json'
ruta_usuarios_sin_contrasenia = 'usuarios_sin_contrasenia.json'

ficha_de_registro = leer_json(ruta_usuarios)
ficha_de_usuarios = leer_json(ruta_usuarios_sin_contrasenia)
ficha_usuario_activo = []

init(autoreset=True)
