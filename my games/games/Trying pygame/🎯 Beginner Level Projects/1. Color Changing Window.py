"""
Color Changing Window
🔸 Goal: Press keys to change the screen color.

🔸 Concepts: Event handling, screen update, basic keys.
"""
import pygame
from random import randint

r = randint(0,255)
b = randint(0,255)
g = randint(0,255)

length = 800
height = 600
screen = pygame.display.set_mode((length,height))
colour = (r,b,g)
clock = pygame.time.Clock()

running = True
while running:
    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_j] : screen.fill(colour)
    if keys[pygame.K_f] : 
        r = randint(0,255)
        b = randint(0,255)
        g = randint(0,255)
        colour = (r,b,g)
        clock.tick(60)
    pygame.display.flip()