import math

class Pokemon:

    def __init__ (self, name, type1, type2, attacks, stats, level, expb, grow):

        #Caracteristicas
        self.__Name = name
        self.__Type1 = type1 #Tupla con un string con el nombre del tipo y con un numero de indice
        self.__Type2 = type2
        self.__Attacks = attacks
        self.__Stats = stats
        self.__Level = level
        self.__Max_HP = self.Calculation_Max_HP()
        self.__Exp_Base = expb
        self.__EXP = 0
        self.__Grow = grow
        self.__Exp_Next_Level = self.Calculation_exp_lvl()
        self.__Debilitado = False
        ##self.ID = id

        #Caracteristicas Batalla
        self.__Current_Status = " "
        self.__Current_HP = self.__Max_HP

    #Geters de las Caracteristicas

    def getName(self):
        return self.__Name

    def getType(self, flag = True):
        if flag:
            return self.__Type1
        else:
            return self.__Type2

    def getAttacks(self):
        return self.__Attacks

    def getStats(self):
        return self.__Stats

    def getLevel(self):
        return self.__Level

    def getMax_HP(self):
        return self.__Max_HP

    def getEXP_base(self):
        return self.__Exp_Base
    
    def getEXP(self):
        return self.__EXP

    def getExp_Next_Level(self):
        return self.__Exp_Next_Level

    def getGrow(self):
        return self.__Grow
        
    #Seters de las Caracteristicas
    def setAttacks(self, Attacks):
        self.__Attacks = Attacks

    def SubirNevel(self):
        self.__Level+=1

    def AumentoDeEXP(self, EXP):
        self.__EXP += EXP

    def setExp_Next_Level(self, Exp_Next_Level):
        self.__Exp_Next_Level = Exp_Next_Level

    #Seters y Geters de las caracteristicas de batalla

    def getDEB(self):
        return self.__Debilitado

    def getCurrent_Status(self):
        return self.__Current_Status

    def getCurrent_HP(self):
        return self.__Current_HP

    def setStatus(self, status):
        self.__Current_Status = status

    def setCurrent_HP(self, HP):
        self.__Current_HP = HP

    def TakeDamage(self, Damage):

        if (self.__Current_HP - Damage) <= 0:
            print("debilitado")
            self.__Debilitado = True
            self.__Current_HP = 0
        else:
            self.__Current_HP -= Damage


    def Cure(self, cure = True, revive = False):
               
        if cure == True:
            self.__Current_HP = self.__Max_HP
            for attack in self.__Attacks:
                attack.ResetCurrent_PP()
                self.__Debilitado = False
       
        elif revive == True:
            self.__Current_HP += cure
            if self.__Current_HP > self.__Max_HP:
                self.__Current_HP = self.__Max_HP
            self.__Debilitado = False

        else:
            self.__Current_HP += cure
            if self.__Current_HP > self.__Max_HP:
                self.__Current_HP = self.__Max_HP

    
    def Calculation_Max_HP(self):
        return int(10 + (((self.__Level/100) * (self.__Stats.getHP() * 2)) + self.__Stats.getIVs("HP") + self.__Stats.getEVs("HP")) + self.__Level) #PS: 10 + { Nivel / 100 x [ (Stat Base x 2) + IV + PE ] } + Nivel

    def Calculation_exp_lvl(self):

        x = self.__Level+1

        if self.__Grow == "Normal":
            return x**3

        if self.__Grow == "Parabolic":
            return int(1.2*pow(x,3)-15*pow(x,2)+100*x-140)

        if self.__Grow == "Slow":
            return int((5/4)*pow(x,3))

        if self.__Grow == "Fast":
            return int(0.8*pow(x,3))