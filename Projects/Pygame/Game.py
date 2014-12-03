# Créé par Xenation, le 28/11/2014 avec EduPython
import pygame
import time
from pygame.locals import *
from lycee import *
from random import randint
from Classes import *
from Definitions import *

pygame.init()

#----------#
# NEW GAME #
#----------#

# VARIABLES #
gameLoop = False
mainLoop = True
devMode = False

# WINDOW #
window = pygame.display.set_mode((640, 480))

# PRE-MENU #
studioLogo = pygame.image.load("Images/pre.jpg").convert()
window.blit(studioLogo, (0,0))
pygame.display.flip()
pygame.time.wait(3000)
pygame.display.flip()

# MENU #
menuBg = pygame.image.load("Images/space2.jpg")
menuTitle = pygame.image.load("Images/MenuTitle.png")
menuStart = pygame.image.load("Images/MenuStartSel.png")
menuExit = pygame.image.load("Images/MenuExit.png")
menuDevMode = pygame.image.load("Images/MenuDevMode.png")
Selection = 1

# Initial Update #
pygame.display.flip()

# MAIN MENU LOOP #
while mainLoop == True:
    # Events #
    for event in pygame.event.get():
        # Keys #
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                mainLoop = False
                pygame.display.quit()
            elif event.key == K_UP:
                if Selection == 2:
                    Selection = 1
                    menuStart = pygame.image.load("Images/MenuStartSel.png")
                    menuExit = pygame.image.load("Images/MenuExit.png")
                elif Selection == 3:
                    Selection = 2
                    menuDevMode = pygame.image.load("Images/MenuDevMode.png")
                    menuExit = pygame.image.load("Images/MenuExitSel.png")
            elif event.key == K_DOWN:
                if Selection == 1:
                    Selection = 2
                    menuStart = pygame.image.load("Images/MenuStart.png")
                    menuExit = pygame.image.load("Images/MenuExitSel.png")
                elif Selection == 2:
                    Selection = 3
                    menuDevMode = pygame.image.load("Images/MenuDevModeSel.png")
                    menuExit = pygame.image.load("Images/MenuExit.png")
            elif event.key == K_SPACE:
                if Selection == 1:
                    mainLoop = False
                    gameLoop = True
                if Selection == 2:
                    mainLoop = False
                    pygame.display.quit()
                if Selection == 3:
                    mainLoop = False
                    gameLoop = True
                    devMode = True
        # Others #
        elif event.type == QUIT:
            mainLoop = False
            pygame.display.quit()
    # Updates #
    if mainLoop == True:
        window.blit(menuBg, (0, 0))
        window.blit(menuTitle, (283, 80))
        window.blit(menuStart, (286, 100))
        window.blit(menuExit, (282, 120))
        window.blit(menuDevMode, (550, 460))
        pygame.display.flip()

# GAME #
if gameLoop == True:
    # Settings #
    pygame.key.set_repeat(30, 30)
    # Variables #
    gameBg = Background("Images/space2.jpg", 0, 0)
    player = Player("Images/surf0.png", ["Images/surf1.png", "Images/surf2.png", "Images/surf3.png"], 0, 0)
    mob = Mob("Images/mob.png", 640, randint(0, 430), "default")
    asteroid1 = Mob("Images/asteroid1.png", 640, randint(0, 430), "asteroid1")
    asteroid2 = Mob("Images/asteroid2.png", 640, randint(0, 430), "asteroid2")
    asteroid3 = Mob("Images/asteroid3.png", 640, randint(0, 430), "asteroid3")
    asteroid4 = Mob("Images/asteroid4.png", 640, randint(0, 430), "asteroid4")
    gameScore = Score("Images/gameScore.png", "Images/Numbers/0.png", "Images/Numbers/1.png", "Images/Numbers/2.png", "Images/Numbers/3.png", "Images/Numbers/4.png", "Images/Numbers/5.png", "Images/Numbers/6.png", "Images/Numbers/7.png", "Images/Numbers/8.png", "Images/Numbers/9.png")
    score = 0
    pygame.mixer.music.load("Sound/Gravity_Original.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    # Pre-Updates #
    window.blit(gameBg.img, (gameBg.posX, gameBg.posY))
    window.blit(player.dir, (player.posX, player.posY))
    window.blit(mob.img, (mob.posX, mob.posY))
    gameScore.displayScore(window, score)
    resetBoxes([player, mob, asteroid1, asteroid2, asteroid3, asteroid4])
    pygame.display.flip()

# GAME LOOP #
while gameLoop == True:
    # Events #
    for event in pygame.event.get():
        # Keys #
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameLoop = False
                pygame.mixer.music.stop()
                pygame.display.quit()
            elif event.key == K_LEFT:
                player.move("left")
            elif event.key == K_RIGHT:
                player.move("right")
            elif event.key == K_UP:
                player.move("up")
            elif event.key == K_DOWN:
                player.move("down")
        # Others #
        elif event.type == QUIT:
            gameLoop = False
            pygame.mixer.music.stop()
            pygame.display.quit()
        else:
            player.move("idle")
    gameBg.move()
    mob.move(player)
    if score > 1500:
        asteroid1.move(player)
    if score > 5000:
        asteroid2.move(player)
    if score > 10000:
        asteroid3.move(player)
    if score > 15000:
        asteroid4.move(player)
    score += 1
    # Updates #
    if gameLoop != False:
        window.blit(gameBg.img, (gameBg.posX, gameBg.posY))
        window.blit(player.dir, (player.posX, player.posY))
        window.blit(mob.img, (mob.posX, mob.posY))
        if score > 1500:
            window.blit(asteroid1.img, (asteroid1.posX, asteroid1.posY))
        if score > 5000:
            window.blit(asteroid2.img, (asteroid2.posX, asteroid2.posY))
        if score > 10000:
            window.blit(asteroid3.img, (asteroid3.posX, asteroid3.posY))
        if score > 15000:
            window.blit(asteroid4.img, (asteroid4.posX, asteroid4.posY))
        gameScore.displayScore(window, score)
        #BoxesDraw
        if (devMode):
            pygame.draw.rect(window, (255, 0, 0), mob.box)
            pygame.draw.rect(window, (255, 0, 0), asteroid1.box)
            pygame.draw.rect(window, (255, 0, 0), asteroid2.box)
            pygame.draw.rect(window, (255, 0, 0), asteroid3.box)
            pygame.draw.rect(window, (255, 0, 0), asteroid4.box)
            pygame.draw.rect(window, (255, 0, 0), player.box)
        pygame.display.flip()
        if pygame.mixer.music.get_busy() != True and mainLoop != False:
            pygame.mixer.music.play()