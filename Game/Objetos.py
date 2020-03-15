class Item:

	def __init__ (self, name, Type, cost):
		self.__Name = name
		self.__Type = Type
		self.__Cost = cost

	def getName(self):
		return self.__Name

	def getType(self):
		return self.__Type

	def getCost(self):
		return self.__Cost



class Cures(Item):
	__Cure = 0
	__Cantidad = 1

	def getCure(self, flag = True):
		if flag:
			return self.__Cure
		else:
			self.__Cantidad-=1
			return self.__Cure

	def Cantidad(self, cantidad):
		self.__Cantidad += cantidad

	def getCantidad(self):
		return self.__Cantidad

	def setCure(self, Cure):
		self.__Cure = Cure



class Potion(Cures):

	def __init__(self):
		super(Potion, self).__init__("Pocion", "Botiquin", 300)
		self.setCure(20)


class Hiper_Potion(Cures):

	def __init__(self):
		super(Hiper_Potion, self).__init__("Hiper Pocion", "Botiquin", 300)
		self.setCure(200)


class Full_Restore(Cures):

	def __init__(self):
		super(Full_Restore, self).__init__("Restaura Todo", "Botiquin", 300)
		self.setCure(1000)
		

class Max_Revive(Cures):

	def __init__(self):
		super(Max_Revive, self).__init__("Max Revivir", "Botiquin", 300)
		self.setCure(1000)