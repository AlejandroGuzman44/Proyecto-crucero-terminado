import requests
from Clases import *

habitaciones = [['SA1' , 'SA2' , 'SA3' , 'SA4' , 'SA5' , 'SA6' , 'SA7' , 'SA7' , 'SA8' , 'SA9' , 'SA10'],
								['PB1' , 'PB2' , 'PB3' , 'PB4' , 'PB5' , 'PB6' , 'PB7' , 'PB7' , 'PB8' , 'PB9' , 'PB10'],
								['VC1' , 'VC2' , 'VC3' , 'VC4' , 'VC5' , 'VC6' , 'VC7' , 'VC7' , 'VC8' , 'VC9' , 'VC10']]



menu = []
menu_combos = []
pasajeross = []

def restaurante():

    '''
    La finalidad de esta funcion es mostrar al cliente todas las cosas que este uede hacer en el restaurante
    '''

	while True :

		print(''' \n Bienvenido al menu del restaurante del crucero que desea hacer ? 

				1) Agregar plato al menu
				2) Eliminar plato del menu 
				3) Modificar productos del menu   
				4) Ver menu
				5) Agregar combo a menu combos
				6) Eliminar combo de menu de combos 
				7) Ver menu de combos
				8) Buscar producto por nombre o rango de precio 
				9) Buscar combo por nombre o rango de precio 
	
				''')


		pregunta = input("\n Que desea hacer ? : ")
		while not pregunta.isnumeric() or (int(pregunta) not in range(1,10)):
			pregunta = input("\n Ingrese un valor valido por favor : ")
		
		if pregunta == '1':
			agregar_plato(menu)
		elif pregunta == '2':
			if len(menu) == 0 :
				print("\n No hay ningun plato registrado aun ")
			else:
				eliminar_producto(menu)
		elif pregunta == '3':
			modificar_menu(menu)
		elif pregunta == '4':
			ver_menu(menu)
		elif pregunta == '5':
			agregar_combo(menu_combos)
		elif pregunta == '6':
			if len(menu_combos) == 0:
				print("\n No hay ningun combo registrado aun ")
			else:
				eliminar_combo(menu_combos)
		elif pregunta == '7':
			if len(menu_combos) == 0:
				print("\n No hay ningun combo registrado aun ")
			else:
				ver_combo(menu_combos)
		elif pregunta == '8':
			buscar_producto(menu)



def agregar_plato(menu):

    '''
    La finalidad de esta funcion es permitir agregar un plato al menu
    '''

	clasificacion = input("\n Es de tipo Alimento(1) o de tipo Bebida(2) ? : ")
	while not clasificacion.isnumeric() or (int(clasificacion) not in range(1,3)):
		clasificacion = input("\n Disculpe , debe de ingresar valores validos ")

	if clasificacion == '1':

		clasificacion = "Alimento"

		nombre = input("\n Cual es el nombre del alimento ? : ").upper()
		while not nombre.isalpha():
			nombre = ("\n Ingrese un nombre valido : ").upper()

		tipo = input("\n Ingrese el tipo de su alimento , Empaque(1) o Preparacion(2) : ")
		while not tipo.isnumeric() or (int(tipo) not in range(1,3)):
			tipo = input("\n Ingrese valores validos : ")

		if tipo == '1':
			tipo = "Empaque"
		elif tipo == '2':
			tipo = "Preparacion"

		monto = input("\n Ingrese el precio del alimento : ")
		while not monto.isnumeric() :
			monto = input("\n Ingrese un monto valido : ")

		precio = int(monto) + int(monto) * 0.16

		with open("Alimentos.txt" , "a+") as bd:
			bd.write(f"{clasificacion} ,{nombre} ,{tipo} ,{precio}\n ")

		alimento = Alimento(clasificacion , nombre , tipo , precio)

		menu.append(alimento)

		return alimento

	elif clasificacion == '2':

		clasificacion = "Bebida"

		nombre = input("\n Ingrese el nombre de su bebida : ").upper()
		while not nombre.isalpha():
			nombre = input("\n Ingrese un nombre valido : ").upper()

		tamanio = input("\n De que tamanio es su bebida ? Pequenia(1) , Mediana(2) , Grande(3) ? : ")
		while not tamanio.isnumeric() or (int(tamanio) not in range(1,4)):
			tamanio = input("\n Ingrese un valor valido por favor : ")

		if tamanio == '1':
			tamanio = "Pequenia"
		elif tamanio == '2':
			tamanio = "Mediana"
		elif tamanio == '3':
			tamanio = "Grande"

		monto = input("\n Ingrese el precio de la bebida : ")
		while not monto.isnumeric():
			monto = input("\n Ingrese un monto valido : ")

		precio = int(monto) + int(monto) * 0.16

		with open("Alimentos.txt" , "a+") as bd:
			bd.write(f"{clasificacion} , {nombre} ,{tamanio} ,{precio} \n ")


		bebida = Bebida(clasificacion , nombre , tamanio , precio)

		menu.append(bebida)

		return bebida


