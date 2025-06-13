"""
🔸 Goal: A ball moves and bounces off window edges.

🔸 Concepts: Motion, collision with screen boundaries.
"""
import pygame
import sys

pygame.init()

# Window set up
length = 800
height = 700
pygame.display.set_caption("BOUNCING BALL")
screen = pygame.display.set_mode((length,height))

# Clock for frame rate
clock = pygame.time.Clock()

# Ball propertys
ball_radius = 20
ball_x = length // 2
ball_y = height // 2
ball_colour = (255,9,0)

# Ball speed
ball_x_speed = 5
ball_y_speed = 4

# Game loop 
running = True
while running:
    screen.fill((0,0,0))

    # Event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball 
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Bounce of edge 
    if ball_x - ball_radius <= 0:
        ball_x_speed *= -1

    elif ball_x + ball_radius >= length:
        ball_x_speed *= -1

    elif ball_y + ball_radius >= height:
        ball_y_speed *= -1

    elif ball_y - ball_radius <= 0:
        ball_y_speed *= -1

    # Draw ball 
    pygame.draw.circle(screen,ball_colour,(ball_x,ball_y),ball_radius)

    # Update display 
    pygame.display.update()
    clock.tick(60)

pygame.quit()