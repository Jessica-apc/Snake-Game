from Code.Const import ENTITY_SPEED, WIN_WIDTH
from Code.Entity import Entity
import pygame


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


        self.surf = pygame.transform.scale(self.surf, (80, 80))

        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH