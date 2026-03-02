import pygame
import pygame.image

from Code.Const import WIN_WIDTH, MENU_OPTION, COLOR_YELLOW
from Code.Const import COLOR_PURPLE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/backgroud 1/background 1.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load("./asset/sound/Menu.mp3")
        pygame.mixer.music.play(-1)

        while True:
            # Mostra o fundo
            self.window.blit(source=self.surf, dest=self.rect)

            # Título
            self.menu_text(
                text_size=50,
                text="Snake",
                text_color=COLOR_PURPLE,
                text_center_pos=(WIN_WIDTH / 2, 70)
            )

            self.menu_text(
                text_size=50,
                text="Game",
                text_color=COLOR_PURPLE,
                text_center_pos=(WIN_WIDTH / 2, 120)
            )

            # Opções do menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(
                    text_size=20,
                    text=MENU_OPTION[i],
                    text_color=COLOR_YELLOW,
                    text_center_pos=(WIN_WIDTH / 2, 200 + 25 * i)
                )

            # Loop de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Atualiza a tela
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(
            name="Lucida Sans Typewriter",
            size=text_size
        )

        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)