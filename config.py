from terminoes import *
from resources import *

class config:

    def __init__(self, H, W, locked, allPiece, allColors, curPiece, nxtPiece, r, run, score, speed, _go):
        self.H = H
        self.W = W
        self.locked = locked
        self.allPiece = allPiece
        self.allColors = allColors
        self.curPiece = curPiece
        self.nxtPiece = nxtPiece
        self.r = r
        self.run = run
        self.score = score
        self.speed = speed
        self.gameOver = _go

    def update(self, _H, _W,  _locked, _curPiece, _nxtPiece, _r, _score, _speed, _go):
        self.H = _H
        self.W = _W
        self.locked = _locked
        self.curPiece = _curPiece
        self.nxtPiece = _nxtPiece
        self.r = _r
        self.score = _score
        self._speed = _speed
        self.gameOver = _go

    def reset(self):
        self.H = H
        self.W = W
        self.locked = locked
        self.curPiece = curPiece
        self.nxtPiece = nxtPiece
        self.r = r
        self.score = score
        self._speed = speed

    def getHeight(self):
        return self.H

    def setHeight(self, _H):
        self.H = -H

    def getWidth(self):
        return self.W

    def setWidth(self, _W):
        self.W = _W

    def getlocked(self):
        return self.locked
    
    def getTetraminoes(self):
        return self.allPiece, self.allColors
    
    def getPieces(self):
        return self.curPiece, self.nxtPiece
    
    def gamests(self):
        return self.gameOver
    
    def getscore(self):
        return self.score
    
    def getspeed(self):
        return self.speed