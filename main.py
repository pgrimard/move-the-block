import pygame, random
import sys

import logging

logging.basicConfig(level=10, format="%(asctime)s - %(levelname)5s - %(message)s") #, filename="output.log")

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move The Block!!!")

# Player attributes
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy attributes
enemy_count = 10
enemies = []

for i in range(enemy_count):
    enemy_size = random.randint(10, 50)
    enemy_rect = pygame.Rect(random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size), enemy_size, enemy_size)
    enemies.append(enemy_rect)

# Font setup
font = pygame.font.Font(None, 20)

clock = pygame.time.Clock()



# Game loop
running = True
while running:
    screen.fill(BLACK)

    text = font.render(f"x={player_x}, y={player_y}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, 10))
    screen.blit(text, text_rect)

    for enemy_rect in enemies:
        pygame.draw.rect(screen, WHITE, enemy_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    player = pygame.Rect(player_x, player_y, player_size, player_size)

    collision_idx = player.collidelist(enemies)

    if collision_idx >= 0:
        logging.debug(f"Collided with {collision_idx}")

        player_colour = RED

        if player_x < enemies[collision_idx].x:
            player_x -= player_speed
        else:
            player_x += player_speed

        if player_y < enemies[collision_idx].y:
            player_y -= player_speed
        else:
            player_y += player_speed
            
    else:
        player_colour = GREEN

    pygame.draw.rect(screen, player_colour, player)

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
