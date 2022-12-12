import os
from funciones import *

def menu_articulos():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear articulo")
        print("2. Modificar articulo")
        print("3. Listar articulos")
        print("0. Volver al menu principal")
        print("\nOpcion: ", end = '')
        opc = int(input())

        if opc == 0: break
        elif opc == 1: crear_articulo()
        elif opc == 2: modificar_articulo()
        elif opc == 3: listar_articulos()
        else: 'Opcion incorrecta, intente nuevamente'