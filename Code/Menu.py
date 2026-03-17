import pygame
import pygame.image

from Code.Const import WIN_WIDTH, MENU_OPTION, COLOR_YELLOW, COLOR_PURPLE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/background 1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, menu_option=0):
        pygame.mixer.music.load("./asset/sound/Menu.mp3")
        pygame.mixer.music.play(-1)

        while True:
            # Fundo
            self.window.blit(self.surf, self.rect)

            #  TÍTULO
            self.menu_text_center(45, "JOGO", COLOR_PURPLE, (WIN_WIDTH / 2, 70))
            self.menu_text_center(45, "DA COBRA", COLOR_PURPLE, (WIN_WIDTH / 2, 120))

            #  OPÇÕES
            for i in range(len(MENU_OPTION)):
                color = COLOR_PURPLE if i == menu_option else COLOR_YELLOW

                self.menu_text_center(
                    25,
                    MENU_OPTION[i],
                    color,
                    (WIN_WIDTH / 2, 200 + 40 * i)
                )

            #  CONTROLES
            x_pos = WIN_WIDTH - 180

            self.menu_text_left(16, "CONTROLES", COLOR_YELLOW, (x_pos, 180))
            self.menu_text_left(14, "SETAS - mover", COLOR_YELLOW, (x_pos, 210))
            self.menu_text_left(14, "ESPAÇO - atirar", COLOR_YELLOW, (x_pos, 230))
            self.menu_text_left(14, "ENTER - selecionar", COLOR_YELLOW, (x_pos, 250))

            #  EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    # TITULO E OPÇÕES
    def menu_text_center(self, size, text, color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf = font.render(text, True, color).convert_alpha()
        rect = surf.get_rect(center=pos)
        self.window.blit(surf, rect)

    # TEXTO LATERAL (CONTROLES)
    def menu_text_left(self, size, text, color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf = font.render(text, True, color).convert_alpha()
        rect = surf.get_rect(midleft=pos)
        self.window.blit(surf, rect)