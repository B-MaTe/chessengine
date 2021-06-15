

import pygame
from table import Table

class Main:
    def __init__(self):
        self.table = Table()
        self.process()

    def process(self):
        while self.table.running:
            self.table.run()



if __name__ == '__main__':
    Main()