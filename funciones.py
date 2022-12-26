import pickle

def cargar(lista: list, clase: str):
    with open(f'{clase}.pkl', 'rb') as f:
        while True:
            try:
                x = pickle.load(f)
                lista.append(x)
            except EOFError: break
    return

def menu_modificar_cliente(opc: int, cl: list):
    while True:
        print('1. Cambiar nombre',
                '\n2. ELIMINAR',
                '\n0. Volver')
        opc2 = int(input('Seleccione opcion: '))
        if opc2 == 0: return

        elif opc2 == 1:
            cl[opc].nombre = input('Nombre: ')
            break

        elif opc2 == 2:
            print('Seguro que desea eliminar el cliente?')
            x = int(input('1.SI - 2.NO: '))
            if x == 1:
                del cl[opc]
                input('El cliente se ha eliminado con exito, presione ENTER para continuar')
                break

        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')

    with open('clientes.pkl', 'wb') as f:
        for cliente in cl:
            pickle.dump(cliente, f)
    return 'El cliente se ha modificado con exito!'

def menu_modificar_articulos(opc: int, art: list):
    while True:
        print('1. Cambiar descripcion',
                '\n2. Cambiar conteo',
                '\n3. Cambiar precio unitario',
                '\n4. ELIMINAR',
                '\n0. Volver')
        opc2 = int(input('Seleccione opcion: '))
        if opc2 == 0: return

        elif opc2 == 1:
            art[opc].descripcion = input('Descripcion: ')
            break

        elif opc2 == 2:
            art[opc].conteo = input('Conteo: ')
            break

        elif opc2 == 3:
            art[opc].precio_unitario = int(input('Precio unitario: $'))
            break

        elif opc2 == 4:
            print('Seguro que desea eliminar el articulo?')
            x = int(input('1.SI - 2.NO: '))
            if x == 1:
                del art[opc]
                input('El articulo se ha eliminado con exito, presione ENTER para continuar')
                break

        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')

    with open('articulos.pkl', 'wb') as f:
        for articulo in art:
            pickle.dump(articulo, f)
    return 'El articulo se ha modificado con exito!'
