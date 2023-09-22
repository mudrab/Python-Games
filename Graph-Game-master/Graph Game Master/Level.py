from pygame.locals import *
import pygame
import glob

def init_display():            #initialize the attributes
    global screen, tile
    screen = pygame.display.set_mode((1000, 550))   
    tile = pygame.image.load("wall.png")

def tiles(path):
    global tile            
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.splitlines()        
    for y, line in enumerate(data):         #iterates each line in a map
        for x, c in enumerate(line):        #iterates each character in a map
            if c == "1":
                screen.blit(tile, (x * 30, y * 30))

pygame.init() 
           
init_display()
loop = 1

while loop:

    tiles('map')
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0

    pygame.display.update()
pygame.quit()