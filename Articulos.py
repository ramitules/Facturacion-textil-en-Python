class art:
	def __init__(self, id: int, desc: str, cont: str, p_u: int):
		self.ID = id
		self.descripcion = desc
		self.conteo = cont
		self.precio_unitario = p_u

	def mostrar(self):
		print(f'ID: {self.ID}, Descripcion: {self.descripcion}, Conteo: {self.conteo}, Precio unitario: {self.precio_unitario}')

	def mostrar_resumen(self):
		print(f'ID: {self.ID}, Descripcion: {self.descripcion}')

	def leer(self):
		try:
			f = open('articulos.dat','rb')
			x = f.read()
			f.close()
			return x
		except: return 'No existe el registro'

	def guardar(self):
		f = open('articulos.dat', 'ab')
		f.write(self)
		f.close()
		return "El articulo se ha guardado exitosamente"
