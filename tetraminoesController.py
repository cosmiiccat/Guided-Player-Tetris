from config import *
from ghostPieces import *
import pygame
import random as rn

pygame.init()
surface = pygame.display.set_mode((W + 50, H))
pygame.display.set_caption('Tetris Game')

gameOver = 0

class tetraminoesController(GhostPieces):

    def __init__(self, inc, H, W, locked, allPiece, allColors, curPiece, nxtPiece, r, run, score, speed, gameOver):
        # super().__init__(inc)
        super().__init__(inc, H, W, locked, allPiece, allColors, curPiece, nxtPiece, r, run, score, speed,  gameOver)
        self.inc = inc

    def removeFilled(self, score):
    # global score
        iterColumn = 380; iterRow = 680

        while  iterRow >= 50:
            sts = 0
            # counter = 0
            while iterColumn >= 50:
                if (iterRow, iterColumn) not in self.locked:
                    sts = 1
                # else:  
                    # counter += 1
                    # print(counter)
                iterColumn -= 30

            if sts == 0:
                self.score += 1
                repColumn = 380; repRow = iterRow
                while repRow  > 50:
                    while repColumn >= 50:
                        if (repRow, repColumn) in self.locked:
                            del self.locked[(repRow, repColumn)]
                        pygame.draw.rect(surface, (80, 0, 115), (repColumn, repRow, self.inc-4, self.inc-4), border_radius=7)
                        if (repRow-30, repColumn) in self.locked:
                            pygame.draw.rect(surface, self.locked[(repRow-30, repColumn)], (repColumn, repRow, self.inc-4, self.inc-4), border_radius=7)
                            self.locked[(repRow, repColumn)] = self.locked[(repRow-30, repColumn)]
                        repColumn -= 30
                    repRow -= 30
                    repColumn = 380
            iterColumn = 380
            iterRow -= 30

        return self.score
    
    def pieceFall(self, curH, curW, curEvent, score):
        global curPiece
        global nxtPiece
        global r
        global gameOver
        global speed

        curH += self.inc

        if curEvent == 1 and curW > 50:
            sts = 1
            for modifier in self.allPiece[self.curPiece][self.r]:
                # print(curPiece, " ", r)
                if curW + modifier[1]*self.inc <= 50:
                    sts = 0
            if sts == 1:
                curW -= self.inc
                curH -= self.inc
        if curEvent == 2 and curW < 370: 
            sts = 1
            for modifier in self.allPiece[self.curPiece][self.r]:
                # print(curPiece, " ", r)
                if curW + modifier[1]*self.inc >= 370:
                    sts = 0
            if sts == 1:
                curW += self.inc
                curH -= self.inc

        if curEvent == 3:
            sts = 1
            rTemp = r
            if r == len(self.allPiece[self.curPiece]) - 1:
                rTemp = 0
            else:
                rTemp += 1

            for modifier in self.allPiece[self.curPiece][rTemp]:
                if (curW + self.inc*modifier[1]) < 50 or  (curW + self.inc*modifier[1]) > 370 or ((curH + self.inc*modifier[0], curW + self.inc*modifier[1]) in self.locked):
                    sts = 0

            if sts == 1:
                if r == len(self.allPiece[self.curPiece]) - 1:
                    r = 0
                else:
                    r += 1

        sts = 1
        for modifier in self.allPiece[self.curPiece][self.r]:
            # print(curPiece, " ", r)
            if (curH + self.inc*modifier[0], curW + self.inc*modifier[1]) in self.locked:
                sts = 0
        if (curH, curW) in self.locked:
            sts = 0

        sts2 = 1
        for modifier in self.allPiece[self.curPiece][self.r]:
            # print(curPiece, " ", r)
            if (curH + self.inc*modifier[0]) > 700:
                sts2 = 0
        if curH > 700:
            sts2 = 0

        if sts2 == 0 or sts == 0:
            # print("true")
            if curH - self.inc == 50:
                gameOver = 1
            self.locked[(curH - self.inc, curW)] = self.allColors[self.curPiece]
            for modifier in self.allPiece[self.curPiece][self.r]:
                # print(curPiece, " ", r)
                self.locked[(curH - self.inc + modifier[0]*self.inc, curW + modifier[1]*self.inc)] =self.allColors[self.curPiece]
                if curH - self.inc + modifier[0]*self.inc == 50:
                    gameOver = 1
            for modifier in self.allPiece[self.curPiece][self.r]:
                # print(curPiece, " ", r)
                pygame.draw.rect(surface, self.locked[(curH - self.inc + modifier[0]*self.inc, curW + modifier[1]*self.inc)], (curW + modifier[1]*self.inc, curH + modifier[0]*self.inc - self.inc, self.inc-4, self.inc-4), border_radius=7)

            pygame.draw.rect(surface, self.locked[(curH - self.inc, curW)], (curW, curH - self.inc, self.inc-4, self.inc-4), border_radius=7)
            # curPiece = rn.randint(0, 6)
            curPiece = nxtPiece
            nxtPiece = rn.randint(0, 6)
            curH = 50
            curW = 180 + 50
            r = 0
        
        for modifier in self.allPiece[self.curPiece][self.r]:
            # print(curPiece, " ", r)
            # print(modifier)
            pygame.draw.rect(surface, self.allColors[self.curPiece], (curW + modifier[1]*self.inc, curH + modifier[0]*self.inc, self.inc-4, self.inc-4), border_radius=7)
        pygame.draw.rect(surface, self.allColors[self.curPiece], (curW, curH, self.inc-4, self.inc-4), border_radius=7)
        self.score = self.removeFilled(self.score)
        self.ghostPieces(curH, curW)
        self.update(H, W, locked, curPiece, nxtPiece, r, score, speed, gameOver)
        pygame.time.wait((int)(self.speed))
        return curH, curW, self.score
    
    def drawGrid(self):
        self.inc = 30
        curH = 50; curW = 50
        while curH < 700:
            while curW < 400:
                if (curH, curW) in self.locked:
                    # print("true grid")
                    pygame.draw.rect(surface, self.locked[(curH, curW)], (curW, curH, self.inc-4, self.inc-4), border_radius=7)
                else:
                    pygame.draw.rect(surface, (80, 0, 115), (curW, curH, self.inc-4, self.inc-4), border_radius=7)
                curW += self.inc
            curW = 50
            curH += self.inc
        # pygame.draw.rect(surface, (128, 0, 128), (curW + inc, curH, inc, inc))

    def nextPiece(self):

        pygame.draw.rect(surface, self.allColors[nxtPiece], (520, 400, self.inc-4, self.inc-4), border_radius=7)
        for modifier in self.allPiece[self.nxtPiece][0]:
            pygame.draw.rect(surface, self.allColors[nxtPiece], (520 + self.inc*modifier[1], 400 + self.inc*modifier[0], self.inc-4, self.inc-4), border_radius=7)


