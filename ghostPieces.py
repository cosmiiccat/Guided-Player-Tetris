from config import *
import pygame

pygame.init()
surface = pygame.display.set_mode((W + 50, H))
pygame.display.set_caption('Tetris Game')

class GhostPieces(config):

    def __init__(self, inc, H, W, locked, allPiece, allColors, curPiece, nxtPiece, r, run, score, speed, gameOver):
        super().__init__(H, W, locked, allPiece, allColors, curPiece, nxtPiece, r, run, score, speed, gameOver)
        self.inc = inc

    def ghostPieces(self, curH, curW):
        sts =  0
        ghostH = curH
        # curH += 30
        while curH < 700:
            curH += self.inc
            sts = 0
            for modifier in self.allPiece[self.curPiece][self.r]:
                if (curH + self.inc*modifier[0], curW + self.inc*modifier[1]) in self.locked:
                    sts = 1
                    break
            if (curH, curW) in self.locked:
                sts = 1
            if sts ==  0:
                ghostH = curH
        if ghostH + 30 > 700:
            ghostH -= self.inc
        for modifier in self.allPiece[self.curPiece][self.r]:
        # print(curPiece, " ", r)
            pygame.draw.rect(surface, (255, 0,  0), (curW + modifier[1]*self.inc, ghostH + modifier[0]*self.inc, self.inc-4, self.inc-4), border_radius=7, width = 1)

        pygame.draw.rect(surface, (255, 0, 0), (curW, ghostH, self.inc-4, self.inc-4), border_radius=7, width = 1)