def eliminar_producto(menu):

    '''
    La finalidad de esta funcion es permitir un plato que este registrado en el menu
    '''

	nombre = input("\n Ingrese el nombre del producto que quiere eliminar del menu : ").upper()

	for x in menu:
		if x.nombre == nombre:
			menu.remove(x)
			print("\n Producto eliminado exitosamente")
		if x.nombre != nombre:
			print("\n El nombre ingresado no coincide con ningun producto registrado")


	for x in menu:

		with open("Alimentos.txt" , "w") as bd:
			datos = bd.write(str(x))
		print (datos)




def ver_menu(menu):

    '''
    La finalidad de esta funcion es permitir ver los platos registrados en el menu
    '''

	with open("Alimentos.txt" , "r") as bd:
		datos = bd.readlines()
		for x in datos:
			print(x)


def modificar_menu(menu):

    '''
    La finalidad de esta funcion es permtir modificar un plato que este en el menu
    '''

	opcion = input("\n Que desea modificar (1)Alimento , (2)Bebida ? : ")
	while not opcion.isnumeric() or (int(opcion) not in range(1,3)):
		opcion = input("\n Ingrese valores validos : ")

	if opcion == '1':
		i =1
		for alimento in menu:
			print(i , alimento.mirar())
			i+=1

		modificar = input("\n Ingrese el nombre del alimento que desea modificar : ").upper()
		for alimento in menu:
			if alimento.nombre == modificar:

				print('''Que desea modificar 

						1) Nombre 
						2) tipo
						3) Precio
				
				
					''')

				op = input("\n Cual desea modificar ? : ")
				while not op.isnumeric() or (int(op) not in range(1,4)):
					op = input("\n Ingrese valores validos : ")

				if op == '1':
					alimento.nombre = input("\n Ingrese el nuevo nombre : ")
				elif op == '2':
					alimento.tipo = input("\n Ingrese el nuevo tipo : ")
				elif op == '3':
					alimento.precio = input("\n Ingrese el nuevo precio : ")
				
				print(alimento.mirar())
			
			elif alimento.nombre() != modificar:
				print("\n Disculpe ese alimento no existe")
			
	elif opcion == '2':

		i = 1
		for bebida in menu:
			print(i , bebida.mirar())
			i += 1
		modificar = input("\n Ingrese el nombre de la bebida a modificar : ").upper()

		for bebida in menu:
			if bebida.nombre == modificar:

				print('''

					1) Nombre 
					2) Tamanio 
					3) precio
				
					''')

				op = input("\n Que desea modificar ? : ")
				while not op.isnumeric() or (int(op) not in range(1,4)):
					op = input("\n Ingrese valores validos : ")

				if op == '1':
					bebida.nombre = input("\n Ingrese el nuevo nombre de la bebida : ")
				elif op == '2':
					bebida.tamanio = input("\n Ingrese el tamanio de la bebida (1)Grande , (2)Mediana , (3)Pequenia : ")
					if bebida.tamanio == '1':
						bebida.tamanio = "Grande"
					elif bebida.tamanio == '2':
						bebida.tamanio = "Mediana"
					elif bebida.tamanio == '3':
						bebida.tamanio = "Pequenia"
				elif op == '3':
					bebida.precio = input("\n Ingrese el nuevo precio : ")

			elif bebida.nombre != modificar:
				print("\n Disculpe esa bebida no esta registrada")

	

def agregar_combo(menu_combos):

    '''
    La finalidad de esta funcion es permitir agregar un plato al menu de combos
    '''

	nombre = input("\n Ingrese el nombre del combo : ").upper()
	while not nombre.isalpha():
		nombre = input("\n Ingrese un nombre valido : ").upper()

	productos = input("\n Ingrese los productos del combo , minimo 2 productos : ")

	monto = input("\n Ingrese el precio del combo : ")
	while not monto.isnumeric():
		monto = input("\n Ingrese un monto valido : ")

	precio = int(monto) + int(monto) * 0.16

	with open("Combos.txt" , "a+") as bd:
		bd.write(f"nombre : {nombre} , productos : {productos} , precio : {precio} \n ")

	combo = Combo(nombre , productos , precio)

	menu_combos.append(combo)

	return combo


