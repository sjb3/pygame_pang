############## Game Set-up #######################
# Basic framework that you can re-use

import pygame

pygame.init()

# Screen size

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Create title

pygame.display.set_caption('BAM')

# Set FPS values

clock = pygame.time.Clock()

####################################################

# 1. Basic game UI
# Create background

background = pygame.image.load(
    '/Users/sungjbyun/pygame_pang/pygame_basic/assets/pietro.jpg')

# Create main character

character = pygame.image.load(
    '/Users/sungjbyun/pygame_pang/pygame_basic/assets/ice-cream.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# positional changes

to_x = 0
to_y = 0

# Moving speed

character_speed = 0.6

# Enemy character

enemy = pygame.image.load(
    '/Users/sungjbyun/pygame_pang/pygame_basic/assets/sleep.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# Fonts

game_font = pygame.font.Font(None, 30)

# Gaming time

total_time = 10

# Time calc

start_ticks = pygame.time.get_ticks()

# Event loop

running = True  # Continue run the game
while running:
    dt = clock.tick(60)  # Frame / sec

# 2. Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Closing window?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # Adjust the character position not to go out of the frame
    # width
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    # height
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # Handle collisions

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Collision

    if character_rect.colliderect(enemy_rect):
        print('BAM')
        running = False

# 3. Render on the screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # Timer

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 24))

    screen.blit(timer, (10, 10))

    # Time out
    if total_time - elapsed_time <= 0:
        print('Time Out!')
        running = False

    pygame.display.update()


# Delayed exit out
pygame.time.delay(2000)

# To quit the game
pygame.quit()
