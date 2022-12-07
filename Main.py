import os
from Facturas import *

while True:
    os.system("cls")
    print("Bienvenido!\n")
    print("Elija una opcion")
    print("1. Crear factura")
    print("0. Salir")
    print("\nOpcion: ", end = '')
    opc = int(input())
    if opc == 0: break
    else: crearFactura()