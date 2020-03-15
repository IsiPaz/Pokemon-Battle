import sys
from gif import *
import time
from Game.constants import *
from Game.Battle import *
from Game.Personaje import *
from Game.Mochila import *
from Game.Team import *
from TextInput import *


pygame.init()
pygame.display.set_icon(pygame.image.load("media/pkm.ico"))
#FONTS PARA TEXTO (SI SE QUIERE AGREGAR UNO CREAR font3= ... para evitar errores de llamados a fonts)
pygame.font.init()
font = pygame.font.Font("media/Android101.ttf", 21)
fuente = pygame.font.Font("media/Android101.ttf", 18)
font1 = pygame.font.Font("media/SFPixelate.ttf", 27)
font2 = pygame.font.Font("media/SFPixelate.ttf", 20)
font3 = pygame.font.Font("media/SFPixelate.ttf", 18)

#MODIFICADOR PARA EL TAMAÑO DE VENTANA (no se recomienda modificar ya que el tamaño de los cuadros de seleccion esta en base al calculo de esos pixeles)

pygame.display.set_caption("Pokemon BATLLE, python edition")
corre = True

#ARCHIVO DE MUSICA PARA REPRODUCIR DURANTE LA BATALLA (se reproduce en loop)
playlist = ["media/music/Battle!.mp3", "media/music/main_theme.mp3"]
file = playlist[1]
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
flag_music = False

#Mochila
mochila = Mochila()
mochila.addItem(Hiper_Potion())
mochila.addItem(Full_Restore())
mochila.addItem(Max_Revive())



#def cambio(pokemon1, pokemon2): FUNCION POR DEFINIR PARA CAMBIAR ATAQUES AL CAMBIAR POKEMON (Sugerencia?)


##Funcion no modificable que aplica el uso de la libreria gif para cargar un nuevo pokemon en base a su nombre (en minusculas)
##Directamente llama solo una vez la funcion para cargar el gif una sola vez y evitar el gasto de memoria
def load(pokemon,letra):
	if letra == 'f': #Letra indicara si es la parte frontal o trasera del pokemon
		md1 = GIFImage("media/gif/"+pokemon.lower()+"_front.gif") #Se busca el achivo gif y se llama la libreria para comenzar su renderizado
		md1.scale(1.8) #Esto reescala la imagen del pokemon para dar el efecto de lejania al hacer uno un poco mas grande que el otro
		return md1
	elif letra == 'b':
		md2 = GIFImage("media/gif/"+pokemon.lower()+'_back.gif')
		md2.scale(2.7)


		return md2

def Vida_Choose(pokemon, ventana, pos):

	maxHP = pokemon.getMax_HP()
	HP = pokemon.getCurrent_HP()
	nombre = str(pokemon.getName())
	status = pokemon.getCurrent_Status()

	pixels = ((HP * 100)/maxHP)

	if pixels > 24 and pixels < 49:
		RGB = (255, 255, 0)
	elif pixels < 24:
		RGB = (255, 0 , 0)
	else:
		RGB = (0, 255, 0)

	pygame.draw.rect(ventana, RGB , (pos[0], pos[1], pixels, 7))

def ShowTeam(Team, ventana):

	imgfondo = pygame.image.load("media/backgrounds/elegir_pkm.png")
	ventana.blit(pygame.transform.scale(imgfondo, (800,600)),(0,0))

	x = [220, 210, 270]

	for pos in range(len(Team)):

		if pos%2 != 0:
			ventana.blit(pygame.transform.scale(pygame.image.load("media/gif/"+ Team[pos].getName().lower() +"_front.gif"), (56, 53)),(475,x[0]))
			ventana.blit(font.render(Team[pos].getName(), False, (255, 255, 255)), (545,x[1]))
			Vida_Choose(Team[pos], ventana, (574,x[1]+40))
			ventana.blit(fuente.render("HP "+str(Team[pos].getCurrent_HP())+"/"+str(Team[pos].getMax_HP()), False, (255, 255, 255)), (605,x[2]))
			x[0] += 140
			x[1] += 140
			x[2] += 140
		else:
			ventana.blit(pygame.transform.scale(pygame.image.load("media/gif/"+ Team[pos].getName().lower() +"_front.gif"), (56, 53)),(90,x[0]))
			ventana.blit(font.render(Team[pos].getName(), False, (255, 255, 255)), (160,x[1]))
			Vida_Choose(Team[pos], ventana, (189,x[1]+40))
			ventana.blit(fuente.render("HP "+str(Team[pos].getCurrent_HP())+"/"+str(Team[pos].getMax_HP()), False, (255, 255, 255)), (220,x[2]))


