import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.Menu import Menu
from Code.Level import Level
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Jogo da Cobra")

    def run(self):

        while True:

            # MENU
            menu = Menu(self.window)
            menu_return = menu.run()

            #  JOGAR
            if menu_return == MENU_OPTION[0]:

                level = Level(self.window, 'Level1', menu_return, 60000)
                level_return = level.run()

                # voltou do level (ex: morreu)
                if level_return == "menu":
                    continue

            #  SAIR
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                sys.exit()
