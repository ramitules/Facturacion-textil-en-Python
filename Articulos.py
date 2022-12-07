import os

Articulo0 = {
    "ID" : 0,
    "Descripcion" : "Ploteo 91cm",
    "Conteo" : "Metro lineal",
    "Precio unitario" : 250
    }

Articulo1 = {
    "ID" : 1,
    "Descripcion" : "Ploteo mayor a 91cm hasta 180cm",
    "Conteo" : "Metro lineal",
    "Precio unitario" : 295
    }

Articulo2 = {
    "ID" : 2,
    "Descripcion" : "Tizada Optitex",
    "Conteo" : "Por pieza",
    "Precio unitario" : 25
    }

Articulo3 = {
    "ID" : 3,
    "Descripcion" : "Repeticion ploteo y tizada",
    "Conteo" : "Metro lineal",
    "Precio unitario" : 250
    }


all_articulos = [Articulo0, Articulo1, Articulo2, Articulo3]

def crearArticulo():
    return

def seleccionarArticulos():
    os.system("cls")
    print("Articulo?")

    for x in all_articulos:
        print(x.get('ID')," ", x.get('Descripcion'))

    print("ID: ", end = '')
    pos = int(input())

    return all_articulos[pos]