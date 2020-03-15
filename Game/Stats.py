from random import randint

class Stats:

    def __init__(self, HP, Attack, Defense, SpAttack, SpDefense, Speed):

        #IV's
        self.__IVs_Max = randint(0, 31)
        self.__IVs = {
                    "HP"        :0,
                    "Attack"    :0,
                    "Defense"   :0,
                    "SpAttack"  :0,
                    "SpDefense" :0,
                    "Speed"     :0
                    }

        #EV's
        self.__EVs_Max = 0
        self.__EVs = {
                    "HP"        :0,
                    "Attack"    :0,
                    "Defense"   :0,
                    "SpAttack"  :0,
                    "SpDefense" :0,
                    "Speed"     :0
        }
        #BASE
        self.__HP = HP
        self.__Attack = Attack
        self.__Defense = Defense
        self.__SpAttack = SpAttack
        self.__SpDefense = SpDefense
        self.__Speed = Speed
        
        #Current
        self.__Current_Attack = Attack
        self.__Current_Defense = Defense
        self.__Current_SpAttack = SpAttack
        self.__Current_SpDefense = SpDefense
        self.__Current_Speed = Speed

    #Geters y Seters IV's and EV's
    def getIVs(self, IV):
        return self.__IVs[IV]
    
    def setIVs(self):
        for IV in self.__IVs:
            num = randint(0, self.__IVs_Max)
            self.__IVs_Max -= num
            self.__IVs[IV] = num

    def getEVs(self, EV):
        return self.__EVs[EV]

    def setEVs(self):
        pass
    #Geters de los stats base

    def getHP(self):
        return self.__HP

    def getAttack(self):
        return self.__Attack

    def getDefense(self):
        return self.__Defense

    def getSpAttack(self):
        return self.__SpAttack

    def getSpDefence(self):
        return self.__SpDefense

    def getSpeed(self):
        return self.__Speed

    #Seters de los stats base (subida de nivel)

    def setHP(self, HP):
        self.__HP += HP

    def setAttack(self, Attack):
        self.__Attack += Attack

    def setDefense(self, Defense):
        self.__Defense += Defense

    def setSpAttack(self, SpAttack):
        self.__SpAttack += SpAttack

    def setSpDefence(self, SpDefence):
        self.__SpDefense += SpDefence

    def setSpeed(self, Speed):
        self.__Speed += Speed

    #Geters de los stats variables
    
    def getCurrent_Attack(self):
        return self.__Current_Attack

    def getCurrent_Defence(self):
        return self.__Current_Defense

    def getCurrent_SpAttanck(self):
        return self.__Current_SpAttack

    def getCurrent_SpDefence(self):
        return self.__Current_SpDefense

    def getCurrent_Speed(self):
        return self.__Current_Speed
    
    #Seters de los stats variable

    def setCurrent_Attack(self, Attack, flag = True):
        self.__Current_Attack 

    def setCurrent_Defence(self, Defense , flag = True):
        self.__Current_Defense

    def setCurrent_SpAttanck(self, SpAttack, flag = True):
        self.__Current_SpAttack

    def setCurrent_SpDefence(self, SpDefense, flag = True):
        self.__Current_SpDefense

    def setSpeed(self, Speed, flag = True):
        self.__Speed

    def Reset(self, flag):
        if flag:
            self.__Current_Attack = self.Attack
            self.__Current_Defense = self.Defense
            self.__Current_SpAttack = self.SpAttack
            self.__Current_SpDefense = self.SpDefense
            self.__Current_Speed = self.Speed