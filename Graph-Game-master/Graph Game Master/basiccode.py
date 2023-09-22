import pygame
import time
import sys
from pygame.locals import *
pygame.init()   #initilize pygame

pygame.display.set_caption("Game")
WINDOW_SIZE=(400,400)   #window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)  #display window
display=pygame.Surface((400,400))

while True:
    for event in pygame.event.get(): #event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
