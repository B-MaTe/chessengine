import pygame as p

class Settings:
    def __init__(self):
        self.dark = (60,60,60)
        self.bright = (255,255,255)
        self.boardSize = 1000
        self.screen = p.display.set_mode((0, 0), p.FULLSCREEN)
        self.addon = 460 # width / 2 - boardWidth / 2
        self.heightOptimizer = 4
        self.cellWidth = int(self.boardSize * 0.2 / 2)
        self.borderColor = self.dark
        self.fps = 60
        self.running = True
        self.pieceSquare = (174, 39, 37)
        self.moveableSquares = (174, 132, 104)