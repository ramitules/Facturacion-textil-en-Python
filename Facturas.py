import os
from funciones import *
from openpyxl import *
from tkinter import filedialog
from MenuClientes import listar_clientes
from MenuArticulos import listar_articulos

def crear_factura():
    plantilla = load_workbook('Plantilla.xlsx')
    nueva_factura = plantilla
    hoja = nueva_factura.active

    print('Seleccionar cliente')
    listar_clientes()
    opc = int(input('Opcion: '))

    clientes = []
    cargar(clientes, 'clientes')
    hoja['C2'] = clientes[opc].nombre

    print('\nPrimer articulo')
    for x in range(14):
        listar_articulos()
        opc = int(input('Opcion: '))

        indice = str(x+5)
        articulos = []
        cargar(articulos, 'articulos')

        hoja['B'+indice] = articulos[opc].ID
        hoja['C'+indice] = articulos[opc].descripcion
        hoja['D'+indice] = articulos[opc].conteo

        print(articulos[opc].conteo, end = " ")
        cant = float(input('cantidad: '))

        hoja['E'+indice] = cant
        hoja['F'+indice] = articulos[opc].precio_unitario
        hoja['G'+indice] = cant * articulos[opc].precio_unitario

        print("\nAgregar mas articulos?")
        opc = int(input("1.SI  2.NO: "))
        if opc == 2: break

    os.system("cls")
    input('A continuacion vas a poder seleccionar el archivo MARK que utilizaste. Presiona ENTER para continuar')
    archivo = filedialog.askopenfilename(title='Seleccionar archivo de marcada', filetypes=[('Archivo Mark','*.MRK')])
    archivoMRK = os.path.basename(archivo)
    print(archivoMRK.replace('.MRK',''))

    hoja['B19'] = str("Observaciones: archivo " + archivoMRK)

    os.chdir('Facturas')
    facturas = os.listdir()
    indice = str(len(facturas) + 1)
    nueva_factura.save(f'Factura {indice}.xlsx')
    os.chdir('..')

    print("Factura creada con exito")

    input("\nPresione ENTER para continuar")
    return 0