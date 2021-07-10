import pygame as p

class Settings:
    def __init__(self):
        self.dark = (80,60,80)
        self.bright = (255,255,255)
        self.boardSize = 1000
        self.screen = p.display.set_mode((0, 0), p.FULLSCREEN)
        self.addon = 460 # width / 2 - boardWidth / 2
        self.heightOptimizer = 4
        self.cellWidth = int(self.boardSize * 0.2 / 2)
        self.borderColor = self.dark
        self.fps = 60
        self.running = True
        self.pieceSquare = (65, 203, 149)
        self.moveableSquares = (197, 215, 222)
        self.boardLetters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.boardNums = ["1", "2", "3", "4", "5", "6", "7", "8"]