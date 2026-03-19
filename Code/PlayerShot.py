import pygame
from Code.Entity import Entity
from Code.Const import ENTITY_SPEED


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # tamanho do tiro
        self.surf = pygame.transform.scale(self.surf, (20, 20))
        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        self.rect.x += ENTITY_SPEED[self.name]