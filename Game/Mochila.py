from Game.Objetos import *


class Mochila:

	def __init__(self):
		self.__OBJETOS = {}
		self.__BOTIQUIN = {}
		self.__MT_MO = {}
		self.__BAYAS = {}
		self.__OBJ_CLAVE = {}

#####################################################################################

	def addItem(self, item):

		if item.getType() == "Objeto":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__OBJETOS[item.getName()] = item
			else:
				self.__OBJETOS[item.getName()].Cantidad()

		elif item.getType() == "Botiquin":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__BOTIQUIN[item.getName()] = item
			else:
				self.__BOTIQUIN[item.getName()].Cantidad()

		elif item.getType() == "MT" or item.getType() == "MO":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__MT_MO[item.getName()] = item
			else:
				self.__MT_MO[item.getName()].Cantidad()

		elif item.getType() == "Baya":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__BAYAS[item.getName()] = item
			else:
				self.__BAYAS[item.getName()].Cantidad()

		else:
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__OBJ_CLAVE[item.getName()] = item
			else:
				self.__OBJ_CLAVE[item.getName()].Cantidad()

#######################################################################################

	def Objetos(self):
		pass

#######################################################################################
	def getBotiquin(self):
		return self.__BOTIQUIN

	def Botiquin(self, Pokemons, item):
		Pokemons[index_pokemon-1].Cure(cure = self.__BOTIQUIN[Objetos[int(comando)-1]].getCure())

##############################################################################################

	def MT_MO(self):
		pass

	def Bayas(self):
		pass

	def OBJ_Clave(self):
		pass