def eliminar_combo(menu_combos):

    '''
    La finalidad de esta funcion es permitir eliminar un plato del menu de combos
    '''

	nombre = input("\n Ingrese el nombre del combo que desea eliminar : ").upper()

	for x in menu_combos:
		if x.nombre == nombre:
			menu_combos.remove(x)
			print("\n Combo eliminado exitosamente")
		if x.nombre != nombre:
			print("\n El nombre ingresado no coincide con ninguno de los combos ")


def ver_combo(menu_combos):

    '''
    La finalidad de esta funcion es mostrar todos los platos registrados hasta el mometo
    '''

	with open("Combos.txt" , "r") as bd:
		datos = bd.readlines()
		for x in datos:
			print(x)	
		

def modificar_menu_combo(menu_combos):

    '''
    La finalidad de esta funcion es modificar los platos que estan registrados en el menu de combos
    '''

	i = 1
	for combo in menu_combos:
		print(i , combo.mirar())
		i += 1

	modificar = input("\n Ingresa el nombre del alimento que desea modificar : ").upper()

	for combo in menu_combos:
		if combo.nombre == modificar:

			print(''' Que desea modificar ?

				1) Nombre 
				2) Productos 
				3) Precio
			
				''')
			
			op = input("\n Que atributo desea modificar ? : ")
			while not op.isnumeric() or (int(op) not in range(1,4)):
				op = input("\n Ingrese valores validos : ")

			if op == '1':
				combo.nombre = input("\n Ingrese el nuevo nombre del combo :")
			elif op == '2':
				combo.productos = input("\n Ingrese los productos : ")
			elif op == '3':
				combo.precio = input("\n Ingrese el nuevo precio : ")


def buscar_producto(menu):

    '''
    La finalidad de esta funcion es permitirle al cliente que busque un plato introduciendo su nombre 
    o un rango de precio
    '''


	pregunta = input("\n Desea buscar por (1)Nombre o (2)Rango de precio ? : ")

	while not pregunta.isnumeric() or (int(pregunta) not in range(1,3)):
		pregunta = input("\n Ingrese valores validos : ")

	if pregunta == '1':

		nombre = input("Ingrese el nombre del producto que desea buscar : ").upper()

		with open("Alimentos.txt" , "r") as bd:
			datos = bd.readlines

		comida = datos[:-1].split(",")
		if comida[1] == nombre:
			return Alimento(comida[0] , comida[1] , comida[2] , comida[3])
		

	elif pregunta == '2':

		precio_menor = input("\n Ingrese el rango de precio que desea buscar : ")
		precio_mayor = input("\n Ingrese el precio : ")

		for alimento in menu:
			if precio_menor < alimento.precio < precio_mayor:
				print(alimento.mirar())



puertos = []
comidas = []
trotars = []
visitas = []

contador_no = 0


def tour():
	'''
	Esta funcion es para cuando una persona selecciona la opcion de ver los tours disponibles , esta funcion
	le da la informacion de la cantidad de tours que hay disponibles 
	'''

	global contador_no

	while True: 
	
		pregunta = input(''' Bienvenido al crucero Saman Caribbean , que tipo de tour le interesa ?

			1) Tour en el puerto
			2) Degustacion de comida local 
			3) Trotar por el pueblo\ciudad 
			4) Visita a lugares historicos
			5) No comprar ninguno

		> ''')

		while not pregunta.isnumeric() or (int(pregunta) not in range(1,6)):
			pregunta = input("\n Ingrese una opcion valida : ")

		if pregunta == '1':
			tour_puerto(puertos)
		elif pregunta == '2':
			degustar_comida(comidas)
		elif pregunta == '3':
			tour_trotar(trotars)
		elif pregunta == '4':
			tour_visita(visitas)
		elif pregunta == '5':
			duda = input("\n Disculpe , cuantas personas son? es para ccalcular unos porcentajes : ")
			while not duda.isnumeric():
				duda = input("\n Ingrese valores validos :")
			contador_no += int(duda)
			main()
			

contador_puerto = 0

