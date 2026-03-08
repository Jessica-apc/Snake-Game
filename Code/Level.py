from xml.dom.minidom import Entity

import pygame

from Code.EntityFactory import EntityFactory
from Code.Const import COLOR_WHITE , WIN_HEIGHT


class Level:

    def __init__ (self, window, name, game_mode , timeout ):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000 # 20 segundos

    def run(self):
        pygame.mixer_music.load(f"./asset/sound/Level1.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()


            # Aqui são os textos que aparecem na tela do primeiro level
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Aqui temos o tipo de formatação que o texto vai receber
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
                text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
                text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
                text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
                self.window.blit(source=text_surf, dest=text_rect)

