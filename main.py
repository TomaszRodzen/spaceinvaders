import pygame
import random
# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceinvaders_icon.png')
pygame.display.set_icon(icon)


# Player
playerimg= pygame.image.load('player.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
enemyimg= pygame.image.load('enemy1.png')
enemyx = random.randint(0, 736)
enemyy = random.randint(64, 150)
enemyx_change = 4
enemyy_change = 40


#bullet
# ready mean you can see bullet
# file means missile is moving
missileimg= pygame.image.load('missile1.png')
missilex = 0
missiley = 480
missilex_change = 0
missiley_change = 10
missile_state = 'ready'


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_missile(x, y):
    global missile_state
    missile_state = 'fire'
    screen.blit(missileimg, (x - 17, y + 10))


# game loop. it closes the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if missile_state is 'ready':
                    missilex = playerx
                    fire_missile(missilex, missiley)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # RGB - Red, Green, Blue from 0 - 255
    screen.fill((13, 0, 0,))
    screen.blit(background, (0, 0))
    # movement in X axis
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736


    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 4
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -4
        enemyy += enemyy_change

    # missile movement
    if missiley <= 0:
        missiley = 480
        missile_state = 'ready'
    if missile_state is 'fire':
        fire_missile(missilex, missiley)
        missiley -= missiley_change

    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()