def tour_puerto(puertos):

	'''
	Cuando una persona selecciona la opcion de tour por el puerto , entonces se le pasa a esta funcion 
	que tiene como finalidad pedir los datos de las personas que desean realizar el tour
	'''

	global contador_puerto


	tipo = "Tour en el puerto"

	dni = input("\n Ingrese su dni : ")

	while not dni.isnumeric():
		dni = input("\n Ingrese valores validos : ")

	

	cantidad = input("\n Cuantas personas son ? : ")
	precio = int(cantidad) * 30


	contador_puerto += int(cantidad)
	

	while contador_puerto > 10:
		print("\n Disculpe este tour tiene una capacidad maxima de 10 personas y ya alcanzamos ese limite ")
		break
	print(contador_puerto)


	if cantidad == '4':
		precio = precio - (precio*0.3)


	while not cantidad.isnumeric() or (int(cantidad) not in range(1,5)):
		cantidad = input("\n Disculpe , maximo pueden ser 4 personas , y debe de ingresar numeros : ")

	hora = "7 A.M"

	puerto = Puerto(tipo , precio , cantidad , hora , dni)

	puertos.append(puerto)

	for x,y in enumerate(puertos):
		print("-----" , x+1 , "----------------")
		print(y.mirar())

	return puerto


contador_comida = 0

def degustar_comida(comidas):

	'''
	Cuando una persona selecciona la opcion del tour de degustar comida , entonces se le pasa a esta funcion 
	que tiene como finalidad pedir los datos de las personas que desean realizar el tour
	'''

	global contador_comida

	tipo = "Degustacion de comida local"

	dni = input("\n Ingrese su dni : ")

	while not dni.isnumeric() :
		dni = input("\n Ingrese valores validos : ")

	cantidad = input("\n Cuantas personas son ? : ")

	contador_comida += int(cantidad)
	

	while contador_comida > 100:
		print("\n Disculpe el cupo total es de 100 personas y ya alcanzamos ese limite")
		break
	
	precio = int(cantidad) * 100

	while not cantidad.isnumeric() or (int(cantidad) > 2):
		cantidad = input("\n Disculpe , solo se pueden dos personas , ingrese solo numeros : ")

	hora = "12 P.M"

	comida = Comida(tipo , dni , precio , cantidad , hora)

	comidas.append(comida)

	for x,y in enumerate(comidas):
		print("-----", x+1, "----------------")
		print(y.mirar())

	return comida


contador_trotar = 0

def tour_trotar(trotars):

	'''
	Cuando una persona selecciona la opcion del tour de trotar , entonces se le pasa a esta funcion 
	que tiene como finalidad pedir los datos de las personas que desean realizar el tour
	'''

	global contador_trotar

	tipo = "Trotar por el pueblo\ciudad"

	dni = input("\n Ingrese su dni : ")

	while not dni.isnumeric():
		dni = input("\n Ingrese valores validos : ")

	cantidad = input("\n Cuantas personas son ? : ")
	contador_trotar += int(cantidad)
	
	
	precio = "Gratuito"

	hora = "6 A.M"

	trotar = Trotar(tipo , dni , precio , cantidad , hora)

	trotars.append(trotar)

	for x,y in enumerate(trotars):
		print("-----" , x+1 , "----------------")
		print(y.mirar())

	return trotar


contador_visita = 0

def tour_visita(visitas):

	'''
	Cuando una persona selecciona la opcion del tour de visita , entonces se le pasa a esta funcion 
	que tiene como finalidad pedir los datos de las personas que desean realizar el tour
	'''

	global contador_visita

	tipo = "Visita a lugares historicos"

	dni = input("\n Ingrese su dni : ")

	while not dni.isnumeric():
		dni = input("\n Ingrese valores validos : ")

	cantidad = input("\n Cuantas personas son ? : ")

	contador_visita += int(cantidad)
	

	while contador_visita > 15:
		print("\n Discule la cantidad de cupos es de 15 personas y ya alcanzamos ese limite")
		break

	precio = int(cantidad) * 40

	if cantidad == '3':
		precio = precio - (precio*0.1)
	if cantidad == '4':
		precio = precio - (precio*0.2)
	

	while not cantidad.isnumeric() or (int(cantidad) not in range(1,5)):
		cantidad = input("\n Revise sus datos , algo puso mal : ")

	hora = "10 A.M"

	visita = Visita(tipo , dni , precio , cantidad , hora)

	visitas.append(visita)

	for x,y in enumerate(visitas):
		print("-----" , x+1 , "----------------")
		print(y.mirar())
	
	return visita



hab = []
compraron = 0
no_compraron = 0

