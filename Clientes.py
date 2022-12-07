import os

clientes = ["Yaco", "Rosa", "Vete al Diablo", "Cecilia"]

def seleccionarCliente():
    os.system("cls")
    print("Cliente?")

    for x in range(len(clientes)):
        print(x," ", clientes[x])

    print("Opcion: ", end = '')
    pos = int(input())

    return clientes[pos]