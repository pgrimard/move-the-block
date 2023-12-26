from enum import Enum
import logging

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
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 7
        self.stance = Stance.UP
        self.rect = pygame.Rect(pos_x, pos_y, 50, 50)

    @handle_key(pygame.K_UP)
    def move_up(self):
        logging.debug("Player facing up")
        self.stance = Stance.UP
        
        if self.pos_y > 0:
            self.pos_y -= self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_DOWN)
    def move_down(self):
        logging.debug("Player facing down")
        self.stance = Stance.DOWN

        if self.pos_y < 600:
            self.pos_y += self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_LEFT)
    def move_left(self):
        logging.debug("Player facing left")
        self.stance = Stance.LEFT

        if self.pos_x > 0:
            self.pos_x -= self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_RIGHT)
    def move_right(self):
        logging.debug("Player facing right")
        self.stance = Stance.RIGHT

        if self.pos_x < 800:
            self.pos_x += self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_SPACE)
    def handle_space_key(self):
        if self.stance == Stance.UP:
            logging.debug("Player is shooting up")
        elif self.stance == Stance.DOWN:
            logging.debug("Player is shooting down")
        if self.stance == Stance.LEFT:
            logging.debug("Player is shooting left")
        if self.stance == Stance.RIGHT:
            logging.debug("Player is shooting right")

    def handle_events(self):
        keys = pygame.key.get_pressed()

        self.move_up(keys)
        self.move_down(keys)
        self.move_left(keys)
        self.move_right(keys)
        self.handle_space_key(keys)