import sys
try:
    import pygame
    import pygame.font
    import pygame.event
    import pygame.draw
    import string
    from pygame.locals import *

    def get_key():
      while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
          return event.key
        else:
          pass

    def display_box(screen, message):
      fontobject = pygame.font.Font("media/SFPixelate.ttf",27)
      pygame.draw.rect(screen, (255,255,255),
                       (160,
                        460,
                        490,29), 0)

      if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (0,0,0)),
                    (160, 460 ))
      pygame.display.flip()

    def ask(screen, question):
      "ask(screen, question) -> answer"
      #string = ''
      pygame.font.init()
      current_string = []
      display_box(screen, question + ": " + "".join(current_string))
      while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
          current_string = current_string[0:-1]
        elif inkey == K_RETURN:
          break
        elif inkey == K_MINUS:
          current_string.append("_")
        elif inkey <= 127:
          current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
      return "".join(current_string)

except:
    print("ERROR AL IMPORTAR LA LIBRERIA")
    sys.exit()
