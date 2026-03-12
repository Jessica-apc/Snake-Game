import pygame
from Code.Entity import Entity

from Code.EntityFactory import EntityFactory
from Code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from Code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window, name, game_mode, timeout):

        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        self.timeout = 20000  # 20 segundos

        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):

        pygame.mixer_music.load("./asset/sound/Level1.mp3")
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))

            # mover e desenhar entidades
            for ent in self.entity_list:

                self.window.blit(ent.surf, ent.rect)

                result = ent.move()

                # criar tiro
                if result == "SHOT":

                    self.entity_list.append(
                        EntityFactory.get_entity(
                            "PlayerShot",
                            (ent.rect.right, ent.rect.centery)
                        )
                    )

            # verificar colisões
            EntityMediator.verify_collision(self.entity_list)

            # textos na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            # mostrar vida do player
            for ent in self.entity_list:
                if ent.name == "Player1":
                    self.level_text(14, f'Vida: {ent.life}', COLOR_WHITE, (10, 25))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):

        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])

        self.window.blit(text_surf, text_rect)

