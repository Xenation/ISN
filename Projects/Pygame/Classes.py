import pygame
from pygame.locals import *
from random import randint

#--------#
# PLAYER #
class Player:
    # Constructor #
    def __init__(self, idle, forward, posX, posY):
        self.idle = pygame.image.load(idle)
        self.forward = [pygame.image.load(forward[0]), pygame.image.load(forward[1]), pygame.image.load(forward[2])]
        self.dir = self.idle
        self.box = self.idle.get_rect()
        self.posX = posX
        self.posY = posY
        self.sizeX = 65
        self.sizeY = 51

    # Metods #
    def move(self, dir):
        if dir == "left":
            self.dir = self.idle
            if self.posX > 4:
                self.posX -= 4
                self.box.move_ip(-4, 0)
        elif dir == "right":
            self.dir = self.forward[randint(0, 2)]
            if self.posX < 590:
                self.posX += 4
                self.box.move_ip(4, 0)
        elif dir == "up":
            self.dir = self.idle
            if self.posY > 4:
                self.posY -= 4
                self.box.move_ip(0, -4)
        elif dir == "down":
            self.dir = self.idle
            if self.posY < 430:
                self.posY += 4
                self.box.move_ip(0, 4)
        elif dir == "idle":
            self.dir = self.idle

#-----#
# MOB #
class Mob:
    # Constructor #
    def __init__(self, img, posX, posY, mobType):
        self.img = pygame.image.load(img)
        self.posX = posX
        self.posY = posY
        self.lastUpdate = 0
        self.mobType = mobType
        self.box = self.img.get_rect()
        if mobType == "default":
            self.sizeX = 50
            self.sizeY = 50
        elif mobType == "asteroid1":
            self.sizeX = 25
            self.sizeY = 21
        elif mobType == "asteroid2":
            self.sizeX = 50
            self.sizeY = 50
        elif mobType == "asteroid3":
            self.sizeX = 37
            self.sizeY = 39
        elif mobType == "asteroid4":
            self.sizeX = 76
            self.sizeY = 83

    # Metods #
    def move(self, player):
        if self.lastUpdate == 5:
            self.posX -= 2
            self.lastUpdate = 0
            self.box.move_ip(-2, 0)
        self.lastUpdate += 1
        if self.posX < -40:
            self.posX = 680
            self.posY = randint(0, 430)
            self.resetBox()
        if self.box.colliderect(player.box):
            player.posX = 0
            player.posY = 0
            player.box = Rect(player.posX, player.posY, player.sizeX, player.sizeY)

    def resetBox(self):
        self.box = Rect(self.posX, self.posY, self.sizeX, self.sizeY)

#-------#
# SCORE #
class Score:
    # Constructor #
    def __init__(self, img, n0, n1, n2, n3, n4, n5, n6, n7, n8, n9):
        self.img = pygame.image.load(img)
        self.n0 = pygame.image.load(n0)
        self.n1 = pygame.image.load(n1)
        self.n2 = pygame.image.load(n2)
        self.n3 = pygame.image.load(n3)
        self.n4 = pygame.image.load(n4)
        self.n5 = pygame.image.load(n5)
        self.n6 = pygame.image.load(n6)
        self.n7 = pygame.image.load(n7)
        self.n8 = pygame.image.load(n8)
        self.n9 = pygame.image.load(n9)
        self.n = [self.n0, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9]

    def displayScore(self, window, nb):
        window.blit(self.img, (0, 0))
        strNb = str(nb)
        strLen = len(strNb)
        for i in range(0, strLen):
            nb = int(strNb[i])
            window.blit(self.n[nb], (50+(i*11), 0))

#------------#
# BACKGROUND #
class Background:
    # Constructor #
    def __init__(self, img, posX, posY):
        self.img = pygame.image.load(img)
        self.posX = posX
        self.posY = posY
        self.lastUpdate = 0

    def move(self):
        if self.lastUpdate == 5:
            self.posX -= 1
            self.lastUpdate = 0
        self.lastUpdate += 1
        if self.posX < -1280:
            self.posX = 0

#--------#
# HITBOX #
class Hitbox:
    # Constructor #
    def __init__(self, surface, posX, posY, sizeX, sizeY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY

    def draw(self, posX, posY):
        pygame.draw.rect(self.surface, (255, 0, 0), (posX, posY, sizeX, sizeY))