import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Enemy import Enemy
from Code.Player import Player
from Code.PlayerShot import PlayerShot


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            #  BACKGROUND
            case 'Level1Bg':

                list_bg = []

                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))

                return list_bg

            #  PLAYER
            case 'Player1':
                return Player("Player1", (10, WIN_HEIGHT // 2))

            #  ENEMY
            case 'Enemy':
                return Enemy(
                    'Enemy',
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))
                )

            #  TIRO
            case 'PlayerShot':
                return PlayerShot('PlayerShot', position)

            #  ERRO
            case _:
                raise ValueError(f"Entidade '{entity_name}' não existe")



