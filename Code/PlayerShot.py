import pygame

from Code.Const import ENTITY_SPEED, WIN_WIDTH
from Code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.rect = self.surf.get_rect(center=position)

    def move(self):

        self.rect.x += ENTITY_SPEED[self.name]

        if self.rect.left > WIN_WIDTH:
            self.rect.right = 0