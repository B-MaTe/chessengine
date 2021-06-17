import pygame as p
import os.path
from settings import Settings
from math import ceil

class Piece(p.sprite.Sprite):
    def __init__(self, piece, color):
        super().__init__()
        self.settings = Settings()
        self.piece = piece
        self.color = color
        self.addon = self.settings.addon
        self.cellWidth = self.settings.cellWidth
        self.boardSize = self.settings.boardSize
        self.screen = self.settings.screen
        self.image = p.image.load(self.getImagePath())
        self.image = p.transform.scale(self.image, (self.settings.cellWidth - int(self.settings.cellWidth * 0.2), self.settings.cellWidth - int(self.settings.cellWidth * 0.1)))
        self.rect = self.image.get_rect()
        self.heightOptimizer = self.settings.heightOptimizer
        self._layer = self.rect.bottom

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x
        self.y = self.rect.y

    def getImagePath(self):
        filepath = os.path.dirname(__file__)
        return os.path.join(filepath, "pieces", self.color + self.piece + ".png")

    def getCurrentPos(self, x, y):
        x -= self.addon
        y -= self.addon / self.heightOptimizer
        return int(ceil(x / 100.0))-1, int(ceil(y / 100.0))-1

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False

    def isOutofTable(self, x, y):
        tableL, tableR, tableT, tableB = self.addon, self.addon + 8*self.cellWidth, self.addon / self.heightOptimizer, self.addon / self.heightOptimizer + 8*self.cellWidth
        if x >= tableR or x <= tableL or y >= tableB or y <= tableT:
            return True
        return False

    def checkHit(self, piece, group):
        try:
            collidedPiece = p.sprite.spritecollide(piece, group, False)[0]
            #print("Collided")
            if piece.color != collidedPiece.color:
                collidedPiece.kill()
            else:
                #print("same")
                pass

        except:
            return False
    