def ver_barcos():

	'''
	La finalidad de esta funcion es presentarle a los potenciales clientes los cruceros que se encuentran disponibles , informacion
	que se saca de una Api dada, tambien esta funcion le pregunta al cliente si desea comprar una habitacion y en que crucero
	que crucero desea. 
	'''

	global compraron , no_compraron

	print("\n Bienvenido a Saman Caribean ")

	url = requests.get("https://saman-caribbean.vercel.app/api/cruise-ships")

	dic = url.json()

	print("\n Estos son los barcos disponibles ")


	for i , barcos in enumerate(dic):
		print(f" {i+1} {dic[i]['name']}")

	compra = input("\n Desea comprar un ticket para algun crucero ? (1)Si , (2)No : ")
	while not compra.isnumeric() or (int(compra) not in range(1,3)):
		compra = input("\n Ingrese valores validos : ")

	if compra == '1':

		pregunta = input("\n Cual crucero desea comprar ? :")
		while not pregunta.isnumeric() or (int(pregunta) not in range(1,5)):
			pregunta = input("\n Ingrese valores validos : ")

		barco_seleccionado = dic[int(pregunta)-1]

		print(f''' 

		Nombre : {barco_seleccionado['name']}
		Ruta : {barco_seleccionado['route']}
		Salida : {barco_seleccionado['departure']}
		Habitacion simple : {barco_seleccionado['cost']['simple']}$ , Cupo para {barco_seleccionado['capacity']['simple']} personas
		Habitacion premium : {barco_seleccionado['cost']['premium']}$ , Cupo para {barco_seleccionado['capacity']['premium']} personas
		Habitacion Vip : {barco_seleccionado['cost']['vip']}$ , Cupo para {barco_seleccionado['capacity']['vip']} personas

		''')
	
		tipo = input("\n Que tipo de habitacion desea ? (1)Simple , (2)Premium , (3)Vip : ")
		while not tipo.isnumeric() or (int(tipo) not in range(1,4)):
			tipo = ("\n Ingrese valores validos : ")	

		if tipo == '1':

			print(f''' Usted ha seleccionado la habitacion Simple , esto es lo que le ofrece

			1) Costo : {barco_seleccionado['cost']['simple']}$
			2) Cupo : {barco_seleccionado['capacity']['simple']} personas
		
			''')

			barco = barco_seleccionado['name']

			cantidad = input("\n Cuantas personas son ? : ")
			while not cantidad.isnumeric():
				cantidad = input("\n Ingrese valores validos : ")

			compraron += int(cantidad)


			for x in habitaciones:
				for y in x:
					print(y , end= " | ")
				print("\t")

			letra = int(input("\n Diga la habitacion que desea comprar (1)SA , (2)PB , (3)VC : "))
			while letra not in range(1,4):
				letra = int(input("\n Ingrese valores validos : "))
			numero = int(input("\n Diga el numero de la habitacion que desea : "))
			while numero not in range(1,11):
				numero = input("\n Ingrese valores validos : ")
			
			if letra == '1':
				letra = 0
			elif letra == '2':
				letra = 1
			elif letra == '3':
				letra = 2

			habitacion = habitaciones[letra - 1][numero - 1]
			hab.append(habitacion)
			print(habitacion)
			print(hab)

			if int(cantidad) <= barco_seleccionado['capacity']['simple']:

				for i in range(int(cantidad)):
	
					nombre = input("\n Ingrese su nombre : ")
					while not nombre.isalpha():
						nombre = input("\n Ingrese valores validos : ")
			
					documento = input("\n Ingrese su cedula de identidad : ")
					while not documento.isnumeric():
						documento = input("\n Ingrese valores validos : ")

					
					pago_boleto = barco_seleccionado['cost']['simple']

					impuesto = pago_boleto * 0.16

					discapacidad = input("\n Tiene alguna discapacidad ? (1)Si , (2)No :")
					while not discapacidad.isnumeric() or (int(discapacidad) not in range(1,3)):
						discapacidad = input("\n Ingrese valores validos : ")
			
					if discapacidad == '1':
						discapacidad = "Discapacitado"
						pago_discapacidad = pago_boleto*0.3
						descuento_discapacidad = 30
					else :
						discapacidad = "No discapacitado"
						pago_discapacidad = 0
						descuento_discapacidad = 0
				

					contador = 0 

					for i in range(1,int(documento) + 1):
						if int(documento) % i == 0 : 
							contador += 1
					if contador == 2:
						pago_primo = pago_boleto*0.1
						descuento_primo = 10
					else :
						pago_primo = 0
						descuento_primo = 0


					count = 1
					suma = 0 

					while (count< int(documento)):
						if (int(documento) % count == 0):
							suma += count
						count = count + 1
					if (suma>int(documento)):
						pago_abundante = pago_boleto*0.15
						descuento_abundante = 15
					else :
						pago_abundante = 0
						descuento_abundante = 0


					pago = pago_boleto - (pago_primo + pago_abundante + pago_discapacidad)
					descuento = descuento_primo + descuento_abundante + descuento_discapacidad
			
					edad = input("\n Ingrese su edad : ")
					while not edad.isnumeric() or int(edad) == 0:
						edad = input("\n Ingrese valores validos : ")

					if int(edad) >= 65:
						duda = input("\n Usted es mayor de edad , por lo cual puede cambiar su habitacion por una premium , desea hacerlo ? (1)Si , (2)No : ")
						while not duda.isnumeric() or (int(duda) not in range(1,3)):
							duda = input("\n Ingrese valores validos : ")

						if duda == '1':

							for x in habitaciones:
								for y in x:
									print(y , end= " | ")
								print("\t")

							letra = int(input("\n Diga la habitacion que desea comprar (1)SA , (2)PB , (3)VC : "))
							while letra == 1 or letra == 3:
								letra = int(input("\n Disculpe , tiene que seleccionar la opcion 2 , ya que es la habitacion premium : "))
							numero = int(input("\n Diga el numero de la habitacion que desea : "))
							while numero not in range(1,11):
								numero = input("\n Ingrese valores validos : ")
			
							if letra == '2':
								letra = 1

							habitacion = habitaciones[letra - 1][numero - 1]
							hab.append(habitacion)
							print(habitacion)
							print(hab)

						elif duda == '2':
							print("\n De acuerdo")
							

					with open("Pasajeros.txt" , "a+") as bd:
						bd.write(f" Nombre :{nombre} | Edad :{edad} | Documento :{documento} | Discapacidad :{discapacidad} | Barco :{barco} | Pago boleto :{pago_boleto} | Pago total :{pago} | Descuento :{descuento}% | Impuestos :{impuesto} | Habitacion :{habitacion} \n ")

					with open("Pasajeros.txt" , "r") as bd:
						datos = bd.readlines()
						for i,dato in enumerate(datos):
							print(f"{i+1} {dato}")

					
	
			elif int(cantidad) > barco_seleccionado['capacity']['simple']:
				print("\n No se puede")

		
		elif tipo == '2':

			print(f''' Usted ha seleccionado la habitacion Premium , esto es lo que le ofrece

			1) Costo : {barco_seleccionado['cost']['premium']}$
			2) Cupo : {barco_seleccionado['capacity']['premium']} personas
		
			''')

			barco = barco_seleccionado['name']

			cantidad = input("\n Cuantas personas son ? : ")
			while not cantidad.isnumeric():
				cantidad = input("\n Ingrese valores validos : ")

			compraron += int(cantidad)


			for x in habitaciones:
				for y in x:
					print(y , end= " | ")
				print("\t")

			letra = int(input("\n Diga la habitacion que desea comprar (1)SA , (2)PB , (3)VC : "))
			while letra not in range(1,4):
				letra = input("\n Ingrese valores validos : ")
			numero = int(input("\n Diga el numero de la habitacion que desea : "))
			while numero not in range(1,11):
				numero = input("\n Ingrese valores validos : ")
			
			if letra == '1':
				letra = 0
			elif letra == '2':
				letra = 1
			elif letra == '3':
				letra = 2

			habitacion = habitaciones[letra - 1][numero - 1]
			hab.append(habitacion)
			print(habitacion)
			print(hab)

			if int(cantidad) <= barco_seleccionado['capacity']['premium']:

				for i in range(int(cantidad)):
	
					nombre = input("\n Ingrese su nombre : ")
					while not nombre.isalpha():
						nombre = input("\n Ingrese valores validos : ")
			
					documento = input("\n Ingrese su cedula de identidad : ")
					while not documento.isnumeric():
						documento = input("\n Ingrese valores validos : ")

					
					pago_boleto = barco_seleccionado['cost']['premium']

					impuesto = pago_boleto * 0.16

					discapacidad = input("\n Tiene alguna discapacidad ? (1)Si , (2)No :")
					while not discapacidad.isnumeric() or (int(discapacidad) not in range(1,3)):
						discapacidad = input("\n Ingrese valores validos : ")
			
					if discapacidad == '1':
						discapacidad = "Discapacitado"
						pago_discapacidad = pago_boleto*0.3
						descuento_discapacidad = 30
					else :
						discapacidad = "No discapacitado"
						pago_discapacidad = 0
						descuento_discapacidad = 0
				

					contador = 0 

					for i in range(1,int(documento) + 1):
						if int(documento) % i == 0:
							contador += 1
							if contador == 2:
								pago_primo = pago_boleto*0.1
								descuento_primo = 0
					else :
						pago_primo = 0
						descuento_primo = 0


					count = 1
					suma = 0 

					while (count< int(documento)):
						if (int(documento) % count == 0):
							suma += count
						count = count + 1
					if (suma>int(documento)):
						pago_abundante = pago_boleto*0.15
						descuento_abundante = 15
					else :
						pago_abundante = 0
						descuento_abundante = 0

					
					pago = pago_boleto - (pago_primo + pago_abundante + pago_discapacidad)
					descuento = descuento_primo + descuento_abundante + descuento_discapacidad

			
					edad = input("\n Ingrese su edad : ")
					while not edad.isnumeric() or int(edad) == 0:
						edad = input("\n Ingrese valores validos : ")
					

		
					with open("Pasajeros.txt" , "a+") as bd:
						bd.write(f" Nombre :{nombre} | Edad :{edad} | Documento :{documento} | Discapacidad :{discapacidad} | Barco :{barco} | Pago boleto :{pago_boleto} | Pago total :{pago} | Descuento :{descuento}% | Impuestos :{impuesto} | Habitacion :{habitacion} \n ")

					with open("Pasajeros.txt" , "r") as bd:
						datos = bd.readlines()
						for i,dato in enumerate(datos):
							print(f"{i+1} {dato}")
	
			elif int(cantidad) > barco_seleccionado['capacity']['premium']:
				print("\n No se puede")


		elif tipo == '3':

			print(f''' Usted ha seleccionado la habitacion Vip , esto es lo que le ofrece

			1) Costo : {barco_seleccionado['cost']['vip']}$
			2) Cupo : {barco_seleccionado['capacity']['vip']} personas
		
			''')

			barco = barco_seleccionado['name']

			cantidad = input("\n Cuantas personas son ? : ")
			while not cantidad.isnumeric() or int(cantidad) == 0:
				cantidad = input("\n Ingrese valores validos : ")

			compraron += int(cantidad)


			for x in habitaciones:
				for y in x:
					print(y , end= " | ")
				print("\t")

			letra = int(input("\n Diga la habitacion que desea comprar (1)SA , (2)PB , (3)VC : "))
			while letra not in range(1,4):
				letra = input("\n Ingrese valores validos : ")
			numero = int(input("\n Diga el numero de la habitacion que desea : "))
			while numero not in range(1,11):
				numero = input("\n Ingrese valores validos : ")
			
			if letra == '1':
				letra = 0
			elif letra == '2':
				letra = 1
			elif letra == '3':
				letra = 2

			habitacion = habitaciones[letra - 1][numero - 1]
			hab.append(habitacion)
			print(habitacion)
			print(hab)

			if int(cantidad) <= barco_seleccionado['capacity']['vip']:

				for i in range(int(cantidad)):
	
					nombre = input("\n Ingrese su nombre : ")
					while not nombre.isalpha():
						nombre = input("\n Ingrese valores validos : ")
			
					documento = input("\n Ingrese su cedula de identidad : ")
					while not documento.isnumeric():
						documento = input("\n Ingrese valores validos : ")

					
					pago_boleto = barco_seleccionado['cost']['vip']

					impuesto = pago_boleto * 0.16

					discapacidad = input("\n Tiene alguna discapacidad ? (1)Si , (2)No :")
					while not discapacidad.isnumeric() or (int(discapacidad) not in range(1,3)):
						discapacidad = input("\n Ingrese valores validos : ")
			
					if discapacidad == '1':
						discapacidad = "Discapacitado"
						pago_discapacidad = pago_boleto*0.3
						descuento_discapacidad = 30
					else :
						discapacidad = "No discapacitado"
						pago_discapacidad = 0
						descuento_discapacidad = 0
				
					contador = 0

					for i in range(1,int(documento) + 1):
						if int(documento) % i == 0:
							contador += 1
					if contador == 2:
						pago_primo = pago_boleto*0.1
						descuento_primo = 10
					else :
						pago_primo = 0
						descuento_primo = 0


					count = 1
					suma = 0 

					while (count< int(documento)):
						if (int(documento) % count == 0):
							suma += count
						count = count + 1
					if (suma>int(documento)):
						pago_abundante = pago_boleto*0.15
						descuento_abundante = 15
					else :
						pago_abundante = 0
						descuento_abundante = 0

					
					pago = pago_boleto - (pago_primo + pago_abundante + pago_discapacidad)
					descuento = descuento_primo + descuento_abundante + descuento_discapacidad
			
					edad = input("\n Ingrese su edad : ")
					while not edad.isnumeric() or int(edad) == 0:
						edad = input("\n Ingrese valores validos : ")

		
					with open("Pasajeros.txt" , "a+") as bd:
						bd.write(f"nombre : {nombre} | Edad :  {edad} | Documento :  {documento} | Barco : {barco} | Discapacidad : {discapacidad} | Habitacion : {habitacion} \n ")

					with open("Pasajeros.txt" , "r") as bd:
						datos = bd.readlines()
						for i,dato in enumerate(datos):
							print(f"{i+1} {dato}")
	
			elif int(cantidad) > barco_seleccionado['capacity']['vip']:
				print("\n No se puede")


		elif compra == '2':
			print("\n Que tenga un feliz dia")

			duda = input("\n Cuantas personas eran , es solo para sacar unos porcentajes : ")
			while not duda.isnumeric():
				duda = input("\n Ingrese valores validos : ")

			no_compraron += int(duda)