def vida(pokemon, JugadorOenemigo, ventana):
	maxHP = pokemon.getMax_HP()
	HP = pokemon.getCurrent_HP()
	nombre = str(pokemon.getName())
	status = pokemon.getCurrent_Status()
	lvl = '100'

	pixels = ((HP * 95)/maxHP)

	if pixels > 24 and pixels < 49:
		RGB = (255, 255, 0)
	elif pixels < 24:
		RGB = (255, 0 , 0)
	else:
		RGB = (0, 255, 0)

	if JugadorOenemigo == 'e':
		ventana.blit(pygame.transform.rotozoom((pygame.image.load("media/boton/BarraHP1.png")), 0, 2 ), (580, -10))
		pygame.draw.rect(ventana, RGB , (701, 97, pixels, 4))
		ventana.blit(font2.render(nombre, False, (255, 255, 255)), (620,75))
		ventana.blit(font3.render(lvl, False, (255, 255, 255)), (768,80))
		if status != " ":
			ventana.blit(pygame.image.load("media/status/"+status+".png"), (625,97))
	if JugadorOenemigo == 'j':
		ventana.blit(pygame.transform.rotozoom((pygame.image.load("media/boton/BarraHP2.png")), 0, 2 ), (1, 220))
		pygame.draw.rect(ventana, RGB , (47, 247, pixels, 4))
		ventana.blit(font2.render(nombre, False, (255, 255, 255)), (7,228))
		ventana.blit(font3.render(lvl, False, (255, 255, 255)), (147,229))
		ventana.blit(font3.render((str(HP)+"  "+str(maxHP)), False, (255, 255, 255)), (5,259))
		if status != " ":
			ventana.blit(pygame.image.load("media/status/"+status+".png"), (116,247))


def Action(ventana, batalla):

	for accion in batalla.getActions():

		if accion.getFlag():
			accion.setOpponent(batalla.getEnemy())
			accion.Attack()

			flag = True
			frame = True
			while flag:
				pygame.time.delay(16)
				for evento in pygame.event.get():
					if evento.type == pygame.QUIT:
						pygame.quit()

					elif evento.type == pygame.MOUSEBUTTONUP:
						flag = False

				ventana.blit(pygame.transform.scale(imgfondo, (800,600)),(0,0))
				vida(batalla.getEnemy(), 'e', ventana)
				vida(batalla.getCurrent_Pokemon(), 'j', ventana)

				if frame:
					pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
					frame = False

				pokemon_back.render(ventana, (130,220))
				pokemon_front.render(ventana, (480,70))
				ventana.blit(pygame.transform.scale(pygame.image.load("media/textbox.png"), (750,120)),(24,470))
				ventana.blit(font.render(accion.getPKM().getName()+' ha usado '+accion.NameAttack() , False, (0, 0, 0)), (87,487))

				pygame.display.flip()
				pygame.display.update()

			pygame.display.flip()
			pygame.display.update()

			if batalla.getEnemy().getDEB():

				break
		else:
			accion.setOpponent(batalla.getCurrent_Pokemon())
			accion.Attack()

			flag = True
			frame = True
			while flag:
				pygame.time.delay(16)
				for evento in pygame.event.get():
					if evento.type == pygame.QUIT:
						pygame.quit()

					elif evento.type == pygame.MOUSEBUTTONUP:
						flag = False

				ventana.blit(pygame.transform.scale(imgfondo, (800,600)),(0,0))
				vida(batalla.getCurrent_Pokemon(), 'j', ventana)
				vida(batalla.getEnemy(), 'e', ventana)

				if frame:
					pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
					frame = False

				pokemon_back.render(ventana, (130,220))
				pokemon_front.render(ventana, (480,70))
				ventana.blit(pygame.transform.scale(pygame.image.load("media/textbox.png"), (750,120)),(24,470))
				ventana.blit(font.render(accion.getPKM().getName()+' ha usado '+accion.NameAttack() , False, (0, 0, 0)), (87,487))

				pygame.display.flip()
				pygame.display.update()

			pygame.display.flip()
			pygame.display.update()

			print(batalla.getCurrent_Pokemon().getDEB())
			if not batalla.getPlayer().Team.DEB():
				if batalla.getCurrent_Pokemon().getDEB():
					ShowTeam(batalla.getPlayer().Team.getTeam(), ventana)
					flag = True
					while flag:
						for evento in pygame.event.get():
							if evento.type == pygame.QUIT:
								pygame.quit()

							for i in range(1, 3):
								if not batalla.getPlayer().Team.getTeam()[i].getDEB():
									if not batalla.getPlayer().Team.DEB():
										if Botones_Pokemon[i].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:

											batalla.Chance_Pokemon(i)
											flag = False
											break
									else:
										flag = False
										break

						pygame.display.flip()
						pygame.display.update()

					pygame.display.flip()
					pygame.display.update()

					break
			else:
				break

	enemy = batalla.getEnemys().getTeam()

	if batalla.getEnemy().getDEB():
		enemy.remove(batalla.getEnemy())
		batalla.setEnemy()
		batalla.ClearActions()

	batalla.ClearActions()

