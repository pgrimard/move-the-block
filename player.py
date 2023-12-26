import logging

import pygame

def handle_key(key):
    def decorator(func):
        def wrapper(self, keys):
            if keys[key]:
                func(self)
        return wrapper
    return decorator

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 7
        self.stance = "up"
        self.rect = pygame.Rect(pos_x, pos_y, 50, 50)

    @handle_key(pygame.K_UP)
    def move_up(self):
        logging.debug("Player facing up")
        self.stance = "up"
        
        if self.pos_y > 0:
            self.pos_y -= self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_DOWN)
    def move_down(self):
        logging.debug("Player facing down")
        self.stance = "down"

        if self.pos_y < 600:
            self.pos_y += self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_LEFT)
    def move_left(self):
        logging.debug("Player facing left")
        self.stance = "left"

        if self.pos_x > 0:
            self.pos_x -= self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_RIGHT)
    def move_right(self):
        logging.debug("Player facing right")
        self.stance = "right"

        if self.pos_x < 800:
            self.pos_x += self.speed
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    @handle_key(pygame.K_SPACE)
    def handle_space_key(self):
        if self.stance == "up":
            logging.debug("Player is shooting up")
        elif self.stance == "down":
            logging.debug("Player is shooting down")
        if self.stance == "left":
            logging.debug("Player is shooting left")
        if self.stance == "right":
            logging.debug("Player is shooting right")

    def handle_events(self):
        keys = pygame.key.get_pressed()

        self.move_up(keys)
        self.move_down(keys)
        self.move_left(keys)
        self.move_right(keys)
        self.handle_space_key(keys)