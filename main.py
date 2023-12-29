import logging
import sys

import pygame

from enemy import Enemy, spawn_enemies
from player import Player

logging.basicConfig(level=10, format="%(asctime)s - %(levelname)5s - %(message)s") #, filename="output.log")

# Initialize Pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 153)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the coins!")

# Font setup
large_font = pygame.font.Font(None, 100)

# Initialize player
player = Player(start_x=WIDTH // 2, start_y=HEIGHT // 2)

# Generate enemies
enemies = spawn_enemies(board_width=WIDTH, board_height=HEIGHT, count=10)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemies)

clock = pygame.time.Clock()


# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Quit game event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw player
    player.update()
    screen.blit(player.image, player.rect)

    # Draw all enemies
    enemy_sprites.draw(screen)

    # Detect enemy collisions, increase player xp and render a new enemy
    if enemy := pygame.sprite.spritecollideany(player, enemy_sprites):
        player.xp += enemy.xp_value
        enemy_sprites.remove(enemy)
        enemy_sprites.add(Enemy(WIDTH, HEIGHT))

    # Render score
    text = large_font.render(f"XP: {player.xp}", True, WHITE)
    text_rect = text.get_rect()
    text_rect.topleft = (5, 5)
    screen.blit(text, text_rect)

    # Update screen
    pygame.display.flip()
    clock.tick(FPS)
    

# Quit Pygame
pygame.quit()
sys.exit()
