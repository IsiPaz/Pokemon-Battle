from Game.Pokemon import *

class Team:

	def __init__(self, team):
		self.__Team = team
		self.__Team_Full = False

	def getTeam(self):
		return self.__Team

	def getPokemon(self, index_pokemon):
		return self.__Team[index_pokemon]

	def Full(self):
	
		if len(self.__Team) == 3:
			self.__Team_Full = True
		
		return self.__Team_Full

	def addPokemon(self, Pokemon):
		if not self.Full():
			self.__Team.append(Pokemon)
		else:
			pass

	def DEB(self):
		cont = 0

		for pkm in self.__Team:
			if pkm.getDEB():
				cont+=1
		if cont == len(self.__Team):
			return True
		else: 
			return False