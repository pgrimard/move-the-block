import logging
from enum import Enum

import pygame


def handle_key(key):
    def decorator(func):
        def wrapper(self, keys):
            if keys[key]:
                func(self)
        return wrapper
    return decorator

class Stance(Enum):
    UP: str = "UP"
    DOWN: str = "DOWN"
    LEFT: str = "LEFT"
    RIGHT: str = "RIGHT"

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x: int, start_y: int):
        super().__init__()
        self.images = [
            pygame.image.load("assets/player.png"),
            pygame.image.load("assets/player_left_foot.png"),
            pygame.image.load("assets/player_right_foot.png"),
        ]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)
        self.last_update = pygame.time.get_ticks()
        self.speed = 8
        self.frame_rate = 100

    def update(self):
        keys = pygame.key.get_pressed()

        # Animate player if moving
        if any(keys[key] for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
        else:
            self.image = self.images[0]

        # Move up
        if keys[pygame.K_UP]:
            logging.debug("Player facing up")
            self.stance = Stance.UP
            self.rect.y -= self.speed if self.rect.y > 0 else 0

        # Move down
        if keys[pygame.K_DOWN]:
            logging.debug("Player facing down")
            self.stance = Stance.DOWN
            self.rect.y += self.speed if self.rect.y < (600 - self.rect.height) else 0

        # Move left
        if keys[pygame.K_LEFT]:
            logging.debug("Player facing left")
            self.stance = Stance.LEFT
            self.rect.x -= self.speed if self.rect.x > 0 else 0

        # Move right
        if keys[pygame.K_RIGHT]:
            logging.debug("Player facing right")
            self.stance = Stance.RIGHT
            self.rect.x += self.speed if self.rect.x < (800 - self.rect.width) else 0

        # Primary attack
        if keys[pygame.K_SPACE]:
            logging.debug("Player primary attack")