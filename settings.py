import pygame as p

class Settings:
    def __init__(self):
        self.dark = (75, 39, 0)
        self.bright = (255, 244, 204)
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
        
        #### PIECE WORTH
        
        self.pieceWorthW = {
            "pawn" : 10.0,
            "bishop" : 30.0,
            "knight" : 30.0,
            "rook" : 50.0,
            "queen" : 90.0,
            "king" : 900.0
        }
        
        self.pieceWorthB = {
            "pawn" : 10.0,
            "bishop" : 30.0,
            "knight" : 30.0,
            "rook" : 50.0,
            "queen" : 90.0,
            "king" : 900.0
        }
        
        
        
        #### POSITIONAL WORTHS
        
        self.pawnPosW = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
            1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 2.0, 1.0,
            0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
            0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
            0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
            0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        ]
        
        self.pawnPosB = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
            0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
            0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
            0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
            1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 2.0, 1.0,
            5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        ]
        
        self.knightPosW = [
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
            -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
            -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
           -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
            -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
            -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
            -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        ]
        
        self.knightPosB = [
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
            -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
            -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
            -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
           -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
            -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
            -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        ]
        
        self.bishopPosW = [
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
            -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
            -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
            -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
            -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
            -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
            -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        ]
        
        self.bishopPosB = [
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
            -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
            -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
            -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
            -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
            -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
            -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        ]
        
        self.rookPosW = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
           -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0,
        ]
        
        self.rookPosB = [
            0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        ]
        
        self.queenPosW = [
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
            -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
            -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
            -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
            0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
            -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
            -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        ]
        
        self.queenPosB = [
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
            -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
            -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
            0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
            -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
           -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
            -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        ]
        
        self.kingPosW = [
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0,-2.0,
            -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0,-1.0,
            2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
            2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0,
        ]
        
        self.kingPosB = [
            2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0,
            2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
            -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0,-1.0,
            -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0,-2.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0,-3.0,
        ]
        
        
        self.nameTranslatorW = {
            "pawn" : self.pawnPosW,
            "bishop" : self.bishopPosW,
            "knight" : self.knightPosW,
            "rook" : self.rookPosW,
            "queen" : self.queenPosW,
            "king" : self.kingPosW,
        }
        
        self.nameTranslatorB = {
            "pawn" : self.pawnPosB,
            "bishop" : self.bishopPosB,
            "knight" : self.knightPosB,
            "rook" : self.rookPosB,
            "queen" : self.queenPosB,
            "king" : self.kingPosB,
        }