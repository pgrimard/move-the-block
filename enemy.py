import random

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, board_width: int, board_height: int):
        super().__init__()
        self.image = pygame.image.load("assets/coin.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            random.randint(0, board_width - self.rect.width),
            random.randint(0, board_height - self.rect.height),
        )
    
    @property
    def xp_value(self):
        return random.randint(1, 10)


def spawn_enemies(board_width: int, board_height: int, count: int = 1) -> list[Enemy]:
    return [Enemy(board_width, board_height) for i in range(count)]