import pygame
import sys
import time
from pygame.locals import *

clock = pygame.time.Clock()
game_timer = 7500
pygame.init()   #initialize the game

pygame.display.set_caption('Graph Game')

WINDOW_SIZE = (1000,600)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)  #initialize the window

display = pygame.Surface((WINDOW_SIZE))
screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))

while True:     #to keep the window running
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()