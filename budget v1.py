class Category:

	lista=[]

	def __init__(self, categoria):

		self.categoria=categoria
		
	def deposit(self, cantidad, descripcion=""):
		
		self.cantidad=cantidad
		self.descripcion=descripcion
		
		lista.append({"cantidad: ":cantidad, "descripcion: ":descripcion})

	def withdraw(self, cantidad, descripcion=""):
		self.cantidad=cantidad 
		cantidad=cantidad*-1
		self.descripcion=descripcion 


	def get_balance(self):

		cantidad1=cantidad.deposit
		cantidad2=cantidad.withdraw
		if cantidad1 < cantidad2:

			print("No hay fondos.")
		else:
			lista.append({"cantidad: ":cantidad2, "descripcion: ":descripcion})

	def transfer(): 
		pass
	def check_funds(self, monto):
		pass



def create_spend_chart(categories):
	pass

lista=[]

leche=Category("comida")

leche.deposit(1500)

leche.withdraw(141112, "Leche")

leche.get_balance()


print(lista)