def Choose_Cure(ventana, Team):
	corre = True
	while corre:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				corre = False
				pygame.quit()
		if pygame.mouse.get_pressed()[2]:
			corre = False
			break

		ShowTeam(Team,  ventana)

		for evento in pygame.event.get():

			if evento.type == pygame.QUIT:
				pygame.quit()

			for i in range(0, 3):

					if Botones_Pokemon[i].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:
						return Team[i]

		pygame.display.flip()
		pygame.display.update()


def pos():
	return pygame.mouse.get_pos()

renderer0 = True
renderer1 = True

menu = True
T = False

equipo = []
team = []

while menu:
	pygame.time.delay(350)

	fondo = "media/backgrounds/menu1.png"
	imgfondo = pygame.image.load(fondo)
	ventana.blit(imgfondo,(0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONUP:
			menu1 = True
			while menu1:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
					#HOMBRE
					elif Seleccion_Sexo[0].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
						menu2 = True
						while menu2:
							fondo = "media/backgrounds/nameB.png"
							imgfondo = pygame.image.load(fondo)
							ventana.blit(imgfondo, (0,0))

							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
								elif event.type == pygame.MOUSEBUTTONUP:
									menu3 = True
									while menu3:
										for event in pygame.event.get():
											if event.type == pygame.QUIT:
												pygame.quit()
										fondo = "media/backgrounds/nameB1.png"
										imgfondo = pygame.image.load(fondo)
										ventana.blit(imgfondo, (0,0))
										NombreJ = ask(ventana, "Nombre")                                              ###nombre jugador
										Termino = True
										menu = False
										menu1 = False
										menu2 = False
										menu3 = False
										T=True
										break

									pygame.display.flip()
									pygame.display.update()

							pygame.display.flip()
							pygame.display.update()

						pygame.display.flip()
						pygame.display.update()


					#MUJER
					elif Seleccion_Sexo[1].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
						menu4 = True
						while menu4:
							fondo = "media/backgrounds/nameG.png"
							imgfondo = pygame.image.load(fondo)
							ventana.blit(imgfondo, (0,0))

							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
								elif event.type == pygame.MOUSEBUTTONUP:
									menu5 = True
									while menu5:
										for event in pygame.event.get():
											if event.type == pygame.QUIT:
												pygame.quit()
										fondo = "media/backgrounds/nameG1.png"
										imgfondo = pygame.image.load(fondo)
										ventana.blit(imgfondo, (0,0))
										NombreJ = ask(ventana, "Nombre")
										Termino = True
										menu = False
										menu1 = False
										menu4 = False
										menu5 = False
										T=True
										break

									pygame.display.flip()
									pygame.display.update()

							if T:
								break
							pygame.display.flip()
							pygame.display.update()
						if T:
							break
						pygame.display.flip()
						pygame.display.update()

				if T:
					break
				fondo = "media/backgrounds/seleccionar.png"
				imgfondo = pygame.image.load(fondo)
				ventana.blit(imgfondo, (0,0))

				pygame.display.flip()
				pygame.display.update()
	if T:
		break
	pygame.display.flip()
	pygame.display.update()

	pygame.time.delay(100)

	ventana.blit(pygame.image.load("media/backgrounds/menu.png"),(0,0))


	pygame.display.flip()
	pygame.display.update()

while True:

	Termino = True
	if flag_music:
		pygame.mixer.music.load(playlist[1])
		pygame.mixer.music.play(-1)

	while Termino:
		pygame.time.delay(50)

		ventana.blit(pygame.transform.scale(pygame.image.load("media/backgrounds/fondot.png"), (800,600)), (0,0))
		N = pygame.transform.rotozoom(pygame.image.load("media/icons/N.png"),0 , 0.5)
		R = pygame.transform.rotozoom(pygame.image.load("media/icons/Rayquaza.png"),0 , 0.5)
		N1 = ventana.blit(N, (475, 230))
		R1 = ventana.blit(R, (120, 250))

		ventana.blit(font.render(NombreJ+', selecciona un modo:', False, (0, 0, 0)), (65,55))
		ventana.blit(font.render('Legendarios', False, (255, 255, 255)), (120,500))
		ventana.blit(font.render('Entrenador', False, (255, 255, 255)), (475,500))

		if N1.collidepoint(pos()):
			ventana.blit(pygame.image.load("media/icons/Tselect.png"),(560, 165))
		else:
			ventana.blit(pygame.image.load("media/icons/Fselect.png"),(560, 165))

		if R1.collidepoint(pos()):
			ventana.blit(pygame.image.load("media/icons/Tselect.png"),(185, 165))
		else:
			ventana.blit(pygame.image.load("media/icons/Fselect.png"),(185, 165))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			elif N1.collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				modalidad = 'e'
				for x in range(0, 3):
					team.append(Pokemons_Enemys[random.randint(0, 11)])
				seleccion = True
				Termino = False
				break

			elif R1.collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				modalidad = 's'
				team.append(Pokemons_Enemys[random.randint(9, 11)])
				seleccion = True
				Termino = False
				break
		pygame.display.flip()
		pygame.display.update()

	M1 = False
	M2 = False
	M3 = False
	M4 = False
	M5 = False
	M6 = False
	M7 = False
	M8 = False
	M9 = False


	contador = 3
	seleccion = True
	while seleccion:
		if contador == 0:
			seleccion = False
			break

		pygame.time.delay(10)
		fondo = "media/backgrounds/chooseteam1.png"
		imgfondo = pygame.image.load(fondo)
		ventana.blit(imgfondo,(0,0))
		ventana.blit(font.render('Elige '+str(contador)+' pokemon, clickeando la pokeball:', False, (0, 0, 0)), (65,55))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			#Pikachu
			if Botones_Seleccion[0].collidepoint(pos()):
				P3 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(30, 185))

			if not Botones_Seleccion[0].collidepoint(pos()) and M3:
				P3 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(30, 185))

			if not Botones_Seleccion[0].collidepoint(pos()) and not M3:
				P3 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(30, 185))

			if Botones_Seleccion[0].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M3:
					contador+=1
					equipo.remove(Pokemons[0])
					M3 = False

				else:
					contador-=1
					equipo.append(Pokemons[0])
					M3 = True
			#Blaziken
			if Botones_Seleccion[1].collidepoint(pos()):
				P2 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(285, 185))

			if not Botones_Seleccion[1].collidepoint(pos()) and M2:
				P2 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(285, 185))

			if not Botones_Seleccion[1].collidepoint(pos()) and not M2:
				P2 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(285, 185))

			if Botones_Seleccion[1].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M2:
					contador+=1
					equipo.remove(Pokemons[1])
					M2 = False

				else:
					contador-=1
					equipo.append(Pokemons[1])
					M2 = True

			#Cryogonal
			if Botones_Seleccion[2].collidepoint(pos()):
				P1 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(540, 185))

			if not Botones_Seleccion[2].collidepoint(pos()) and M1:
				P1 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(540, 185))

			if not Botones_Seleccion[2].collidepoint(pos()) and not M1:
				P1 = ventana.blit(pygame.image.load("media/icons/Tselect.png"), (540,185))

			if Botones_Seleccion[2].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M1:
					contador+=1
					equipo.remove(Pokemons[2])
					M1 = False
				else:
					contador-=1
					equipo.append(Pokemons[2])
					M1 = True

			#Gardevoir
			if Botones_Seleccion[3].collidepoint(pos()):
				P6 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(30, 310))

			if not Botones_Seleccion[3].collidepoint(pos()) and M6:
				P6 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(30, 310))

			if not Botones_Seleccion[3].collidepoint(pos()) and not M6:
				P6 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(30, 310))

			if Botones_Seleccion[3].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M6:
					contador+=1
					equipo.remove(Pokemons[3])
					M6 = False

				else:
					contador-=1
					equipo.append(Pokemons[3])
					M6 = True


			#Swampert
			if Botones_Seleccion[4].collidepoint(pos()):
				P5 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(285, 310))

			if not Botones_Seleccion[4].collidepoint(pos()) and M5:
				P5 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(285, 310))

			if not Botones_Seleccion[4].collidepoint(pos()) and not M5:
				P5 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(285, 310))

			if Botones_Seleccion[4].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M5:
					contador+=1
					equipo.remove(Pokemons[4])
					M5 = False

				else:
					contador-=1
					equipo.append(Pokemons[4])
					M5 = True

			#Lucario
			if Botones_Seleccion[5].collidepoint(pos()):
				P4 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(540, 310))

			if not Botones_Seleccion[5].collidepoint(pos()) and M4:
				P4 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(540, 310))

			if not Botones_Seleccion[5].collidepoint(pos()) and not M4:
				P4 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(540, 310))

			if Botones_Seleccion[5].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M4:
					contador+=1
					equipo.remove(Pokemons[5])
					M4 = False

				else:
					contador-=1
					equipo.append(Pokemons[5])
					M4 = True

			#Lapras
			if Botones_Seleccion[6].collidepoint(pos()):
				P9 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(30, 435))

			if not Botones_Seleccion[6].collidepoint(pos()) and M9:
				P9 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(30, 435))

			if not Botones_Seleccion[6].collidepoint(pos()) and not M9:
				P9 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(30, 435))

			if Botones_Seleccion[6].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M9:
					contador+=1
					equipo.remove(Pokemons[6])
					M9 = False

				else:
					contador-=1
					equipo.append(Pokemons[6])
					M9 = True


			#Sceptile
			if Botones_Seleccion[7].collidepoint(pos()):
				P8 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(285, 435))

			if not Botones_Seleccion[7].collidepoint(pos()) and M8:
				P8 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(285, 435))

			if not Botones_Seleccion[7].collidepoint(pos()) and not M8:
				P8 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(285, 435))

			if Botones_Seleccion[7].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M8:
					contador+=1
					equipo.remove(Pokemons[7])
					M8 = False

				else:
					contador-=1
					equipo.append(Pokemons[7])
					M8 = True

			#Meloetta
			if Botones_Seleccion[8].collidepoint(pos()):
				P7 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(540, 435))

			if not Botones_Seleccion[8].collidepoint(pos()) and M7:
				P7 = ventana.blit(pygame.image.load("media/icons/Fselect.png"),(540, 435))

			if not Botones_Seleccion[8].collidepoint(pos()) and not M7:
				P7 = ventana.blit(pygame.image.load("media/icons/Tselect.png"),(540, 435))

			if Botones_Seleccion[8].collidepoint(pos()) and event.type == pygame.MOUSEBUTTONUP:
				if M7:
					contador+=1
					equipo.remove(Pokemons[8])
					M7 = False

				else:
					contador-=1
					equipo.append(Pokemons[8])
					M7 = True

			pygame.display.flip()
			pygame.display.update()

	Player = Personaje(NombreJ, Team(equipo), mochila)

	batalla = Battle(Player, Team(team), modalidad)
	pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
	pokemon_front = load(batalla.getEnemy().getName() , 'f')

	pygame.mixer.music.stop()
	file = playlist[0]
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1)

	pygame.mixer.music.stop()
	file = playlist[0]
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1)

	while not batalla.Huir() and not batalla.is_finished():
		pygame.time.delay(16) #actualiza cada 10 miliseg
		frame = True
		fondo = "media/backgrounds/menu1.png"
		imgfondo = pygame.image.load(fondo)
		ventana.blit(imgfondo,(0,0))


		for event in pygame.event.get():
			print(len(team))
			print(len(equipo))

			if event.type == pygame.QUIT:
				corre=False
				break

			if event.type == pygame.MOUSEBUTTONUP: #cambio de texto
				corre1 = True

				while corre1 and not batalla.is_finished() and not batalla.Huir():

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()

					pygame.font.init()

					if frame:
						pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
						frame = False
					#Renderiza la imagen del fondo al principio SIEMPRE, para que no se coloque sobre las otras imagenes que se vayan a poner
					fondo = "media/backgrounds/fondo1.png"
					imgfondo = pygame.image.load(fondo)
					ventana.blit(pygame.transform.scale(imgfondo, (800,600)),(0,0))

					#Esto directamente imprime la imagen del gif fotograma por fotograma en la ventana y su posicion
					pokemon_back.render(ventana, (130,220))
					vida(batalla.getEnemy(), 'e', ventana)
					vida(batalla.getCurrent_Pokemon(), 'j', ventana)

					#BOTON ATAQUE
					ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/lucha.png"), (210,80)),(350,410))
					if Botones[0].collidepoint(pos()):
						ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/lucha1.png"), (210,80)), (350,410))

					#BOTON POKEMON
					ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/pokemon.png"), (210,80)),(570,410))
					if Botones[1].collidepoint(pos()):
						ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/pokemon1.png"), (210,80)), (570,410))

					#BOTON BOLSA
					ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/bolsa.png"), (210,80)),(350,495))
					if Botones[2].collidepoint(pos()):
						ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/bolsa1.png"), (210,80)), (350,495))

					#BOTON HUIR
					ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/huir.png"), (210,80)),(570,495))
					if Botones[3].collidepoint(pos()):
						ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/huir1.png"), (210,80)), (570,495))

					##Este carga el pokemon enemigo, revisar siempre que sea el ultimo en renderizar
					pokemon_front.render(ventana, (480,70))

					#PARA CADA BOTON SE HIZO UN GRAN FOR QUE REVISA EN CADA ELIF SI HAY UNA COLISION ENTRE CADA BOTON Y EL LEVANTAMIENTO
					#DEL BOTON DEL MOUSE PARA ENTRAR, PARA RETROCEDER EN EL MENU SI O SI HAY QUE HACER EL CLICK DERECHO FUERA DE LOS 4
					#BOTONES

					#PARA ATAQUE
					for event in pygame.event.get():



						if event.type == pygame.QUIT:
							pygame.quit()

						elif Botones[0].collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
							corre2 = True
							while corre2:
								for event in pygame.event.get():
									if event.type == pygame.QUIT:
										corre2 = False
										pygame.quit()
								if pygame.mouse.get_pressed()[2]:
									corre2 = False
									break

								fondo = "media/backgrounds/fondo1.png"
								imgfondo = pygame.image.load(fondo)
								ventana.blit(pygame.transform.scale(imgfondo, (800,600)),(0,0))
								vida(batalla.getEnemy(), 'e', ventana)
								vida(batalla.getCurrent_Pokemon(), 'j', ventana)

								pokemon_back.render(ventana, (130,220))

								Attacks = batalla.getCurrent_Pokemon().getAttacks()

								#BOTON ATK 1
								ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/unnamed.png"), (210,80)),(350, 410))
								ventana.blit(pygame.transform.scale(pygame.image.load("media/types/Tipo_"+Attacks[0].getType() +".gif"), (45,15)),(360,420))
								ventana.blit(font.render(Attacks[0].getName(), False, (255, 255, 255)), (360,435))
								ventana.blit(fuente.render("PP "+str(Attacks[0].getCurrent_PP())+"/"+str(Attacks[0].getPP()), False, (255, 255, 255)), (450,460))
								#BOTON ATK 2
								ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/unnamed.png"), (210,80)),(570, 410))
								ventana.blit(pygame.transform.scale(pygame.image.load("media/types/Tipo_"+Attacks[1].getType() +".gif"), (45,15)),(580,420))
								ventana.blit(font.render(Attacks[1].getName(), False, (255, 255, 255)), (580,435))
								ventana.blit(fuente.render("PP "+str(Attacks[1].getCurrent_PP())+"/"+str(Attacks[1].getPP()), False, (255, 255, 255)), (670,460))

								#BOTON ATK 3
								ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/unnamed.png"), (210,80)),(350, 495))
								ventana.blit(pygame.transform.scale(pygame.image.load("media/types/Tipo_"+Attacks[2].getType() +".gif"), (45,15)),(360,505))
								ventana.blit(font.render(Attacks[2].getName(), False, (255, 255, 255)), (360,520))
								ventana.blit(fuente.render("PP "+str(Attacks[2].getCurrent_PP())+"/"+str(Attacks[2].getPP()), False, (255, 255, 255)), (450,545))

								#BOTON ATK 4
								ventana.blit(pygame.transform.scale(pygame.image.load("media/boton/unnamed.png"), (210,80)),(570, 495))
								ventana.blit(pygame.transform.scale(pygame.image.load("media/types/Tipo_"+Attacks[3].getType() +".gif"), (45,15)),(580,505))
								ventana.blit(font.render(Attacks[3].getName(), False, (255, 255, 255)), (580,520))
								ventana.blit(fuente.render("PP "+str(Attacks[3].getCurrent_PP())+"/"+str(Attacks[3].getPP()), False, (255, 255, 255)), (670,545))

								pokemon_front.render(ventana, (480,70))

								for evento in pygame.event.get():
									if evento.type == pygame.QUIT:
										pygame.quit()

									for i in range(0, 4):
										if Botones[i].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:

											if batalla.getCurrent_Pokemon().getStats().getCurrent_Speed() > batalla.getEnemy().getStats().getCurrent_Speed():
												batalla.Combat(i)
												batalla.bot()
												Action(ventana, batalla)
												pokemon_front = load(batalla.getEnemy().getName() , 'f')
												pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
												corre2 = False
												break
											else:
												batalla.bot()
												batalla.Combat(i)
												Action(ventana, batalla)
												pokemon_front = load(batalla.getEnemy().getName() , 'f')
												pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
												corre2 = False
												break

								pygame.display.flip()
								pygame.display.update()

						#PARA POKEMON:
						elif Botones[1].collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
							corre3 = True
							while corre3:
								for event in pygame.event.get():

									if event.type == pygame.QUIT:
										corre3 = False
										pygame.quit()
								if pygame.mouse.get_pressed()[2]:
									corre3 = False
									break

								ShowTeam(batalla.getPlayer().Team.getTeam(),  ventana)

								for evento in pygame.event.get():

									if evento.type == pygame.QUIT:
										pygame.quit()

									for i in range(1, 3):

										if not batalla.getPlayer().Team.getTeam()[i].getDEB():

											if Botones_Pokemon[i].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:
												batalla.Chance_Pokemon(i)
												batalla.bot()
												Action(ventana, batalla)
												corre3 = False
												corre2 = False
												corre1= False
												renderer0 = True
												break

								pygame.display.flip()
								pygame.display.update()

						#PARA BOLSA
						elif Botones[2].collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
							corre4 = True
							while corre4:
								for event in pygame.event.get():
									if event.type == pygame.QUIT:
										corre4 = False
										pygame.quit()
								if pygame.mouse.get_pressed()[2]:
									corre4 = False
									break

								#SE CAMBIA LA IMAGEN DEL FONDO, POR EL DE LA BOLSA HECHO EN PAINT 3D
								fondo = "media/backgrounds/BOLSA.png"
								imgfondo1 = pygame.image.load(fondo)

								boti = batalla.getPlayer().getBag().getBotiquin()

								ventana.blit(pygame.transform.scale(imgfondo1, (800,600)),(0,0))

								ventana.blit(font.render(str(boti["Max Revivir"].getCantidad())    , False, (255, 255, 255)), (300, 304))
								ventana.blit(font.render(str(boti["Hiper Pocion"].getCantidad())   , False, (255, 255, 255)), (300, 484))
								ventana.blit(font.render(str(boti["Restaura Todo"].getCantidad())  , False, (255, 255, 255)), (710, 304))


								for evento in pygame.event.get():

									if evento.type == pygame.QUIT:
										pygame.quit()

									elif Botones_Mochila[0].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:
										if boti["Max Revivir"].getCantidad() != 0:
											Choose_Cure(ventana, batalla.getPlayer().Team.getTeam()).Cure(cure = boti["Max Revivir"].getCure(flag = False), revive = True)
											batalla.bot()
											Action(ventana, batalla)
											corre4 = False
											corre3 = False
											corre2 = False
											break

									elif Botones_Mochila[1].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:
										if boti["Restaura Todo"].getCantidad() != 0:

											while Choose_Cure(ventana, batalla.getPlayer().Team.getTeam()).getDEB():
												x = 1

											Choose_Cure(ventana, batalla.getPlayer().Team.getTeam()).Cure(boti["Restaura Todo"].getCure(flag = False))
											batalla.bot()
											Action(ventana, batalla)
											corre4 = False
											corre3 = False
											corre2 = False
											break

									elif Botones_Mochila[2].collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONUP:
										if boti["Hiper Pocion"].getCantidad() != 0:

											while Choose_Cure(ventana, batalla.getPlayer().Team.getTeam()).getDEB():
												x = 1

											Choose_Cure(ventana, batalla.getPlayer().Team.getTeam()).Cure(boti["Hiper Pocion"].getCure(flag = False))
											batalla.bot()
											Action(ventana, batalla)
											corre4 = False
											corre3 = False
											corre2 = False
											break

									pygame.display.flip()
									pygame.display.update()

						elif Botones[3].collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:

							batalla.HUIR()
							break

						##FLIP Y UPDATE PARA LO QUE ESTE FUERA DEL FOR
						pygame.display.flip()
						pygame.display.update()

					#PARA HUIR (EN PROCESO, SE PIENSA MOSTRAR UN TEXO QUE DIGA "NO PUEDES HUIR DE UN COMBATE") SE HARA MAÑANA ;)
					pygame.display.flip()
					pygame.display.update()


		##ESTOS SON LAS CARGAS DEL PRIMER WHILE, NO MODIFICAR PORQUE CONTIENE EL RENDERIZADO PARA EL CASO DEL CAMBIO DE POKEMON

		fondo = "media/backgrounds/fondo1.png"
		imgfondo = pygame.image.load(fondo)
		ventana.blit(pygame.transform.scale(imgfondo, (800,600)),(0,0))
		pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')

		print (not batalla.Huir() and not batalla.is_finished())

		if not batalla.Huir() and not batalla.is_finished():
			if renderer0:
				pokemon_back = load(batalla.getCurrent_Pokemon().getName() , 'b')
				renderer0 = False
			pokemon_back.render(ventana, (130,220))

			if renderer1:
				pokemon_front = load(batalla.getEnemy().getName() , 'f')
				renderer1 = False
			pokemon_front.render(ventana, (480,70))

			#ESTO COLOCA TEXTO EN LA VENTADA CREADA

			pygame.font.init()
			ventana.blit(pygame.transform.scale(pygame.image.load("media/textbox.png"), (750,120)),(24,470))
			ventana.blit(font.render('Que deberia hacer '+batalla.getCurrent_Pokemon().getName()+'?', False, (0, 0, 0)), (87,487))
		else:

			finish = True
			while finish:

				if batalla.is_finished():
					if batalla.getEnemys().DEB():
						ventana.blit(pygame.transform.scale(pygame.image.load("media/textbox.png"), (750,120)),(24,470))
						ventana.blit(font.render("Has ganado!", False, (0, 0, 0)), (87,487))

					if batalla.getPlayer().Team.DEB():
						ventana.blit(pygame.transform.scale(pygame.image.load("media/textbox.png"), (750,120)),(24,470))
						ventana.blit(font.render("Todo tus pokemons se han debilitado.", False, (0, 0, 0)), (87,487))
						ventana.blit(font.render("Has perdido.", False, (0, 0, 0)), (87,505))

				if batalla.Huir():
					ventana.blit(pygame.transform.scale(pygame.image.load("media/textbox.png"), (750,120)),(24,470))
					ventana.blit(font.render("Has huido.", False, (0, 0, 0)), (87,487))

				for evento in pygame.event.get():

					if evento.type == pygame.QUIT:
						pygame.quit()

					elif evento.type == pygame.MOUSEBUTTONUP:
						finish = False

				pygame.display.flip()
				pygame.display.update()

			pygame.display.flip()
			pygame.display.update()

		pygame.display.flip()
		pygame.display.update()

	team.clear()
	equipo.clear()
	batalla.ResetHuida()
	mochila = Mochila()
	mochila.addItem(Hiper_Potion())
	mochila.addItem(Full_Restore())
	mochila.addItem(Max_Revive())
	render0 = True

	for pkm in Pokemons:
		pkm.Cure()

	for pkm in Pokemons_Enemys:
		pkm.Cure()

	flag_music = True
	#pygame.quit()
