import sys
from openpyxl import *
from Articulos import art

def cantidad(archivo: str):
    try:
        f = open(f'{archivo}.dat', 'rb')
        cont = f.read()
        cant = len(cont) / sys.getsizeof(art)
        return int(cant)
    except: return int(0)

def crear_articulo():
    i = cantidad('articulos')
    desc = str(input("Descripcion: "))
    cont = str(input("Conteo: "))
    p_u = int(input("Precio unitario: "))
    art(i, desc, cont, p_u).guardar()

def modificar_articulo():
    return 0

def listar_articulos():
    return 0

def crear_factura():
    return 0

#def crearFactura():
#    plantilla = load_workbook('Factura.xlsx')
#    nuevaFactura = plantilla
#    hoja = nuevaFactura.active

#    hoja['C2'] = seleccionarCliente()
    
#    for x in range(14):
#        aux = agregarArticulo(x)
        
#        indice = str(x+5)
#        hoja['B'+indice] = aux.get("ID")
#        hoja['C'+indice] = aux.get("Descripcion")
#        hoja['D'+indice] = aux.get("Conteo")

#        print(aux.get("Conteo"), "cantidad: ", end = "")
#        cant = float(input())

#        hoja['E'+indice] = cant
#        hoja['F'+indice] = aux.get("Precio unitario")
#        hoja['G'+indice] = cant * aux.get("Precio unitario")

#        print("Agregar mas articulos?\n1.SI  2.NO: ", end = "")
#        opc = int(input())
#        if opc == 2: break

#    os.system("cls")
#    print("Que archivo se ha utilizado? ", end = "")
#    archivoMRK = str(input())

#    hoja['B19'] = str("Observaciones: archivo " + archivoMRK)

#    os.chdir('Facturas')
#    nuevaFactura.save('Factura 1.xlsx')
#    os.chdir('..')

#    print("Factura creada con exito")

#    input("\nPresione ENTER para continuar")
    
#    return