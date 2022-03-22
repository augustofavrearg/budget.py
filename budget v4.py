class Category:

	lista=[]

	def __init__(self, categoria):

		self.categoria=categoria
		
	def deposit(self, cantidadD, descripcion=""):
		
		if self.categoria=="Ropa":
			self.cantidad_ropa=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad_ropa: ":self.cantidad_ropa, "descripcion: ":descripcion})

		if self.categoria=="Comida":
			self.cantidad_comida=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad_comida: ":self.cantidad_comida, "descripcion: ":descripcion})
		if self.categoria=="Auto":
			self.cantidad_auto=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad_auto: ":self.cantidad_auto, "descripcion: ":descripcion})
		if self.categoria=="Alquiler":
			self.cantidad_alquiler=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad_alquiler: ":self.cantidad_alquiler, "descripcion: ":descripcion})

	


	def withdraw(self, cantidadW, descripcion=""):
		
		if self.categoria=="Ropa":
			self.cantidad_ropa=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_ropa < cantidadW:
				print("No hay fondos.")
				return False
			else:
				self.lista.append({"cantidad_ropa: ": self.cantidad_ropa, "descripcion": self.descripcion})
				

			print(self.lista)

			return True

		if self.categoria=="Comida":
			self.cantidad_comida=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_comida < cantidadW:
				print("No hay fondos.")
				return False
			else:
				self.lista.append({"cantidad_comida: ": self.cantidad_comida, "descripcion": self.descripcion})
				

			print(self.lista)

			return True
		if self.categoria=="Alquiler":
			self.cantidad_alquiler=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_alquiler < cantidadW:
				print("No hay fondos.")
				return False
			else:
				self.lista.append({"cantidad_alquiler: ": self.cantidad_alquiler, "descripcion": self.descripcion})
				

			print(self.lista)

			return True
		if self.categoria=="Auto":
			self.cantidad_auto=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_auto < cantidadW:
				print("No hay fondos.")
				return False
			else:
				self.lista.append({"cantidad_auto: ": self.cantidad_auto, "descripcion": self.descripcion})
				

			print(self.lista)

			return True
		#self.lista.append({"cantidad: ":self.cantidad, "descripcion: ":descripcion})
		

	def get_balance(self):
		if self.categoria=="Auto":
			self.saldo_actual_auto=0

			for i in self.lista:
				self.saldo_actual_auto= self.saldo_actual_auto + i["cantidad_auto: "]
			
			print("Saldo actual auto: " + str(self.saldo_actual_auto))

			


		if self.categoria=="Ropa":
			self.saldo_actual_ropa=0

			for i in self.lista:
				self.saldo_actual_ropa= self.saldo_actual_ropa + i["cantidad_ropa: "]
			
			print("Saldo actual ropa: " + str(self.saldo_actual_ropa))

			

		if self.categoria=="Comida":
			self.saldo_actual_comida=0

			for i in self.lista:
				self.saldo_actual_comida= self.saldo_actual_comida + i["cantidad_comida: "]
			
			print("Saldo actual comida: " + str(self.saldo_actual_comida))

			


		if self.categoria=="Alquiler":
			self.saldo_actual_alquiler=0

			for i in self.lista:
				self.saldo_actual_alquiler= self.saldo_actual_alquiler + i["cantidad_alquiler: "]
			
			print("Saldo actual alquiler: " + str(self.saldo_actual_alquiler))

			
	def check_funds(self, monto):
		pass



def create_spend_chart(categories):
	pass

comida=Category("Comida")

ropa=Category("Ropa")

auto=Category("Auto")

alquiler=Category("Alquiler")

comida.deposit(1500, "Esta plata es para usar en comida.")
comida.withdraw(500, "Asado")
comida.withdraw(200, "Pan")
comida.withdraw(850, "Lechuga")

comida.get_balance()

ropa.deposit(5000, "Esta plata es para comprar ropa.")
ropa.withdraw(500, "Jeans")
ropa.withdraw(200, "Camisa")
ropa.withdraw(600, "Zapatillas")

ropa.get_balance()
