from Clientes import seleccionarCliente
from Articulos import *
from openpyxl import *
import os

def crearFactura():
    plantilla = load_workbook('Factura.xlsx')
    nuevaFactura = plantilla
    hoja = nuevaFactura.active

    hoja['C2'] = seleccionarCliente()
    
    for x in range(14):
        aux = agregarArticulo(x)
        
        indice = str(x+5)
        hoja['B'+indice] = aux.get("ID")
        hoja['C'+indice] = aux.get("Descripcion")
        hoja['D'+indice] = aux.get("Conteo")

        print(aux.get("Conteo"), "cantidad: ", end = "")
        cant = float(input())

        hoja['E'+indice] = cant
        hoja['F'+indice] = aux.get("Precio unitario")
        hoja['G'+indice] = cant * aux.get("Precio unitario")

        print("Agregar mas articulos?\n1.SI  2.NO: ", end = "")
        opc = int(input())
        if opc == 2: break

    os.system("cls")
    print("Que archivo se ha utilizado? ", end = "")
    archivoMRK = str(input())

    hoja['B19'] = str("Observaciones: archivo " + archivoMRK)

    os.chdir('Facturas')
    nuevaFactura.save('Factura 1.xlsx')
    os.chdir('..')

    print("Factura creada con exito")

    input("\nPresione ENTER para continuar")
    
    return