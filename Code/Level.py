import pygame
import sys
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY
from Code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window, name, game_mode, timeout):

        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = timeout

        self.entity_list: list[Entity] = []

        # fundo
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # player
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        # controle de tiro
        self.last_shot_time = 0

        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):

        pygame.mixer.music.load("./asset/sound/Level1.mp3")
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            #  EVENTOS
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))

            #  TIRO
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:

                now = pygame.time.get_ticks()

                if now - self.last_shot_time > 400:

                    self.last_shot_time = now

                    for ent in self.entity_list:
                        if ent.name == "Player1":

                            self.entity_list.append(
                                EntityFactory.get_entity(
                                    "PlayerShot",
                                    (ent.rect.right, ent.rect.centery)
                                )
                            )

            #  ATUALIZAÇÃO
            for ent in self.entity_list[:]:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            # 🔥 REMOVER TIROS FORA DA TELA
            self.entity_list = [
                ent for ent in self.entity_list
                if not (ent.name == "PlayerShot" and ent.rect.left > WIN_WIDTH)
            ]

            # colisões
            EntityMediator.verify_collision(self.entity_list)

            #  PLAYER
            player = None
            for ent in self.entity_list:
                if ent.name == "Player1":
                    player = ent
                    break

            if player:
                self.level_text(14, f'Vida: {player.life}', COLOR_WHITE, (10, 25))

                if player.life <= 0:

                    self.level_text(
                        40,
                        "GAME OVER",
                        COLOR_WHITE,
                        (WIN_WIDTH / 2 - 120, WIN_HEIGHT / 2)
                    )

                    pygame.display.flip()
                    pygame.time.delay(2000)

                    return "menu"

            #  HUD
            self.level_text(
                14,
                f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                COLOR_WHITE,
                (10, 5)
            )

            self.level_text(
                14,
                f'fps: {clock.get_fps():.0f}',
                COLOR_WHITE,
                (10, WIN_HEIGHT - 35)
            )

            self.level_text(
                14,
                f'entidades: {len(self.entity_list)}',
                COLOR_WHITE,
                (10, WIN_HEIGHT - 20)
            )

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):

        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)

        text_surf = text_font.render(text, True, text_color).convert_alpha()

        text_rect = text_surf.get_rect(
            left=text_pos[0],
            top=text_pos[1]
        )

        self.window.blit(text_surf, text_rect)
