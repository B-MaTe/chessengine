import pygame
from table import Table

class Main:
    def __init__(self):
        self.table = Table()
        self.process()

    def process(self):
        while self.table.running:
            self.table.run()
            self.table.events()
            if self.table.restart:
                self.table.restart = False
                pygame.quit()
                Main()
                



if __name__ == '__main__':
    Main()