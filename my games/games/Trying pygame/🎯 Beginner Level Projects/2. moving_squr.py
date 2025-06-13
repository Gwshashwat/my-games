"""
2. Moving Square
🔸 Goal: Use arrow keys to move a square around the screen.

🔸 Concepts: Keyboard input, drawing shapes, screen refresh.
"""
import pygame

pygame.init()

clock = pygame.time.Clock()
length = 800
height = 800
screen = pygame.display.set_mode((length,height))
pygame.display.set_caption("Moving Square")
x, y = 200, 150
speed = 20

running = True
while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 0 : y -= speed
    if keys[pygame.K_d] and x + 50 < length : x += speed
    if keys[pygame.K_a] and x > 0 : x -= speed
    if keys[pygame.K_s] and y + 50 < height : y += speed
    pygame.draw.rect(screen,(255,0,0),(x,y,50,50))
    pygame.display.flip()

    clock.tick(60)
            
pygame.quit()