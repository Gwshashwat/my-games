import pygame
pygame.init()

length = 1000
height = 700
screen = pygame.display.set_mode((length,height))
pygame.display.set_caption("Typing test")

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

    clock.tick(60)
pygame.quit()