import pygame

pygame.init()

# Display 
length = 1500
height = 780
screen = pygame.display.set_mode((length,height))
pygame.display.set_caption("BALL GAME")

clock = pygame.time.Clock()

# Ball property 
ball_x = length // 2
ball_y = height // 2
ball_rad = 10

# paddle property 
paddle_x = 800
paddle_y = 760

# 1. Create a font
font = pygame.font.SysFont(None, 50)  # (font name, size)

# Score set up
score = 0
# 2. Render the text (turn it into an image)
text = font.render("GAME OVER!", True, (255, 255, 255))  # (text, anti-aliasing, color)
text2 = font.render("PRESS R TO RESTART!", True, (255, 255, 255)) 

# 3. Blit (draw) it on the screen

# speed 
ball_x_speed = 9
ball_y_speed = 9
paddle_speed = 10

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    ball_x += ball_x_speed
    ball_y += ball_y_speed
    if ball_x - ball_rad <= 0:
        ball_x_speed *= -1

    elif ball_x + ball_rad >= length:
        ball_x_speed *= -1

    if ball_y + ball_rad <= 0:
        ball_y_speed *= -1
    
    elif ball_y + ball_rad >= height :
        ball_y_speed *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and paddle_x + 150 < length:
        paddle_x += paddle_speed
       
    elif keys[pygame.K_r]:
        ball_x = length // 2
        ball_y = height // 2
        ball_x_speed = 5
        ball_y_speed = 5
        paddle_speed = 9
        score = 0

    elif keys[pygame.K_LEFT] and paddle_x > 0 :
        paddle_x -= paddle_speed
    
    if ball_y + ball_rad >= paddle_y and paddle_x <= ball_x <= paddle_x + 150:
        ball_y_speed *= -1
        paddle_speed *= 1
        score += 1

        # Calculate where the ball hit on the paddle
        hit_pos = ball_x - paddle_x  # 0 to 150
        offset = (hit_pos - 75) / 75  # -1.0 (left) to 1.0 (right)

        # Change horizontal speed based on hit offset
        ball_x_speed = offset * 7    # Adjust '7' for more/less tilt
    
    text3 = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(text3,(10,10))

    if ball_y >= 760:
        screen.blit(text,(600,height // 2))
        screen.blit(text2,(600,450))
        ball_x_speed *= 0
        ball_y_speed *= 0

    pygame.draw.circle(screen,(255,255,255),(ball_x,ball_y),ball_rad)
    pygame.draw.rect(screen,(0,200,250),(paddle_x,paddle_y,150,20))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()