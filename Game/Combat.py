from Game.constants import *
from random import uniform	

class Combat():

	def __init__(self, Pokemon_1, index_attack):

		self.__Flag = True

		self.__Pokemon_1 = Pokemon_1
		self.__Pokemon_2 = None
		self.__Index_Attack = index_attack

############################################################################################################
	def getPKM(self):
		return self.__Pokemon_1
	
	def NameAttack(self):
		return self.__Pokemon_1.getAttacks()[self.__Index_Attack].getName()
	
	def setFlag(self, flag = False):
		if flag:
			self.__Flag = False

############################################################################################################

	def getFlag(self):
		return self.__Flag


	def setOpponent(self, opponent):
		self.__Pokemon_2 = opponent

############################################################################################################

	def Calculation_Damage(self):

		pkm1 = self.__Pokemon_1
		pkm2 = self.__Pokemon_2
		index_attack = self.__Index_Attack

		Bonus = 1
		Effectiveness = (EFFECTIVENESS[pkm1.getAttacks()[index_attack].getType()][pkm2.getType()[1]] 
					   * EFFECTIVENESS[pkm1.getAttacks()[index_attack].getType()][pkm2.getType()[1]])
		Varation = uniform(85, 100)
		Level = pkm1.getLevel()
		Power = pkm1.getAttacks()[index_attack].getPower()

		if pkm1.getAttacks()[index_attack].getCategory() == PHYSICAL:
			Attack = pkm1.getStats().getAttack()
			Defense = pkm2.getStats().getDefense()

		elif pkm1.getAttacks()[index_attack].getCategory() == SPECIAL:
			Attack = pkm1.getStats().getSpAttack()
			Defense = pkm2.getStats().getSpDefence()

		if (pkm1.getAttacks()[index_attack].getType() == pkm1.getType() or pkm1.getAttacks()[index_attack].getType() == pkm1.getType(False)):
			print(pkm1.getAttacks()[index_attack].getType())
			Bonus = 1.5


		damage = 0.01 * Bonus * Effectiveness * Varation * (((((0.2 * Level)+2) * Attack * Power)/(25 * Defense))+2)
		print(int(damage))
		return int(damage)


############################################################################################################
	def Attack(self):
		pkm1 = self.__Pokemon_1
		pkm2 = self.__Pokemon_2

		print(pkm1.getName(), "ha usado", pkm1.getAttacks()[self.__Index_Attack].getName())

		if pkm1.getAttacks()[self.__Index_Attack].getCategory() == STATE:
			print("jajaj equis de")

		else:
			pkm2.TakeDamage(self.Calculation_Damage())
			pkm1.getAttacks()[self.__Index_Attack].Attack()

		if pkm2.getCurrent_HP() <= 0:
			
			pkm2.setCurrent_HP(0)
			print(pkm2.getName(),":",str(pkm2.getCurrent_HP())+"/"+str(pkm2.getMax_HP()),"HP")
			return

		print(pkm2.getName(),":",str(pkm2.getCurrent_HP())+"/"+str(pkm2.getMax_HP()),"HP")	
	