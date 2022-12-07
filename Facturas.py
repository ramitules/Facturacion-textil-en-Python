from Clientes import seleccionarCliente
from Articulos import seleccionarArticulos
from openpyxl import *
import os

def crearFactura():
    plantilla = load_workbook('Factura.xlsx')
    nuevaFactura = plantilla
    hoja = nuevaFactura.active

    hoja['C2'] = seleccionarCliente()
    
    aux = seleccionarArticulos()
    hoja['B5'] = aux.get("ID")
    hoja['C5'] = aux.get("Descripcion")
    hoja['D5'] = aux.get("Conteo")

    print(aux.get("Conteo"), "cantidad: ", end = "")
    cant = float(input())

    hoja['E5'] = cant
    hoja['F5'] = aux.get("Precio unitario")
    hoja['G5'] = cant * aux.get("Precio unitario")

    os.system("cls")
    print("Que archivo se ha utilizado? ", end = "")
    archivoMRK = str(input())
    hoja['B19'] = str("Observaciones: archivo " + archivoMRK)
    
    nuevaFactura.save('Factura 1.xlsx')
    return 
