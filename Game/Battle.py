import random
from Game.constants import *
from Game.Combat import *

class Battle:

    def __init__(self, player, enemy, typec):
        
        self.__Player = player
        self.__Current_Pokemon = player.Team.getPokemon(0)
        self.__Enemy = enemy
        self.__Curr_Enemy = enemy.getPokemon(0)
        self.__Actual_Turn = 0
        self.__Type_Combat = typec  ##char s : salvaje , e: entrenador
        self.__Winner = None
        self.__Loser = None
        self.__Huir = False
        self.__Turns = []


###############################################################################################################
    def getPlayer(self):
        return self.__Player

    def getEnemys(self):
        return self.__Enemy

    def getCurrent_Pokemon(self):
        return self.__Current_Pokemon

    def getEnemy(self):
        return self.__Curr_Enemy

    def setEnemy(self):
        if len(self.__Enemy.getTeam()) != 0:
            self.__Curr_Enemy = self.__Enemy.getTeam()[random.randint(0, len(self.__Enemy.getTeam())- 1)]

###############################################################################################################

    def addAction(self, action):
        self.__Turns.append(action)

    def getActions(self):
        return self.__Turns

    def ClearActions(self):
        self.__Turns.clear()

###############################################################################################################

    def Huir(self):
        return self.__Huir

###############################################################################################################

    def ResetHuida(self):
        self.__Huir = False

###############################################################################################################

    def Combat(self, index_attack):
        combat = Combat(self.__Current_Pokemon, index_attack)
        self.addAction(combat)
        

########################################################################################################

    def Chance_Pokemon(self, pokemon_index):

        team = self.__Player.Team.getTeam()
        self.__Current_Pokemon = team[pokemon_index]
        team[0], team[pokemon_index] = team[pokemon_index], team[0]


########################################################################################################

    def HUIR(self):
        self.__Huir = True

#########################################################################################################

    def bot(self):
        index_attack = random.randint(0, len(self.__Curr_Enemy.getAttacks()) - 1)
        combate = Combat(self.__Curr_Enemy, index_attack)
        combate.setFlag(flag = True)
        self.addAction(combate)


############################################################################################################

    def is_finished(self):
        return self.__Player.Team.DEB() or self.__Enemy.DEB()

###############################################################################################################

    def Calculation_EXP (self):

        e = self.__Loser.getEXP_base()
        c = self.__Type_Combat
        l = self.__Loser.getLevel()

        if c == "s" :
            new_exp = (1*e*l)/7
        else :
            new_exp = (1.5*e*l)/7

        self.__Winner.AumentoDeEXP(int(new_exp))
        if self.__Winner.getName() == self.__Current_Pokemon.getName():
            print("Has ganado!!!")
            print("+",int(new_exp),"Exp")
            print("Nivel de experiencia ",int(new_exp),"/",self.__Winner.getExp_Next_Level())
            if self.__Winner.getEXP() >= self.__Winner.getExp_Next_Level():
                ##cambiar STATS D:
                self.__Winner.setExp_Next_Level(self.__Winner.Calculation_exp_lvl(self.__Winner.getGrow()))
                self.__Winner.SubirNevel()
                print(self.__Winner.getName()," ha subido de nivel")
                print("Nivel: ",self.__Winner.getLevel())

        else:
            print("Tus pokemons se han debilitado")
            print("Has ido corriendo al centro pokemon mas cercano")