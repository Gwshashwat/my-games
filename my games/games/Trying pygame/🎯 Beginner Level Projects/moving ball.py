import pygame

pygame.init()

length = 1550
height = 800
screen = pygame.display.set_mode((length,height))
pygame.display.set_caption("MADE BY ME")

clock = pygame.time.Clock()

# Ball property
ball_radius = 20
ball_x = length // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 3
ball_colour = (0,255,0)

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= length:
        ball_speed_x *= -1
    elif ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y *= -1

    # Draw ball 
    pygame.draw.circle(screen,ball_colour,(ball_x,ball_y),ball_radius)


    pygame.display.update()
    clock.tick(120)
pygame.quit()