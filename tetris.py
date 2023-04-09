import pygame
import random as rn
from terminoes import S, Z, I, O, J, L, T

H = 800; W = 600
locked = dict()
allPiece = [S, Z, I, O, J, L, T]
allColors = [(144,238,144), (0,255,255), (255,0,255), (230,230,250), (255,99,71), (255,0,0), (30,144,255)]
# curPiece = rn.randint(0, 6)
curPiece =  2
nxtPiece = 2
r = 0
gameOver = 0
run = True
score = 0
speed = 300

pygame.init()
surface = pygame.display.set_mode((W + 50, H))
pygame.display.set_caption('Tetris Game')

font = pygame.font.Font('freesansbold.ttf', 32)

def buttonNames(x, y, content):
    text = font.render(content, True, (255, 255, 255))
    surface.blit(text, (x, y))

def ghostPieces(surface, curH, curW):
    sts =  0
    ghostH = curH
    # curH += 30
    while curH < 700:
        curH += inc
        sts = 0
        for modifier in allPiece[curPiece][r]:
            if (curH + inc*modifier[0], curW + inc*modifier[1]) in locked:
                sts = 1
                break
        if (curH, curW) in locked:
            sts = 1
            break
        if sts ==  0:
            ghostH = curH
    if ghostH + 30 > 700:
        ghostH -= inc
    for modifier in allPiece[curPiece][r]:
    # print(curPiece, " ", r)
        pygame.draw.rect(surface, (255, 0,  0), (curW + modifier[1]*inc, ghostH + modifier[0]*inc, inc-4, inc-4), border_radius=7, width = 1)

    pygame.draw.rect(surface, (255, 0, 0), (curW, ghostH, inc-4, inc-4), border_radius=7, width = 1)


def removeFilled(surface):
    global score
    iterColumn = 380; iterRow = 680

    while  iterRow >= 50:
        sts = 0
        # counter = 0
        while iterColumn >= 50:
            if (iterRow, iterColumn) not in locked:
                sts = 1
            # else:  
                # counter += 1
                # print(counter)
            iterColumn -= 30

        if sts == 0:
            score += 1
            repColumn = 380; repRow = iterRow
            while repRow  > 50:
                while repColumn >= 50:
                    if (repRow, repColumn) in locked:
                        del locked[(repRow, repColumn)]
                    pygame.draw.rect(surface, (80, 0, 115), (repColumn, repRow, inc-4, inc-4), border_radius=7)
                    if (repRow-30, repColumn) in locked:
                        pygame.draw.rect(surface, locked[(repRow-30, repColumn)], (repColumn, repRow, inc-4, inc-4), border_radius=7)
                        locked[(repRow, repColumn)] = locked[(repRow-30, repColumn)]
                    repColumn -= 30
                repRow -= 30
                repColumn = 380
        iterColumn = 380
        iterRow -= 30

