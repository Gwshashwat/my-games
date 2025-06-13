"""
🔸 Goal: A calculator interface with number buttons and result display.

🔸 Concepts: Buttons, mouse input, rendering text.
"""
import pygame

pygame.init()

# Disply
length = 600
height = 700
screen = pygame.display.set_mode((length,height))
pygame.display.set_caption("CALCULATOR")

# Clock
clock = pygame.time.Clock()

# Numbers 
font = pygame.font.SysFont(None,150)
font2 = pygame.font.SysFont(None,100)
text1 = font.render("1",True,(0,0,0))
text2 = font.render("2",True,(0,0,0))
text3 = font.render("3",True,(0,0,0))
text4 = font.render("4",True,(0,0,0))
text5 = font.render("5",True,(0,0,0))
text6 = font.render("6",True,(0,0,0))
text7 = font.render("7",True,(0,0,0))
text8 = font.render("8",True,(0,0,0))
text9 = font.render("9",True,(0,0,0))
text0 = font.render("0",True,(0,0,0))
text_add = font.render("+",True,(0,0,0))
text_minus = font.render("-",True,(0,0,0))
text_divide = font.render("/",True,(0,0,0))
text_multiply = font.render("*",True,(0,0,0))
text_equal = font.render("=",True,(0,0,0))
text_C = font.render("C",True,(0,0,0))

# function 
def is_clicked(pos,x,y,w = 150,h=115) :
    return x <= pos[0] <= x + w and y <= pos[1] <= y + h

user_input = ""
# Main loop 
running = True
while running :
    screen.fill((255,255,255))
    display_surface = font2.render(user_input, True, (0,0,0))
    screen.blit(display_surface, (20, 50))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            x,y = event.pos
            if is_clicked((x,y), 0, 180): user_input += "1"
            elif is_clicked((x,y), 150, 180): user_input += "2"
            elif is_clicked((x,y), 300, 180): user_input += "3"
            elif is_clicked((x,y), 0, 315): user_input += "4"
            elif is_clicked((x,y), 150, 315): user_input += "5"
            elif is_clicked((x,y), 300, 315): user_input += "6"
            elif is_clicked((x,y), 0, 445): user_input += "7"
            elif is_clicked((x,y), 150, 445): user_input += "8"
            elif is_clicked((x,y), 300, 445): user_input += "9"
            elif is_clicked((x,y), 150, 580): user_input += "0"
            elif is_clicked((x,y), 450, 315): user_input += "+"
            elif is_clicked((x,y), 450, 445): user_input += "-"
            elif is_clicked((x,y), 0, 580): user_input += "*"
            elif is_clicked((x,y), 300, 580): user_input += "/"
            elif is_clicked((x,y), 450, 180): user_input = ""  # Clear
            elif is_clicked((x,y), 450, 580):  # Equals
                try:
                    user_input = str(eval(user_input))
                except:
                    user_input = "Error"
    
    # Numbers and signs
    screen.blit(text1,(45 , 210))
    screen.blit(text2,(200 , 210))
    screen.blit(text3,(350 , 210))
    screen.blit(text4,(45 , 330))
    screen.blit(text5,(200 , 330))
    screen.blit(text6,(350 , 330))
    screen.blit(text7,(50 , 460))
    screen.blit(text8,(200 , 460))
    screen.blit(text9,(350 , 460))
    screen.blit(text0,(200,580))
    screen.blit(text_add,(498,320))
    screen.blit(text_minus,(513,448))
    screen.blit(text_multiply,(57,602))
    screen.blit(text_divide,(359,588))
    screen.blit(text_equal,(498,568))
    screen.blit(text_C,(493,205))

    # Vertical lines 
    pygame.draw.rect(screen,(0,0,0),(0 , 180 , 5 , height - 180))
    pygame.draw.rect(screen,(0,0,0),(150 , 180 , 5, height - 180))
    pygame.draw.rect(screen,(0,0,0),(300 , 180 , 5 , height - 180))
    pygame.draw.rect(screen,(0,0,0),(450 , 180, 5 , height - 180))
    pygame.draw.rect(screen,(0,0,0),(595 , 180 , 5 , height - 180))

    # Hrizontal lines 
    pygame.draw.rect(screen,(0,0,0),(0 , 180 , length , 5))
    pygame.draw.rect(screen,(0,0,0),(0 , 315 , length , 5))
    pygame.draw.rect(screen,(0,0,0),(0 , 445 , length , 5))
    pygame.draw.rect(screen,(0,0,0),(0 , 580 , length , 5))
    pygame.draw.rect(screen,(0,0,0),(0 , 695 , length , 5))

    pygame.display.flip()