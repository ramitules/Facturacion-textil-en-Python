class Cantidades:
    def __init__(self):
        self.art = int(0)
        self.cli = int(0)
        self.fac = int(0)

    def leer():
        try:
            f = open('cantidades.dat','rb')
            self = f.read()
            f.close()
            return self
        except:
            f = open('cantidades.dat','wb')
            f.write(self)
            f.close()
            return self

    def guardar(self):
        f = open('cantidades.dat', 'wb')
        f.write(self)
        f.close()

    def articulos(self):
        self.art += 1

    def clientes(self):
        self.cli += 1

    def facturas(self):
        self.fac += 1