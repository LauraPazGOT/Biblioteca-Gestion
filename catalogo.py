#catalogo.py
# Catálogo completo: funciones para usuarios y bibliotecarias

import json
import time
import os
from datetime import date, timedelta
from colorama import init, Fore, Back

# ----------------------------------------------------- #
#                  Funciones auxiliares                 #
# ----------------------------------------------------- #

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def guardar_json_catalogo():
    """Guarda el catálogo completo en JSON."""
    try:
        with open(ruta_catalogo, 'w', encoding='utf-8') as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error al guardar el catálogo: {e}")

def leer_json_catalogo():
    """Lee el catálogo desde JSON. Devuelve lista vacía si falla."""
    try:
        with open(ruta_catalogo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (OSError, json.JSONDecodeError):
        return []

def mostrar_libro(libro):
    """Muestra la información de un libro de forma tabular."""
    print(f"{libro['nombre']:<45}{libro['autor']:<30}{libro['ISBN']:<13}{libro['editorial']:<30}{libro['año']:<6}{libro['género']:<20}{libro['estado']:<10}")

def mostrar_catalogo(libros):
    """Muestra una lista de libros en tabla."""
    print(Back.LIGHTCYAN_EX + Fore.BLACK + "CATÁLOGO".center(45))
    print(Fore.CYAN + "*"*150)
    print(Fore.CYAN + f"{'Nombre':<45}{'Autor':<30}{'ISBN':<13}{'Editorial':<30}{'Año':<6}{'Género':<20}{'Estado':<10}")
    for libro in libros:
        mostrar_libro(libro)
    print(Fore.CYAN + "*"*150)

# ----------------------------------------------------- #
#                     Funciones de búsqueda             #
# ----------------------------------------------------- #

def buscar():
    """Permite buscar libros por distintos criterios."""
    while True:
        print(Back.LIGHTCYAN_EX + Fore.BLACK + "BÚSQUEDA POR CATÁLOGO".center(55))
        print(Fore.LIGHTCYAN_EX + "-"*45)
        print(Fore.LIGHTCYAN_EX + "Seleccione búsqueda:\n[1] Nombre\n[2] Autor\n[3] ISBN\n[4] Género\n[5] Palabra clave\n[6] Volver al menú")
        print(Fore.LIGHTCYAN_EX + "-"*45)
        opcion = input().strip()

        if opcion == "6":
            clear()
            return

        criterio = None
        valor = None

        if opcion == "1":
            valor = input("Ingrese nombre del libro: ")
            criterio = "nombre"
        elif opcion == "2":
            valor = input("Ingrese autor: ")
            criterio = "autor"
        elif opcion == "3":
            valor = input("Ingrese ISBN: ")
            criterio = "ISBN"
        elif opcion == "4":
            valor = input("Ingrese género (Ciencia Ficción, Fantasía, Infantil, Educación): ")
            criterio = "género"
        elif opcion == "5":
            valor = input("Ingrese palabra clave: ")
            criterio = "palabras claves"
        else:
            print(Back.RED + "Opción no válida")
            continue

        encontrados = [libro for libro in catalogo if valor in libro.get(criterio, "")]
        if encontrados:
            mostrar_catalogo(encontrados)
        else:
            print(Fore.RED + "No se encontraron libros con ese criterio.")
        time.sleep(2)
        clear()

# ----------------------------------------------------- #
#                Funciones de gestión de libros        #
# ----------------------------------------------------- #

def agregar_libro():
    """Permite a bibliotecarias agregar un libro al catálogo."""
    print(Fore.MAGENTA + "Complete los datos del libro:")
    nombre = input("Nombre: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    if any(libro["ISBN"] == isbn for libro in catalogo):
        print(Fore.RED + "El ISBN ya existe. No se agregará.")
        return
    editorial = input("Editorial: ")
    anio = input("Año: ")
    genero = input("Género: ")
    palabras_claves = input("Palabras clave: ")
    nuevo_libro = {
        "nombre": nombre,
        "autor": autor,
        "ISBN": isbn,
        "editorial": editorial,
        "año": anio,
        "género": genero,
        "palabras claves": palabras_claves,
        "estado": "Disponible"
    }
    catalogo.append(nuevo_libro)
    guardar_json_catalogo()
    print(Fore.MAGENTA + "Libro agregado correctamente.")
    time.sleep(1)
    clear()

def quitar_libro():
    """Permite eliminar un libro por ISBN."""
    isbn = input("Ingrese ISBN del libro a eliminar: ")
    libro = next((l for l in catalogo if l["ISBN"] == isbn), None)
    if libro:
        confirm = input("¿Desea eliminarlo? [Si/No]: ").lower()
        if confirm == "si":
            catalogo.remove(libro)
            guardar_json_catalogo()
            print("Libro eliminado.")
    else:
        print("No se encontró el ISBN.")
    time.sleep(1)
    clear()

def modificar_libro():
    """Permite modificar un libro por ISBN."""
    isbn = input("Ingrese ISBN del libro a modificar: ")
    libro = next((l for l in catalogo if l["ISBN"] == isbn), None)
    if libro:
        mostrar_libro(libro)
        campo = input("Campo a modificar (nombre, autor, ISBN, editorial, año, genero, palabras claves): ")
        if campo in libro:
            valor = input("Nuevo valor: ")
            libro[campo] = valor
            guardar_json_catalogo()
            print("Libro modificado correctamente.")
            mostrar_libro(libro)
        else:
            print("Campo inválido.")
    else:
        print("ISBN no encontrado.")
    time.sleep(1)
    clear()

# ----------------------------------------------------- #
#                Funciones para usuarios               #
# ----------------------------------------------------- #

def solicitar_libro():
    """Permite al usuario solicitar un libro por ISBN."""
    isbn = input("Ingrese ISBN del libro a solicitar: ")
    libro = next((l for l in catalogo if l["ISBN"] == isbn), None)
    if libro:
        mostrar_libro(libro)
        if libro["estado"] == "Disponible":
            if input("Desea solicitar el libro? [Si/No]: ").lower() == "si":
                libro["estado"] = "Solicitado"
                fecha_dev = date.today() + timedelta(days=10)
                print(f"Libro solicitado. Fecha de devolución: {fecha_dev}")
                guardar_json_catalogo()
        else:
            print("El libro no está disponible.")
    else:
        print("ISBN no encontrado.")
    time.sleep(1)
    clear()

def devolver_libro():
    """Permite devolver un libro solicitado."""
    isbn = input("Ingrese ISBN del libro a devolver: ")
    libro = next((l for l in catalogo if l["ISBN"] == isbn), None)
    if libro:
        mostrar_libro(libro)
        if libro["estado"] == "Solicitado":
            if input("Desea devolver el libro? [Si/No]: ").lower() == "si":
                libro["estado"] = "Disponible"
                print("Libro devuelto correctamente.")
                guardar_json_catalogo()
        else:
            print("El libro no estaba solicitado.")
    else:
        print("ISBN no encontrado.")
    time.sleep(1)
    clear()

def renovar_libro():
    """Permite renovar un libro solicitado."""
    isbn = input("Ingrese ISBN del libro a renovar: ")
    libro = next((l for l in catalogo if l["ISBN"] == isbn), None)
    if libro:
        mostrar_libro(libro)
        if libro["estado"] == "Solicitado":
            if input("Desea renovar el libro? [Si/No]: ").lower() == "si":
                nueva_fecha = date.today() + timedelta(days=10)
                print(f"Libro renovado. Nueva fecha de devolución: {nueva_fecha}")
                guardar_json_catalogo()
        else:
            print("El libro no estaba solicitado.")
    else:
        print("ISBN no encontrado.")
    time.sleep(1)
    clear()

# ----------------------------------------------------- #
#                   Datos del catálogo                 #
# ----------------------------------------------------- #

init(autoreset=True)
ruta_catalogo = 'catalogo.json'
catalogo = leer_json_catalogo()
