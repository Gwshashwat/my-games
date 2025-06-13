"""
🔸 Goal: Draw circles wherever the mouse is clicked.

🔸 Concepts: Mouse events, drawing shapes.
"""
import pygame
pygame.init()

length = 800
height = 500
screen = pygame.display.set_mode((length,height))
pygame.display.set_caption("CIRCLES CLICK")

clock = pygame.time.Clock()

# Circle property 
cir_radius = 15
cir_colour = (255,25,25)

circles = []

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            circles.append(pos)

    for cir in circles:
        pygame.draw.circle(screen,cir_colour,cir,cir_radius)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()