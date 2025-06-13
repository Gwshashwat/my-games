"""
🔸 Goal: Move a basket to catch falling objects.

🔸 Concepts: Object motion, collision, score keeping.
"""
import pygame
import random
pygame.init()

lenght = 1000
height = 750
screen = pygame.display.set_mode((lenght,height))
pygame.display.set_caption("GRAB YOUR EGGS!!!")

clock = pygame.time.Clock()

# egg property
egg_x = random.randint(20,lenght-20)
egg_y = 0
egg_colour = (255,255,255)
egg_radius = 20
egg_speed = 5

# Bucket property

basket_length = 50
basket_height = 80
basket_x = lenght // 2
basket_y = height - basket_height
basket_colour = (100,100,100)
basket_speed = 10

# score setup
score = 0
egg_fallen = 0
font = pygame.font.SysFont(None,40)

running = True
while running:
    screen.fill((0,0,0))
    egg_y += egg_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    text1 = font.render(f"SCORE : {score}" , True , (255,255,255))
    text2 = font.render(f"EGG FALLEN : {egg_fallen}" , True , (255,255,255))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0 :
        basket_x -= basket_speed
    
    if keys[pygame.K_RIGHT] and basket_x + basket_length < lenght :
        basket_x += basket_speed

    if basket_x <= egg_x <= basket_x + basket_length and basket_y < egg_y + egg_radius :
        egg_x = random.randint(20,lenght-20)
        egg_y = 0
        score += 1
        if egg_speed < 15 :
            egg_speed += 0.2
            basket_speed += 0.2
    
    elif egg_y >= height :
        egg_x = random.randint(20,lenght-20)
        egg_y = 0
        egg_fallen += 1
        if egg_speed < 15 :
            egg_speed += 0.2
            basket_speed += 0.2
        
    screen.blit(text1, (10,10))
    screen.blit(text2, (10,50))

    pygame.draw.rect(screen,basket_colour,(basket_x ,basket_y ,basket_length,basket_height))
    pygame.draw.circle(screen,egg_colour,(egg_x,egg_y),egg_radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()