import pygame
from main import Main

class Run:
    def __init__(self):
        self.main = Main()
        self.process()

    def process(self):
        while self.main.running:
            self.main.run()
            self.main.events()
            if self.main.restart:
                self.main.restart = False
                pygame.quit()
                Run()
                



if __name__ == '__main__':
    Run()