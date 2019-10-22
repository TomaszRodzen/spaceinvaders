import pygame
import random
# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))


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
enemyx_change = 0.3
enemyy_change = 40


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


# game loop. it closes the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # RGB - Red, Green, Blue from 0 - 255
    screen.fill((13, 0, 0,))

    # movement in X axis
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736


    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 0.3
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -0.3
        enemyy += enemyy_change

    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()