import logging
import sys
from datetime import datetime, timedelta

import pygame

from board import Board
from enemy import spawn_enemies, spawn_random_enemy

logging.basicConfig(level=10, format="%(asctime)s - %(levelname)5s - %(message)s") #, filename="output.log")

# Initialize Pygame
pygame.init()

board = Board(width=800, height=600, fps=60)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 153)

# Create the window
screen = pygame.display.set_mode((board.width, board.height))
pygame.display.set_caption("Move The Block!!!")


# Player attributes
player_size = 50
player_x = board.width // 2 - player_size // 2
player_y = board.height - player_size - 10
player_speed = 5
xp = 0

# Generate enemies
enemies = spawn_enemies(board=board, count=10)

# Timer
timer = 20

# Font setup
font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 150)

clock = pygame.time.Clock()


# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if timer > 0:
        milliseconds = clock.tick(board.fps)
        seconds = milliseconds / 1000
        timer -= seconds

        if timer < 0:
            timer = 0

        screen.fill(BLACK)

        text = font.render(f"x={player_x}, y={player_y}, xp={xp}, timer={timer:.3f}s", True, WHITE)
        text_rect = text.get_rect(center=(board.width // 2, 10))
        screen.blit(text, text_rect)

        # Spawn enemies
        for enemy in enemies:
            pygame.draw.rect(screen, YELLOW, enemy.rect, border_radius=12)

        

        # Get the keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < board.width - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < board.height - player_size:
            player_y += player_speed

        player = pygame.Rect(player_x, player_y, player_size, player_size)

        collision_idx = player.collidelist(enemies)

        if collision_idx >= 0:
            logging.debug(f"Collided with {collision_idx}")

            player_colour = RED
            xp += enemies[collision_idx].xp

            del enemies[collision_idx]

            # Respawn dead enemy
            enemies.append(spawn_random_enemy(board.width, board.height))
                
        else:
            player_colour = GREEN
    else:
        text = large_font.render(f"GAME OVER!", True, RED)
        text_rect = text.get_rect(center=(board.width // 2, board.height // 2))
        screen.blit(text, text_rect)

    pygame.draw.rect(screen, player_colour, player)

    pygame.display.flip()
    

# Quit Pygame
pygame.quit()
sys.exit()
