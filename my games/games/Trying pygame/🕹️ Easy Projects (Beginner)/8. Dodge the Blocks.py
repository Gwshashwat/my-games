"""
🔸 Goal: Move a character left/right to avoid falling blocks.

🔸 Concepts: Object spawning, increasing difficulty.

"""
import pygame
import random

pygame.init()

# Display
length = 1000
height = 700
screen = pygame.display.set_mode((length, height))
pygame.display.set_caption("DODGE THOSE BALOKSS !!!!")

# Clock
clock = pygame.time.Clock()

# Character
char_length = 50
char_height = 30
char_x = length // 2
char_y = height - char_height - 10
char_speed = 10

# Block properties
block_speed = 6
blocks = []

# Function to spawn a new block
def spawn_block():
    width = random.randint(20, 100)
    height_b = random.randint(20, 50)
    x = random.randint(0, length - width)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return [color, pygame.Rect(x, 0, width, height_b)]

# Spawn initial blocks
for _ in range(3):
    blocks.append(spawn_block())

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Character movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and char_x > 0:
        char_x -= char_speed
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and char_x < length - char_length:
        char_x += char_speed

    char_rect = pygame.Rect(char_x, char_y, char_length, char_height)
    pygame.draw.rect(screen, (255, 255, 255), char_rect)

    # Update blocks
    for block in blocks:
        block[1].y += block_speed
        pygame.draw.rect(screen, block[0], block[1])

        # Collision detection
        if char_rect.colliderect(block[1]):
            print("💥 You got hit!")
            running = False

    # Remove off-screen blocks and spawn new ones
    blocks = [block for block in blocks if block[1].y < height]
    while len(blocks) < 3:
        blocks.append(spawn_block())

    # Refresh display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()