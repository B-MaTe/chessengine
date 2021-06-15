import pygame as p
from settings import Settings

p.init()

class Table:

    def __init__(self):
        self.HEIGHT = 800
        self.WIDTH = 800
        self.screen = p.display.set_mode([self.HEIGHT, self.WIDTH])
        self.running = True
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.settings = Settings()
        self.addon = self.settings.addon

    def getTableRect(self, posX, posY):
        rect = p.Rect(posX, posY, self.addon, self.addon)

        return rect

    def drawTable(self):
        for i in range(1,9):
            if i % 2 == 0:
                tableColor = self.white
            else: tableColor = self.black
            for j in range(1,9):
                p.draw.rect(self.screen, tableColor, self.getTableRect(j*self.addon, i*self.addon))
                if tableColor == self.black:
                    tableColor = self.white
                else:
                    tableColor = self.black

    def drawBorder(self):
        color = self.black
        for k in range(2):
            p.draw.rect(self.screen, color, p.Rect(self.addon, self.addon+k*640, 640, 5))
            p.draw.rect(self.screen, color, p.Rect(self.addon+k*640, self.addon, 5, 645))
        
        
    def run(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False

        self.screen.fill((255, 255, 255))
        self.drawTable()
        self.drawBorder()
        p.display.flip()

p.quit()