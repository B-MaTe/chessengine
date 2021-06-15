import pygame as p

class Settings:
    def __init__(self):
        self.dark = (60,60,60)
        self.bright = (255,255,255)
        self.boardWidth = 1200
        self.boardHeight = 1000
        self.screen = p.display.set_mode([self.boardWidth, self.boardHeight])
        self.addon = int(self.boardHeight * 0.2 / 2)
        self.borderColor = self.dark
        self.fps = 60
        self.running = True

        # PIECES STARTING POSITIONS
        self.wKingX, self.wKingY = 5 * self.addon, self.addon * 8
        self.wQueenX, self.wQueenY = 4 * self.addon, self.addon * 8