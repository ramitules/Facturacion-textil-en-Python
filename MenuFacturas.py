import os
from funciones import *
from Facturas import crear_factura

def menu_facturas():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear factura")
        print("0. Volver al menu principal")
        print("\nOpcion: ", end = '')
        opc = int(input())

        if opc == 0: break
        elif opc == 1: crear_factura()
        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')