from fileinput import fileno
import os
from funciones import cargar
from openpyxl import *
from tkinter import filedialog
from datetime import datetime, date

def seleccionar_mark():
    os.system("cls")
    input('A continuacion vas a poder seleccionar el archivo MARK que utilizaste. Presiona ENTER para continuar')

    try:
        os.chdir('Tizadas')
        archivo = filedialog.askopenfilename(title='Seleccionar archivo de marcada', filetypes=[('Archivo Mark','*.MRK')])
        archivoMRK1 = os.path.basename(archivo)
        archivoMRK = archivoMRK1.replace('.MRK','')
    except:
        archivoMRK = 'error'

    os.chdir('..')
    print(archivoMRK)
    return archivoMRK

def crear_factura():
    plantilla = load_workbook('Plantilla.xlsx')
    nueva_factura = plantilla
    hoja = nueva_factura.active

    fecha = date.today().strftime('%d/%m/%Y')
    hoja['G2'] = fecha

    articulos = []
    cargar(articulos, 'articulos')

    if len(articulos) == 0:
        print('No hay articulos cargados')
        return

    clientes = []
    cargar(clientes, 'clientes')

    if len(clientes) == 0:
        print('No hay clientes cargados')
        return

    print('Seleccionar cliente')
    for cliente in clientes:
        print(cliente)

    opc = int(input('Opcion: '))
    opc -= 1
    hoja['C2'] = clientes[opc].nombre

    os.chdir('..')
    os.chdir(f'Optitex\\{clientes[opc].nombre}')

    print('\nPrimer articulo')

    for x in range(13):
        indice = str(x+5)

        for articulo in articulos:
            print(articulo)

        opc = int(input('Opcion: '))
        opc -= 1

        hoja['B'+indice] = articulos[opc].ID
        hoja['C'+indice] = articulos[opc].descripcion
        hoja['D'+indice] = articulos[opc].conteo

        print(articulos[opc].conteo, end = " ")
        cant = float(input('cantidad: '))

        hoja['E'+indice] = cant
        hoja['F'+indice] = articulos[opc].precio_unitario
        hoja['G'+indice] = cant * articulos[opc].precio_unitario

        print("\nAgregar mas articulos?")
        opc = input("1.SI  2.NO: ")
        if opc == '2': break

    archivoMRK = seleccionar_mark()

    hoja['B19'] = str("Observaciones: archivo " + archivoMRK)
    os.chdir('Facturas')
    nueva_factura.save(f'{archivoMRK}.xlsx')
    os.startfile(f'{archivoMRK}.xlsx')

    while True:
        try:
            os.chdir('Facturacion')
            break
        except FileNotFoundError: os.chdir('..')

    print("Factura creada con exito")

def listar_facturas(periodo: str, fac: list, acum: float):
    ahora = datetime.now()

    if periodo == 'semanal':
        semana = ahora.isocalendar()[1]
    else:
        mes = ahora.month

    for factura in fac:
            aux = load_workbook(factura)
            hoja_aux = aux.active
            fecha_factura = str(hoja_aux['G2'])
            fecha_objeto = datetime.strptime(fecha_factura, "%d/%m/%Y")

            if periodo == 'semanal':
                semana_factura = fecha_objeto.isocalendar()[1]
                if semana_factura == semana:
                    valor = hoja_aux['G18']
                    acum += valor
                    aux.close()
            else:
                mes_factura = fecha_objeto.month
                if mes_factura == mes:
                    valor = hoja_aux['G18']
                    acum += valor
                    aux.close()

def resumen_general(periodo: str, clientes: list):
    acumular = float(0)

    for cliente in clientes:
        os.chdir(f'{cliente}\\Facturas')
        facturas = os.listdir()
        listar_facturas(facturas, periodo, acumular)

    print(f'Total {periodo} acumulado: $', acumular)

def resumen_por_cliente(periodo: str, clientes: list):
    acumular = float(0)

    for cliente in clientes:
        print(cliente)
    opc = int(input('Seleccione cliente: '))

    os.chdir(f'{cliente[opc].nombre}\\Facturas')
    facturas = os.listdir()

    listar_facturas(facturas, periodo, acumular)

    print(f'Total {periodo} acumulado, cliente {cliente[opc].nombre}: $', acumular)

def resumen(periodo: str):
    os.chdir('..')
    os.chdir('Optitex')

    clientes = []
    cargar(clientes, 'clientes')

    print(f'1. Resumen {periodo} general')
    print(f'2. Resumen {periodo} por cliente')
    print('0. Volver\n')
    opc = input('Opcion: ')

    if opc == '1': resumen_general(periodo, clientes)
    elif opc == '2': resumen_por_cliente(periodo, clientes)
    else: return