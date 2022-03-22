class Category:

	lista=[]

	def __init__(self, categoria):

		self.categoria=categoria
		
	def deposit(self, cantidadD, descripcion=""):
		
		if self.categoria=="Ropa":
			self.cantidad=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad: ":self.cantidad, "descripcion: ":descripcion})

		if self.categoria=="Comida":
			self.cantidad=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad: ":self.cantidad, "descripcion: ":descripcion})
		if self.categoria=="Auto":
			self.cantidad=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad: ":self.cantidad, "descripcion: ":descripcion})
		if self.categoria=="Alquiler":
			self.cantidad=cantidadD
			self.descripcion=descripcion
		
			self.lista.append({"cantidad: ":self.cantidad, "descripcion: ":descripcion})

	


	def withdraw(self, cantidadW, descripcion=""):
		
		if self.categoria=="Ropa":
			self.cantidadW=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_ropa < cantidadW:
				print("No hay fondos.")

				self.saldo_actual_ropa=self.saldo_actual_ropa-self.saldo_actual_ropa
				
				return False
			else:
				self.lista.append({"cantidad: ": self.cantidadW, "descripcion": self.descripcion})
				
				return True

		if self.categoria=="Comida":
			self.cantidadW=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_comida < cantidadW:
				print("No hay fondos.")
				self.saldo_actual_comida=self.saldo_actual_comida-self.saldo_actual_comida
				return False
			else:
				self.lista.append({"cantidad: ": self.cantidadW, "descripcion": self.descripcion})
				return True

		if self.categoria=="Alquiler":
			self.cantidadW=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_alquiler < cantidadW:
				print("No hay fondos.")
				self.saldo_actual_alquiler=self.saldo_actual_alquiler-self.saldo_actual_alquiler
				return False
			else:
				self.lista.append({"cantidad: ": self.cantidadW, "descripcion": self.descripcion})
				
				return True
		

			
		if self.categoria=="Auto":
			self.cantidadW=cantidadW * (-1)
			self.descripcion=descripcion 
			
			self.get_balance()

			if self.saldo_actual_auto < cantidadW:
				print("No hay fondos.")
				self.saldo_actual_auto=self.saldo_actual_auto-self.saldo_actual_auto
				return False
			else:
				self.lista.append({"cantidad: ": self.cantidadW, "descripcion": self.descripcion})
				
				return True
		#self.lista.append({"cantidad: ":self.cantidad, "descripcion: ":descripcion})
		

	def get_balance(self):
		if self.categoria=="Auto":
			self.saldo_actual_auto=0

			for i in self.lista:
				self.saldo_actual_auto= self.saldo_actual_auto + i["cantidad: "]
			
			print("Saldo actual: " + str(self.saldo_actual_auto))

			return self.saldo_actual_auto


		if self.categoria=="Ropa":
			self.saldo_actual_ropa=0

			for i in self.lista:
				self.saldo_actual_ropa= self.saldo_actual_ropa + i["cantidad: "]
			
			print("Saldo actual: " + str(self.saldo_actual_ropa))

			return self.saldo_actual_ropa


		if self.categoria=="Comida":
			self.saldo_actual_comida=0

			for i in self.lista:
				self.saldo_actual_comida= self.saldo_actual_comida + i["cantidad: "]
			
			print("Saldo actual: " + str(self.saldo_actual_comida))

			return self.saldo_actual_comida


		if self.categoria=="Alquiler":
			self.saldo_actual_alquiler=0

			for i in self.lista:
				self.saldo_actual_alquiler= self.saldo_actual_alquiler + i["cantidad: "]
			
			print("Saldo actual: " + str(self.saldo_actual_alquiler))

			return self.saldo_actual_alquiler
	
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
