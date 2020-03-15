class Personaje():

	def __init__(self, name, team, bag):

		self.__Name = name
		self.Team = team
		self.__Bag = bag
		#self.__PC

	def getName(self):
		return self.__Name

	def getBag(self):
		return self.__Bag