def pieceFall(surface, curH, curW, curEvent):
    global curPiece
    global nxtPiece
    global r
    global gameOver
    global speed
    curH += inc

    if curEvent == 1 and curW > 50:
        sts = 1
        for modifier in allPiece[curPiece][r]:
            # print(curPiece, " ", r)
            if curW + modifier[1]*inc <= 50:
                sts = 0
        if sts == 1:
            curW -= inc
            curH -= inc
    if curEvent == 2 and curW < 370: 
        sts = 1
        for modifier in allPiece[curPiece][r]:
            # print(curPiece, " ", r)
            if curW + modifier[1]*inc >= 370:
                sts = 0
        if sts == 1:
            curW += inc
            curH -= inc

    if curEvent == 3:
        sts = 1
        rTemp = r
        if r == len(allPiece[curPiece]) - 1:
            rTemp = 0
        else:
            rTemp += 1

        for modifier in allPiece[curPiece][rTemp]:
            if (curW + inc*modifier[1]) < 50 or  (curW + inc*modifier[1]) > 370 or ((curH + inc*modifier[0], curW + inc*modifier[1]) in locked):
                sts = 0

        if sts == 1:
            if r == len(allPiece[curPiece]) - 1:
                r = 0
            else:
                r += 1

    sts = 1
    for modifier in allPiece[curPiece][r]:
        # print(curPiece, " ", r)
        if (curH + inc*modifier[0], curW + inc*modifier[1]) in locked:
            sts = 0
    if (curH, curW) in locked:
        sts = 0

    sts2 = 1
    for modifier in allPiece[curPiece][r]:
        # print(curPiece, " ", r)
        if (curH + inc*modifier[0]) > 700:
            sts2 = 0
    if curH > 700:
        sts2 = 0

    if sts2 == 0 or sts == 0:
        # print("true")
        if curH - inc == 50:
            gameOver = 1
        locked[(curH - inc, curW)] = allColors[curPiece]
        for modifier in allPiece[curPiece][r]:
            # print(curPiece, " ", r)
            locked[(curH - inc + modifier[0]*inc, curW + modifier[1]*inc)] = allColors[curPiece]
            if curH - inc + modifier[0]*inc == 50:
                gameOver = 1
        for modifier in allPiece[curPiece][r]:
            # print(curPiece, " ", r)
            pygame.draw.rect(surface, locked[(curH - inc + modifier[0]*inc, curW + modifier[1]*inc)], (curW + modifier[1]*inc, curH + modifier[0]*inc - inc, inc-4, inc-4), border_radius=7)

        pygame.draw.rect(surface, locked[(curH - inc, curW)], (curW, curH - inc, inc-4, inc-4), border_radius=7)
        # curPiece = rn.randint(0, 6)
        curPiece = nxtPiece
        nxtPiece = rn.randint(0, 6)
        curH = 50
        curW = 180 + 50
        r = 0
    
    for modifier in allPiece[curPiece][r]:
        # print(curPiece, " ", r)
        # print(modifier)
        pygame.draw.rect(surface, allColors[curPiece], (curW + modifier[1]*inc, curH + modifier[0]*inc, inc-4, inc-4), border_radius=7)
    pygame.draw.rect(surface, allColors[curPiece], (curW, curH, inc-4, inc-4), border_radius=7)
    removeFilled(surface)
    ghostPieces(surface, curH, curW)
    pygame.time.wait((int)(speed))
    return curH, curW

def drawGrid(surface):
    global inc
    inc = 30
    curH = 50; curW = 50
    while curH < 700:
        while curW < 400:
            if (curH, curW) in locked:
                # print("true grid")
                pygame.draw.rect(surface, locked[(curH, curW)], (curW, curH, inc-4, inc-4), border_radius=7)
            else:
                pygame.draw.rect(surface, (80, 0, 115), (curW, curH, inc-4, inc-4), border_radius=7)
            curW += inc
        curW = 50
        curH += inc
    # pygame.draw.rect(surface, (128, 0, 128), (curW + inc, curH, inc, inc))


def nextPiece(surface):
    inc = 30

    pygame.draw.rect(surface, allColors[nxtPiece], (520, 400, inc-4, inc-4), border_radius=7)
    for modifier in allPiece[nxtPiece][0]:
        pygame.draw.rect(surface, allColors[nxtPiece], (520 + inc*modifier[1], 400 + inc*modifier[0], inc-4, inc-4), border_radius=7)
    

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
    gameOver = 0
    locked = dict()
    curPiece = rn.randint(0, 6)
    nxtPiece = rn.randint(0, 6)
    r = 0
    # global locked 
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
        nextPiece(surface)
        buttonNames(500, 500, "Score")
        buttonNames(500, 550, str(score))


        drawGrid(surface)
        curH, curW = pieceFall(surface, curH, curW, curEvent)
        curEvent = -1
        if gameOver == 1:
            break
        pygame.display.update()
        # print(locked.keys())
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