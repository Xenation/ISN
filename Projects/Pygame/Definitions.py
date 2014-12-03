import pygame
from pygame.locals import *

def resetBoxes(boxlist):
    for i in range(0, len(boxlist)):
        boxlist[i].box = Rect(boxlist[i].posX, boxlist[i].posY, boxlist[i].sizeX, boxlist[i].sizeY)