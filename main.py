import sys
from board import *

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
player = Snake(5,5)
global apple
apple = Apple(player)

def draw():
    pygame.draw.rect(screen, (0,255,0), player.render(1))   
    for i in player.render(0):
        pygame.draw.rect(screen, (0,255,0), i) 

    pygame.draw.rect(screen, (255,0,0), apple.render())

def update():
    global apple
    player.move()
    if apple.isEaten(player):
        apple = Apple(player)
    player.isHit()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    update()
    draw()

    pygame.display.flip()
    fpsClock.tick(fps)


