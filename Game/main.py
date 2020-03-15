from constants import *
from Pokemon import *
from Battle import *
from Attack import *
from Stats import *
from Personaje import *
from Mochila import *

#MOCHILA

mochila = Mochila()
pocion = Potion()
mochila.addItem(pocion)

#PERSONAJE

jugador = Personaje("seba", [], mochila)

#STATS

pkm1_stats = Stats(45,60,40,70,50,54) #HP, Attack, Defense, SpAttack, SpDefense, Speed
pkm2_stats = Stats(40,45,30,65,55,70) #HP, Attack, Defense, SpAttack, SpDefense, Speed

#POKEMONS

pkm1 = Pokemon("Treecko", Grass, NONE, pkm2_stats, 5, 65, "Parabolic")
pkm2 = Pokemon("Torchic Enemigo", Fire, NONE, pkm1_stats, 5, 65, "Parabolic")
pkm3 = Pokemon("Torchic", Fire, NONE, pkm1_stats, 5, 65, "Parabolic")

#ATTACKS
pkm1.setAttacks([Attack("Destructor",Normal,PHYSICAL,35,40,100, None, 0), Attack("Malicioso", Normal, STATE, 30, 0, 100, None, 0)])
pkm2.setAttacks([Attack("Arañazo"   ,Normal,PHYSICAL,35,40,100, None, 0), Attack("Gruñido",   Normal, STATE, 40, 0, 100, None, 0)])
pkm3.setAttacks([Attack("Arañazo"   ,Normal,PHYSICAL,35,40,100, None, 0), Attack("Gruñido",   Normal, STATE, 40, 0, 100, None, 0)])

jugador.addPokemon(pkm1)
jugador.addPokemon(pkm3)

#BATTLE

batalla = Battle(jugador, pkm2, "s")

while not batalla.Huir() and not batalla.is_finished():
	batalla.Action()
	##batalla.combat(batalla.pokemon1, batalla.pokemon2)

print("El combate a finalizado")

if batalla.Huir() == False:
	batalla.Calculation_EXP()
else:
	print("Has huido")
	batalla.ResetHuida()