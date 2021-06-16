import pygame as p
import os.path
from settings import Settings

class Piece(p.sprite.Sprite):
    def __init__(self, piece, color):
        super().__init__()
        self.settings = Settings()
        self.piece = piece
        self.color = color
        self.addon = self.settings.addon
        self.screen = self.settings.screen
        self.image = p.image.load(self.getImagePath())
        self.image = p.transform.scale(self.image, (self.settings.addon - int(self.settings.addon * 0.2), self.settings.addon - int(self.settings.addon * 0.1)))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x
        self.y = self.rect.y

    def getImagePath(self):
        filepath = os.path.dirname(__file__)
        return os.path.join(filepath, "pieces", self.color + self.piece + ".png")


    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False
    

    def checkHit(self, piece, group):
        try:
            collidedPiece = p.sprite.spritecollide(piece, group, False)[1]
            print("Collided")
            if piece.color != collidedPiece.color:
                collidedPiece.kill()
            else:
                print("same")

        except:
            return False
    