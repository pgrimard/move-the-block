import random
from dataclasses import dataclass

import pygame

from board import Board


@dataclass
class Enemy():
    size: int
    x: int
    y: int

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    @property
    def xp(self):
        return random.randint(1, 10)


def spawn_enemies(board: Board, count: int = 1) -> list[Enemy]:
    enemies = []

    for i in range(count):
        enemy = spawn_random_enemy(board.width, board.height)
        enemies.append(enemy)

    return enemies

def spawn_random_enemy(board_width: int, board_height: int) -> Enemy:
    size = 25 #random.randint(10, 25)
    x = random.randint(0, board_width - size)
    y = random.randint(0, board_height - size)
    return Enemy(size=size, x=x, y=y)