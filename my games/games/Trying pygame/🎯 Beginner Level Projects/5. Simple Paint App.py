"""
🔸 Goal: Move the mouse to draw; click to change color.

🔸 Concepts: Mouse motion, color selection.
"""
import pygame
import sys
pygame.init()

length = 800
height = 500
screen = pygame.display.set_mode((length,height))

pygame.display.set_caption("PAINT")

clock = pygame.time.Clock()

# Circle property 
cir_radius = 15
cir_colour = (255,25,25)

# Clours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
pink = (255, 192, 203)
screen.fill(white)

# Brush size
brush_size = 5

drawing = False
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        # Mouse down starts drawing
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        # Mouse up stops drawing
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        elif event.type == pygame.KEYDOWN :
            
            if event.key == pygame.K_r:
                cir_colour = red

            elif event.key == pygame.K_g:
                cir_colour = green

            elif event.key == pygame.K_p:
                cir_colour = pink

            elif event.key == pygame.K_b:
                cir_colour = blue

            elif event.key == pygame.K_w:
                cir_colour = white

            elif event.key == pygame.K_0:
                cir_colour = black

            elif event.key == pygame.K_c:
                screen.fill(white)  # Clear screen

        if drawing:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,cir_colour,mouse_pos,brush_size)
        
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()