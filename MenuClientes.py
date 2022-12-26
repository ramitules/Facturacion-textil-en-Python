import pickle
import os
from funciones import *
from Clientes import cli

def crear_cliente():
    i = int(0)
    
    try:
        with open('clientes.pkl', 'rb') as f:
            while True:
                try:
                    pickle.load(f)
                    i += 1
                except EOFError: break
    except: pass

    nombre = str(input("Nombre: "))
    cliente = cli(i, nombre)

    with open('clientes.pkl', 'ab') as f:
        pickle.dump(cliente, f)

    return print('Se ha creado el cliente con exito!')

def modificar_cliente():
    clientes = []
    cargar(clientes, 'clientes')

    for cliente in clientes:
        print(cliente)

    opc = int(input('Que cliente desea modificar? '))
    print(menu_modificar_cliente(opc, clientes))

def listar_clientes():
    clientes = []
    cargar(clientes, 'clientes')

    for cliente in clientes:
        print(cliente)


def menu_clientes():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear cliente")
        print("2. Modificar cliente")
        print("3. Listar clientes")
        print("0. Volver al menu principal")
        print("\nOpcion: ", end = '')
        opc = int(input())

        if opc == 0: break
        elif opc == 1: crear_cliente()
        elif opc == 2: modificar_cliente()
        elif opc == 3: listar_clientes()
        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')
        input('Presione ENTER para continuar')