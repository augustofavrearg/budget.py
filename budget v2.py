class Category:

	lista=[]

	def __init__(self, categoria):

		self.categoria=categoria
		
	def deposit(self, cantidad, descripcion=""):
		
		self.cantidad=cantidad
		self.descripcion=descripcion
		
		self.lista.append({"cantidad: ":cantidad, "descripcion: ":descripcion})

		print(self.lista)


	def withdraw(self, cantidad, descripcion=""):
		self.cantidad=cantidad 
		self.cantidad=cantidad*-1
		self.descripcion=descripcion 


	def get_balance(self):

		cantidad1=self.cantidad.deposit()
		cantidad2=self.cantidad.withdraw()
		if cantidad1 < cantidad2:

			print("No hay fondos.")
		else:
			self.lista.append({"cantidad: ":cantidad2, "descripcion: ":descripcion})

	def transfer(): 
		pass
	def check_funds(self, monto):
		pass



def create_spend_chart(categories):
	pass

#instancia de objeto
comida=Category("Comida")

#uso de metodo deposit
comida.deposit(1500, "Dinero para gastar en Comida")

#uso withdraw
comida.withdraw(20, "Leche")
comida.withdraw(10, "Pan")
#uso de get_balance
comida.get_balance()

#instancia de objeto
auto=Category("Auto")

#uso de metodo deposit
auto.deposit(4000, "Dinero para gastar en auto")

#instancia de objeto
alquiler=Category("Alquiler")

#uso de metodo deposit
alquiler.deposit(10000, "Dinero para alquiler.")