def estadisticas(compraron , no_compraron , contador_no):

	'''
	Esta funcion tiene la finalidad de mostrarle a los clientes las estadisticas de los cruceros 
	'''

	simple = []
	premium = []
	vip = []

	pregunta = input(''' Que estadisticas desea ver ?

		1) Gasto promedio de un cliente en el crucero
		2) Porcentaje de Clientes que no compran tours
		3) La cantidad de personas que compraron y no compraron tickets
		4) Promedio de personas que compraron y no tickets
	
		> ''')

    while not pregunta.isnumeric() or (int(pregunta) not in range(1,5)):
        pregunta = input("\n Ingrese valores validos : ")


	if pregunta == '1':


		hab_s_1 = 69.99
		hab_s_2 = 59.99
		hab_s_3 = 49.99
		hab_s_4 = 59.99

		hab_s_p = (hab_s_1 + hab_s_2 + hab_s_3 + hab_s_4)//4

		hab_p_1 = 89.99
		hab_p_2 = 99.99
		hab_p_3 = 89.99
		hab_p_4 = 99.99

		hab_p_p = (hab_p_1 + hab_p_2 + hab_p_3 + hab_p_4)//4
			

		hab_v_1 = 129.99
		hab_v_2 = 119.99
		hab_v_3 = 139.99
		hab_v_4 = 119.99

		hab_v_p = (hab_v_1 + hab_v_2 + hab_v_3 + hab_v_4)//4

		tor_1 = 30
		tor_2 = 100
		tor_3 = 40

		promedio_tor = (tor_1 + tor_2 + tor_3)//3


		promedio_habitacion_simple = hab_s_p + promedio_tor
		promedio_habitacion_premium = hab_p_p + promedio_tor
		promedio_habitacion_vip = hab_v_p + promedio_tor

		print(f"Si el pasajero compra una habitacion simple , el promedio se su gasto sera de {promedio_habitacion_simple}")
		print(f"Si el pasajero compra una habitacion premium , el promedio se su gasto sera de {promedio_habitacion_premium}")
		print(f"Si el pasajero compra una habitacion vip , el promedio se su gasto sera de {promedio_habitacion_vip}")

	
	elif pregunta == '2':

		
			
		contador_tour_total = contador_visita + contador_puerto + contador_comida +contador_trotar
		porcentaje = (100 * contador_no)/contador_tour_total

		print(f"El porcentaje de clientes que no compraron tours fue de {porcentaje}"


	elif pregunta == '3':

		print(f" \n La cantidad de personas que compraron fueron de {compraron}")
		print(f" \n La cantidad de personas que no compraron fueron de {no_compraron}")


	elif pregunta == '4':

		total = compraron + no_compraron

		porcentaje_compra = (100 * no_compraron)/compraron
		porcentaje_no_compra = (100 * compraron)/ no_compraron

		print(f"El porcentaje de personas que compraron tickets fueron de {porcentaje_no_compra}")
		print(f"El porcentaje de personas que no compraron tickets fueron de {porcentaje_compra}")


def main():
    '''
    Esta funcion tiene como finalidad mostrarle al cliente todas las opciones que este puede ver
    '''

	while True:

		pregunta = input('''Bienvenido a Saman Caribbean , que desea hacer ? 
 
			1) Ver las habitaciones
			2) Ver los tours
			3) Ver restaurante
			4) Ver estadisticas
	
	 	> ''')

		if pregunta == '1':
			ver_barcos()
		elif pregunta == '2':
			tour()
		elif pregunta == '3':
			restaurante()
		elif pregunta == '4':
			estadisticas(compraron , no_compraron , contador_no)


main()