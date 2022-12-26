import pickle
import os
from funciones import *
from Articulos import art

def crear_articulo():
    i = int(0)

    try:
        with open('articulos.pkl', 'rb') as f:
            while True:
                try:
                    pickle.load(f)
                    i += 1
                except EOFError: break
    except: pass

    desc = str(input("Descripcion: "))
    cont = str(input("Conteo: "))
    p_u = int(input("Precio unitario: $"))
    articulo = art(i, desc, cont, p_u)

    with open('articulos.pkl', 'ab') as f:
        pickle.dump(articulo, f)

    input('Se ha creado el articulo con exito! Presione ENTER para continuar')
    return True

def modificar_articulo():
    articulos = []
    cargar(articulos, 'articulos')
    if len(articulos) == 0:
        input('No hay articulos para modificar, presione ENTER para volver')
        return False

    for articulo in articulos:
        print(articulo)

    opc = int(input('Que articulo desea modificar? '))
    continuar = menu_modificar_articulos(opc, articulos)
    if continuar == True:
        return True
    else:
        input('Ha ocurrido un error, presione ENTER para volver')
        return False


def listar_articulos():
    articulos = []
    cargar(articulos, 'articulos')
    if len(articulos) == 0:
        input('No hay articulos para mostrar, presione ENTER para volver')
        return False

    for articulo in articulos:
        print(articulo)
    return True


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
        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')
        input('Presione ENTER para continuar')