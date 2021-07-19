import pygame as p
from settings import Settings
from random import choice
from pieces import Piece


class Computer:
    
    def __init__(self, color, level):
        self.color = color
        self.level = level
        self.settings = Settings()
        
        
    def getPieceWorth(self, pieces):
        whiteW = 0
        blackW = 0
        for piece in pieces:
            x, y = piece.getCurrentPos(piece.rect.x, piece.rect.y)
            if piece.color == "w":
                whiteW += self.settings.pieceWorthW[piece.piece] + self.settings.nameTranslatorW[piece.piece][x + y * 8]
            else:
                blackW += self.settings.pieceWorthB[piece.piece] + self.settings.nameTranslatorB[piece.piece][x + y * 8]
        
        return whiteW, -blackW
    
        
    def getSingelPieceWorth(self, piece):
        x, y = piece.getCurrentPos(piece.rect.x, piece.rect.y)
        if piece.color == "w":
            return self.settings.pieceWorthW[piece.piece] + self.settings.nameTranslatorW[piece.piece][x + y * 8]
        return self.settings.pieceWorthB[piece.piece] + self.settings.nameTranslatorB[piece.piece][x + y * 8]
    def randomLogic(self, moves):
        piece = choice(moves)
        if len(piece) < 2:
            self.randomLogic(moves)
        return piece[0], choice(piece[1:])