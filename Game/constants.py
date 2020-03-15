import sys
try:
	import pygame
	from pygame.locals import *
	from Game.Pokemon import *
	from Game.Attack import *
	from Game.Stats import *
	#CONSTANTS

	ventana = pygame.display.set_mode((800, 600))

	#CATEGORY

	PHYSICAL = "Physical"
	SPECIAL  = "Special"
	STATE    = "State"

	#TYPES
	Normal = ("Normal", 0)
	Fighting = ("Fighting", 1)
	Flying = ("Flying", 2)
	Poison = ("Poison", 3)
	Ground = ("Ground", 4)
	Rock = ("Rock", 5)
	Bug = ("Bug", 6)
	Ghost = ("Ghost", 7)
	Steel = ("Steel", 8)
	Fire = ("Fire", 9)
	Water = ("Water", 10)
	Grass = ("Grass", 11)
	Electric = ("Electric", 12)
	Psychic = ("Psychic", 13)
	Ice = ("Ice", 14)
	Dragon = ("Dragon", 15)
	Dark = ("Dark", 16)
	Fairy = ("Fairy", 17)
	NONE = ("Vacio", 18)

	#STATUS

	BRN = "BRN"
	FRZ = "FRZ"
	PAR = "PAR"
	PSN = "PSN"
	SLP = "SLP"


	#STRENGTHS AND WEAKNESSES

	EFFECTIVENESS = {   # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18
			Normal  [0]:	[1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],  #0
			Fighting[0]:	[2.0, 1.0, 0.5, 0.5, 1.0, 2.0, 0.5, 0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 0.5, 1.0],  #1
			Flying	[0]:	[1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],  #2
			Poison	[0]:	[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 0.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0],  #3
			Ground	[0]:	[1.0, 1.0, 0.0, 2.0, 1.0, 2.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],  #4
			Rock	[0]:	[1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0],  #5
			Bug 	[0]:	[1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 2.0, 0.5, 1.0],  #6
			Ghost	[0]:	[0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 1.0, 1.0],  #7
			Steel	[0]:	[1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0],  #8
			Fire 	[0]:	[1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 0.5, 0.5, 2.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0],  #9
			Water	[0]:	[1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],  #10
			Grass	[0]:	[1.0, 1.0, 0.5, 0.5, 2.0, 2.0, 0.5, 1.0, 0.5, 0.5, 2.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],  #11
			Electric[0]:	[1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],  #12
			Psychic	[0]:	[1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.0, 1.0, 1.0],  #13
			Ice 	[0]:	[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 2.0, 1.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0],  #14
			Dragon	[0]:	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.0, 1.0],  #15
			Dark  	[0]:	[1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 1.0],  #16
			Fairy	[0]:	[1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0],  #17
			NONE    [0]:	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]   #18
			}



	OPTIONS = ["1", "2", "3", "4"]



	#POKEMONS
	Pokemons = [

	        Pokemon("Pikachu",   Electric,    NONE,        [], Stats(35,  55,  30, 50,  40,  90),   100, 65, "Parabolic"),
	        Pokemon("Blaziken",  Fire,        Fighting,    [], Stats(80,  120, 70, 110, 70,  80),   100, 65, "Parabolic"),
	        Pokemon("Cryogonal", Ice,         NONE,        [], Stats(70,  50,  30, 95,  135, 105),  100, 65, "Parabolic"),
	        Pokemon("Gardevoir", Psychic,     NONE,        [], Stats(68,  65,  65, 125, 115, 80),   100, 65, "Parabolic"),
	        Pokemon("Swampert",  Water,       Ground,      [], Stats(100, 110, 90, 85,  90,  60),   100, 65, "Parabolic"),
	        Pokemon("Lucario",   Fighting,    Steel,       [], Stats(70,  110, 70, 115, 70,  90),   100, 65, "Parabolic"),
	        Pokemon("Lapras",    Water,       NONE,        [], Stats(130, 85,  80, 85,  95,  60),   100, 65, "Parabolic"),
	        Pokemon("Sceptile",  Grass,       NONE,        [], Stats(70,  85,  65, 105, 85,  120),  100, 65, "Parabolic"),
	        Pokemon("Melloetta", Normal,      Psychic,     [], Stats(100, 77,  77, 128, 128, 90),   100, 65, "Parabolic"),
	        ]


	Pokemons_Enemys = [

	        Pokemon("Pikachu",   Electric,    NONE,        [], Stats(35,  55,  30,  50,  40,  90),  100, 65, "Parabolic"),
	        Pokemon("Blaziken",  Fire,        Fighting,    [], Stats(80,  120, 70,  110, 70,  80),  100, 65, "Parabolic"),
	        Pokemon("Cryogonal", Ice,         NONE,        [], Stats(70,  50,  30,  95,  135, 105), 100, 65, "Parabolic"),
	        Pokemon("Gardevoir", Psychic,     NONE,        [], Stats(68,  65,  65,  125, 115, 80),  100, 65, "Parabolic"),
	        Pokemon("Swampert",  Water,       Ground,      [], Stats(100, 110, 90,  85,  90,  60),  100, 65, "Parabolic"),
	        Pokemon("Lucario",   Fighting,    Steel,       [], Stats(70,  110, 70,  115, 70,  90),  100, 65, "Parabolic"),
	        Pokemon("Lapras",    Water,       NONE,        [], Stats(130, 85,  80,  85,  95,  60),  100, 65, "Parabolic"),
	        Pokemon("Sceptile",  Grass,       NONE,        [], Stats(70,  85,  65,  105, 85,  120), 100, 65, "Parabolic"),
	        Pokemon("Melloetta", Normal,      Psychic,     [], Stats(100, 77,  77,  128, 128, 90),  100, 65, "Parabolic"),
	        Pokemon("Groudon",   Ground,      NONE,        [], Stats(100, 150, 140, 100, 90,  90),  100, 65, "Parabolic"),
	        Pokemon("Kyogre",    Water,       NONE,        [], Stats(100, 100, 90,  150, 140, 90),  100, 65, "Parabolic"),
	        Pokemon("Rayquaza",  Dragon,      NONE,        [], Stats(105, 150, 90,  150, 90,  95),  100, 65, "Parabolic"),
	        ]

	#ATTACKS
	Pokemons[0].setAttacks([Attack("Rayo",          Electric, SPECIAL,  15, 90,  100, None, 0),
							Attack("Onda trueno",   Electric, STATE,    20, 60,  100, None, 0),
							Attack("Trueno",        Electric, SPECIAL,  10, 110, 70,  None, 0),
							Attack("Ataque rapido", Normal,   PHYSICAL, 30, 40,  100, None, 0)])

	Pokemons[1].setAttacks([Attack("Patada ignea",  Fire,     PHYSICAL, 10, 85,  90,  None, 0),
							Attack("Puño fuego",    Fire,     PHYSICAL, 15, 75,  100, None, 0),
							Attack("Ascuas",        Fire,     SPECIAL,  25, 40,  100, None, 0),
							Attack("Doble patada",  Fighting, PHYSICAL, 30, 60,  100, None, 0)])

	Pokemons[2].setAttacks([Attack("Rayo aurora",   Ice,      SPECIAL,  20, 65,  100, None, 0),
							Attack("Rayo hielo",    Ice,      SPECIAL,  10, 90,  100, None, 0),
							Attack("Giro rapido",   Normal,   PHYSICAL, 40, 20,  100, None, 0),
							Attack("Tajo umbrio",   Dark,     SPECIAL,  15, 70,  100, None, 0)])

	Pokemons[3].setAttacks([Attack("Fuerza lunar",  Fairy,    SPECIAL,  15, 95,  100, None, 0),
							Attack("Confusion",     Psychic,  SPECIAL,  25, 20,  100, None, 0),
							Attack("Bola sombra",   Dark,     SPECIAL,  15, 80,  100, None, 0),
							Attack("Poder Oculto",  Normal,   SPECIAL,  15, 60,  100, None, 0)])

	Pokemons[4].setAttacks([Attack("Pistola agua",  Water,    SPECIAL,  25, 40,  100, None, 0),
							Attack("Disparo lodo",  Ground,   SPECIAL,  15, 55,  95,  None, 0),
							Attack("Placaje",       Normal,   PHYSICAL, 35, 40,  100, None, 0),
							Attack("Hidropulso",    Water,    SPECIAL,  20, 60,  100, None, 0)])

	Pokemons[5].setAttacks([Attack("Esfera aural",  Fighting, PHYSICAL, 20, 80,  100, None, 0),
							Attack("Garra metal",   Steel,    PHYSICAL, 35, 50,  195, None, 0),
							Attack("Pulso umbrio",  Dark,     SPECIAL,  15, 80,  100, None, 0),
							Attack("Ataque rapido", Normal,   PHYSICAL, 30, 40,  100, None, 0)])

	Pokemons[6].setAttacks([Attack("Hidrobomba",    Water,    SPECIAL,  5,  120, 80,  None, 0),
							Attack("Rayo de hielo", Ice,      SPECIAL,  10, 95,  100, None, 0),
							Attack("Pulso dragon",  Dragon,   SPECIAL,  10, 90,  100, None, 0),
							Attack("Cola de hierro",Steel,    PHYSICAL, 15, 100, 75,  None, 0)])

	Pokemons[7].setAttacks([Attack("Tijera X",      Bug,      PHYSICAL, 15, 80,  100, None, 0),
							Attack("Hojas navajas", Grass,    PHYSICAL, 15, 90,  100, None, 0),
							Attack("Lluevehojas",   Grass,    SPECIAL,  5,  130, 90,  None, 0),
							Attack("Malicioso",     Normal,   STATE,    30, 0,   100, 'def',0)])

	Pokemons[8].setAttacks([Attack("Ataque rapido", Normal,   PHYSICAL, 30, 40,  100, None, 0),
							Attack("Psiquico",      Psychic,  SPECIAL,  10, 90,  100, None, 0),
							Attack("Acrobata",      Flying,   PHYSICAL, 15, 55,  100, None, 0),
							Attack("Canon",         Normal,   SPECIAL,  15, 60,  100, None, 0)])

	#ATTACKS ENEMYS
	Pokemons_Enemys[0].setAttacks([Attack("Rayo",          Electric, SPECIAL,  15, 90,  100, None, 0),
								   Attack("Onda trueno",   Electric, STATE,    20, 60,  100, None, 0),
								   Attack("Trueno",        Electric, SPECIAL,  10, 110, 70,  None, 0),
								   Attack("Ataque rapido", Normal,   PHYSICAL, 30, 40,  100, None, 0)])

	Pokemons_Enemys[1].setAttacks([Attack("Patada ignea" , Fire,     PHYSICAL, 10, 85,  90,  None, 0),
								   Attack("Puno fuego",    Fire,     PHYSICAL, 15, 75,  100, None, 0),
								   Attack("Ascuas",        Fire,     SPECIAL,  25, 40,  100, None, 0),
								   Attack("Doble patada",  Fighting, PHYSICAL, 30, 60,  100, None, 0)])

	Pokemons_Enemys[2].setAttacks([Attack("Rayo aurora",   Ice,      SPECIAL,  20, 65,  100, None, 0),
								   Attack("Rayo hielo",    Ice,      SPECIAL,  10, 90,  100, None, 0),
								   Attack("Giro rapido",   Normal,   PHYSICAL, 40, 20,  100, None, 0),
								   Attack("Tajo umbrio",   Dark,     SPECIAL,  15, 70,  100, None, 0)])

	Pokemons_Enemys[3].setAttacks([Attack("Fuerza lunar",  Fairy,    SPECIAL,  15, 95,  100, None, 0),
								   Attack("Confusion",     Psychic,  SPECIAL,  25, 20,  100, None, 0),
								   Attack("Bola sombra",   Dark,     SPECIAL,  15, 80,  100, None, 0),
								   Attack("Poder Oculto",  Normal,   SPECIAL,  15, 60,  100, None, 0)])

	Pokemons_Enemys[4].setAttacks([Attack("Pistola agua",  Water,    SPECIAL,  25, 40,  100, None, 0),
								   Attack("Disparo lodo",  Ground,   SPECIAL,  15, 55,  95,  None, 0),
								   Attack("Placaje",       Normal,   PHYSICAL, 35, 40,  100, None, 0),
								   Attack("Hidropulso",    Water,    SPECIAL,  20, 60,  100, None, 0)])

	Pokemons_Enemys[5].setAttacks([Attack("Esfera aural",  Fighting, PHYSICAL, 20, 80,  100, None, 0),
								   Attack("Garra metal",   Steel,    PHYSICAL, 35, 50,  195, None, 0),
								   Attack("Pulso umbrio",  Dark,     SPECIAL,  15, 80,  100, None, 0),
								   Attack("Ataque rapido", Normal,   PHYSICAL, 30, 40,  100, None, 0)])

	Pokemons_Enemys[6].setAttacks([Attack("Hidrobomba",    Water,    SPECIAL,  5,  120, 80,  None, 0),
								   Attack("Rayo de hielo", Ice,      SPECIAL,  10, 95,  100, None, 0),
								   Attack("Pulso dragon",  Dragon,   SPECIAL,  10, 90,  100, None, 0),
								   Attack("Cola de hierro",Steel,    PHYSICAL, 15, 100, 75,  None, 0)])

	Pokemons_Enemys[7].setAttacks([Attack("Tijera X",      Bug,      PHYSICAL, 15, 80,  100, None, 0),
								   Attack("Hojas navajas", Grass,    PHYSICAL, 15, 90,  100, None, 0),
								   Attack("Lluevehojas",   Grass,    SPECIAL,  5,  130, 90,  None, 0),
								   Attack("Malicioso",     Normal,   STATE,    30, 0, 100, 'def', 0)])

	Pokemons_Enemys[8].setAttacks([Attack("Ataque rapido", Normal,   PHYSICAL, 30, 40,  100, None, 0),
								   Attack("Psiquico",      Psychic,  SPECIAL,  10, 90,  100, None, 0),
								   Attack("Acrobata",      Flying,   PHYSICAL, 15, 55,  100, None, 0),
								   Attack("Canon",         Normal,   SPECIAL,  15, 60,  100, None, 0)])

	Pokemons_Enemys[9].setAttacks([Attack("Llamarada",     Fire,     SPECIAL,  5,  110, 85,  None, 0),
								   Attack("Terremoto",     Ground,   PHYSICAL, 10, 100, 100, None, 0),
								   Attack("Poder pasado",  Ground,    SPECIAL,  5,  60,  100, None, 0),
								   Attack("Estallido",     Fire,     SPECIAL,  5,  150, 100, None, 0)])

	Pokemons_Enemys[10].setAttacks([Attack("Hidropulso",   Water,    SPECIAL,  20, 60,  100, None, 0),
								    Attack("Hidrobomba",   Water,    SPECIAL,  5,  120, 80,  None, 0),
								    Attack("Rayo hielo",   Ice,      SPECIAL,  10, 90,  100, None, 0),
								    Attack("Poder pasado", Ground,   SPECIAL,  5,  60,  100, None, 0)])

	Pokemons_Enemys[11].setAttacks([Attack("Pulso dragon", Dragon,   SPECIAL,  10, 90,  100, None, 0),
								    Attack("Garra dragon", Dragon,   PHYSICAL, 15, 80,  100, None, 0),
								    Attack("Triturar",     Dark,     PHYSICAL, 15, 80,  100, None, 0),
								    Attack("Ciclon",       Dragon,   SPECIAL,  20, 40,  100, None, 0)])


	Botones = [
				pygame.draw.rect(ventana, (0, 0, 0), (350, 420, 210, 70)),
				pygame.draw.rect(ventana, (0, 0, 0), (570, 420, 210, 70)),
				pygame.draw.rect(ventana, (0, 0, 0), (350, 505, 210, 70)),
				pygame.draw.rect(ventana, (0, 0, 0), (570, 505, 210, 70))
				]


	Botones_Mochila = [
						pygame.draw.rect(ventana, (0, 0, 0), (65,  250, 280, 90)),
						pygame.draw.rect(ventana, (0, 0, 0), (455, 250, 280, 90)),
						pygame.draw.rect(ventana, (0, 0, 0), (65,  430, 280, 90)),
						pygame.draw.rect(ventana, (0, 0, 0), (455, 430, 280, 90))
						]


	Botones_Pokemon = [	pygame.draw.rect(ventana, (0, 0, 0), (60,  200, 295, 95)),
						pygame.draw.rect(ventana, (0, 0, 0), (445, 200, 295, 95)),
						pygame.draw.rect(ventana, (0, 0, 0), (60,  345, 295, 95)),
						pygame.draw.rect(ventana, (0, 0, 0), (445, 345, 295, 95)),
						pygame.draw.rect(ventana, (0, 0, 0), (60,  490, 295, 95)),
						pygame.draw.rect(ventana, (0, 0, 0), (445, 490, 295, 95))
						]

	Seleccion_Sexo = [
						pygame.draw.rect(ventana, (0, 0, 0), (0, 0, 400, 600)),
						pygame.draw.rect(ventana, (0, 0, 0), (400, 0, 400, 600))
						]

	Botones_Seleccion = [
						pygame.draw.rect(ventana, (0,0,0), (30,  185, 44, 56)), #P3
						pygame.draw.rect(ventana, (0,0,0), (285, 185, 44, 56)), #P2
						pygame.draw.rect(ventana, (0,0,0), (540, 185, 44, 56)), #P1
						pygame.draw.rect(ventana, (0,0,0), (30,  310, 44, 56)), #P6
						pygame.draw.rect(ventana, (0,0,0), (285, 310, 44, 56)), #P5
						pygame.draw.rect(ventana, (0,0,0), (540, 310, 44, 56)), #P4
						pygame.draw.rect(ventana, (0,0,0), (30,  435, 44, 56)), #P9
						pygame.draw.rect(ventana, (0,0,0), (285, 435, 44, 56)), #P8
						pygame.draw.rect(ventana, (0,0,0), (540, 435, 44, 56)), #P7
						]

except:
	print("ERROR AL IMPORTAR LA LIBRERIA")
	sys.exit()
