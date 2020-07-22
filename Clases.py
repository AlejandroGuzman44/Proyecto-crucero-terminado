class Pasajeros:

	def __init__(self , nombre , edad , documento , barco , pago_boleto , pago , descuento , impuesto , discapacidad , habitacion):

		self.nombre = nombre 
		self.edad = edad 
		self.documento = documento
		self.barco = barco 
		self.pago_boleto = pago_boleto
		self.pago = pago
		self.descuento = descuento
		self.impuesto = impuesto
		self.discapacidad = discapacidad
		self.habitacion = habitacion

	def mirar(self):

		return (f"Nombre : {self.nombre} \n Edad : {self.edad} \n Documento : {self.documento} \n Barco : {self.barco} \n Habitacion : {self.habitacion} \n Discapacidad : {self.discapacidad} \n Pago boleto : {self.pago_boleto} \n Pago total : {self.pago} \n Descuento : {self.descuento} \n Impuestos : {self.impuesto} ")



class Alimento :

	def __init__(self , clasificacion , nombre , tipo , precio):
		self.clasificacion = clasificacion 
		self.nombre = nombre
		self.tipo = tipo
		self.precio = precio

	def mirar(self):
		return(f" clasificacion : {self.clasificacion} \n Nombre : {self.nombre} \n Tipo : {self.tipo} \n Precio : {self.precio}")


class Bebida():

	def __init__(self , clasificacion , nombre , tamanio , precio):
		self.clasificacion = clasificacion
		self.nombre = nombre
		self.tamanio = tamanio
		self.precio = precio

	def mirar(self):
		return(f"clasificacion : {self.clasificacion} \n Nombre : {self.nombre} \n Tamanio : {self.tamanio} \n Precio : {self.precio}")

class Combo():

	def __init__(self , nombre , productos , precio):
		self.nombre = nombre
		self.productos = productos
		self.precio = precio

	def mirar(self):
		return(f"Nombre : {self.nombre} \n Productos : {self.productos} \n Precio : {self.precio}")


class Puerto:

	def __init__(self , tipo , precio , cantidad , hora , dni):
		self.tipo = tipo
		self.precio = precio
		self.cantidad = cantidad
		self.hora = hora
		self.dni = dni
	
	def mirar(self):
		return(f"Tipo : {self.tipo} \n Dni : {self.dni} \n Precio : {self.precio} \n Cantidad : {self.cantidad} \n Hora : {self.hora}")


class Comida:

	def __init__(self , tipo , dni , precio , cantidad , hora):
		self.tipo = tipo
		self.dni = dni
		self.precio = precio
		self.cantidad = cantidad
		self.hora = hora
		
	
	def mirar(self):
		return(f"Tipo : {self.tipo} \n Dni : {self.dni} \n Precio : {self.precio} \n Cantidad : {self.cantidad} \n Hora : {self.hora}")


class Trotar:

	def __init__(self , tipo , dni , precio , cantidad , hora):
		self.tipo = tipo 
		self.dni = dni
		self.precio = precio
		self.cantidad = cantidad
		self.hora = hora
	
	def mirar(self):
		return(f"Tipo : {self.tipo} Dni : {self.dni} \n Precio : {self.precio} \n Cantidad : {self.cantidad} \n Hora : {self.hora}")
 

class Visita:

	def __init__(self , tipo , dni , precio , cantidad , hora):
		self.tipo = tipo 
		self.precio = precio
		self.cantidad = cantidad
		self.hora = hora
		self.dni = dni

	def mirar(self):
		return(f"Tipo : {self.tipo} \n Dni : {self.dni} \n Precio : {self.precio} \n Cantidad : {self.cantidad} \n Hora : {self.hora}")