import pygame
import random as rn
import numpy as np
from terminoes import S, Z, I, O, J, L, T
from resources import *
from config import *
from ghostPieces  import GhostPieces
from tetraminoesController import tetraminoesController

pygame.init()
surface = pygame.display.set_mode((W + 50, H))
pygame.display.set_caption('Tetris Game')
font = pygame.font.Font('freesansbold.ttf', 32)

gameOver = 0

def buttonNames(x, y, content):
    text = font.render(content, True, (255, 255, 255))
    surface.blit(text, (x, y))

def main(level):
    global score
    global run
    global locked
    global speed
    global curPiece
    global  nxtPiece
    
    score = 0

    speed /= level
    run = True
    curH = 50; curW = 180 + 50
    global gameOver
    curPiece = rn.randint(0, 6)
    nxtPiece = rn.randint(0, 6)
    r = 0

    controller = tetraminoesController(30, H, W, locked, allPiece, allColors, curPiece, nxtPiece, r, run, score, speed, gameOver)
    controller.gameOver = 0
    
    curEvent = -1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    curEvent = 1
                elif event.key == pygame.K_RIGHT:
                    curEvent = 2
                elif event.key == pygame.K_UP:
                    curEvent = 3
                elif event.key == pygame.K_DOWN:
                    curEvent = 4

        # pygame.draw.rect()
        surface.fill((50, 0, 100))
        pygame.draw.rect(surface, (50, 200, 0), (42, 42, 370, 670), width = 2, border_radius=9)
        buttonNames(500, 200, "Next")
        buttonNames(500, 230, "Piece")
        controller.nextPiece()
        buttonNames(500, 500, "Score")
        buttonNames(500, 550, str(score))

        controller.drawGrid()
        curH, curW, score = controller.pieceFall(curH, curW, curEvent, score)
        curEvent = -1
        # print(curH)
        if controller.gameOver == 1:
            break
        pygame.display.update()

    outro()
    return 1

def outro():

    global run
    img = pygame.image.load("gameover.webp").convert()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        surface.fill((0, 0, 0))
        surface.blit(img, (-25, 0))

        mousePress = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()

        pygame.draw.rect(surface, (0, 255, 0), (200, 540, 250, 100), border_radius=9)
        pygame.draw.rect(surface, (112,128,144), (200, 540, 250, 100), border_radius=9)

        buttonNames(200 + 43, 540 + 40, "Play")
        buttonNames(200 + 123, 540 + 40, "Again")

        buttonNames(250, 460, "Score: " + str(score))

        buttonNames(190, 680, "With Great Efforts")
        buttonNames(165, 720, "Comes Great Success")


        if 540 < mousePos[1] < 640 and 220 < mousePos[0] < 470:
            pygame.draw.rect(surface, (50,  0, 100), (200, 540, 250, 100), border_radius=9)
            pygame.draw.rect(surface, (50, 200, 0), (200 - 10, 540 - 5, 270, 110), border_radius=9)
            buttonNames(200 + 43, 540 + 40, "Play")
            buttonNames(200 + 123, 540 + 40, "Again")

            

            if mousePress[0]:
                intro()
                run =  False

        pygame.display.update()
    
    intro()
    return 0

def intro():

    pygame.time.wait(500)
    global run
    sts = 0
    img = pygame.image.load("doodle.webp").convert()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mousePress = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()

        surface.fill((50, 0, 100))
        # img = pygame.transform.scale(img, (400,1000))
        surface.blit(img, (0, 0))

        # (112,128,144)

        pygame.draw.rect(surface, (0, 255, 0), (220, 120, 200, 100), border_radius=9)
        pygame.draw.rect(surface, (112,128,144), (220, 120, 200, 100), border_radius=9)

        buttonNames(220 + 60, 120 + 40, "Easy")

        pygame.draw.rect(surface, (255, 165, 0), (220, 330, 200, 100), border_radius=9)
        pygame.draw.rect(surface, (112,128,144), (220, 330, 200, 100), border_radius=9)

        buttonNames(220 + 40, 330 + 40, "Medium")

        pygame.draw.rect(surface, (255, 50, 0), (220, 540, 200, 100), border_radius=9)
        pygame.draw.rect(surface, (112,128,144), (220, 540, 200, 100), border_radius=9)

        buttonNames(220 + 60, 540 + 40, "Hard")

        if 120 < mousePos[1] < 220 and 220 < mousePos[0] < 420:
            pygame.draw.rect(surface, (50,  0, 100), (220, 120, 200, 100), border_radius=9)
            pygame.draw.rect(surface, (50, 200, 0), (220 - 10, 120 - 5, 220, 110), border_radius=9)
            buttonNames(220 + 60, 120 + 40, "Easy")

            if mousePress[0]:
                main(1)

        elif 330 < mousePos[1] < 530 and 220 < mousePos[0] < 420:
            pygame.draw.rect(surface, (50,  0, 100), (220, 330, 200, 100), border_radius=9)
            pygame.draw.rect(surface, (200, 150, 30), (220 - 10, 330 - 5, 220, 110), border_radius=9)
            buttonNames(220 + 40, 330 + 40, "Medium")

            if mousePress[0]:
                main(2)

        elif 540 < mousePos[1] < 640 and 220 < mousePos[0] < 420:
            pygame.draw.rect(surface, (50,  0, 100), (220, 540, 200, 100), border_radius=9)
            pygame.draw.rect(surface, (220, 50, 50), (220 - 10, 540 - 5, 220, 110), border_radius=9)
            buttonNames(220 + 60, 540 + 40, "Hard")

            if mousePress[0]:
                main(3)

        # if sts == 1:
        #     sts = outro()

        pygame.display.update()

def welcome():
    global run
    img = pygame.image.load("tetris.webp").convert()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        surface.fill((0, 0, 0))
        img = pygame.transform.scale(img, (700,600))
        surface.blit(img, (0, 0))

        mousePress = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()

        pygame.draw.rect(surface, (0, 255, 0), (220, 540, 250, 100), border_radius=9)
        pygame.draw.rect(surface, (112,128,144), (220, 540, 250, 100), border_radius=9)

        buttonNames(220 + 43, 540 + 40, "Start")
        buttonNames(220 + 129, 540 + 40, "Play")

        if 540 < mousePos[1] < 640 and 220 < mousePos[0] < 470:
            pygame.draw.rect(surface, (50,  0, 100), (220, 540, 250, 100), border_radius=9)
            pygame.draw.rect(surface, (50, 200, 0), (220 - 10, 540 - 5, 270, 110), border_radius=9)

            buttonNames(220 + 43, 540 + 40, "Start")
            buttonNames(220 + 129, 540 + 40, "Play")

            if mousePress[0]:
                intro()
                # run =  False

        pygame.display.update()
        

if __name__ == "__main__":
    # main(3)
    # intro()
    # outro()
    welcome()
