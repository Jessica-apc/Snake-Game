from enum import nonmember

import pygame

from Code.Menu import Menu


class Game:
    def _init_(self):
         pygame.init()
         self.window = pygame.display.set_mode(size=(600, 480))

    def run(self,):
        while True :
            menu = Menu(self.window)
            menu.run()
            pass

             # Check for all events "Cheque por todos os eventos"
         #    for event in pygame.event.get():
         #       if event .type == pygame.QUIT:
         #          pygame.quit() # Close window = Fechar janela
         #          quit()