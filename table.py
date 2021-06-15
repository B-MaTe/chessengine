import pygame as p
from settings import Settings
from pieces import Piece

p.init()

class Table:

    def __init__(self):
        self.settings = Settings()

        #### PIECES
        self.pawns = p.sprite.Group()
        self.rooks = p.sprite.Group()
        self.bishops = p.sprite.Group()
        self.knights = p.sprite.Group()
        self.queens = p.sprite.Group()
        self.kings = p.sprite.Group()
        ##########
        
        self.running = self.settings.running
        self.dark = self.settings.dark
        self.bright = self.settings.bright
        self.addon = self.settings.addon
        self.borderColor = self.settings.borderColor
        self.HEIGHT = self.settings.boardHeight
        self.WIDTH = self.settings.boardWidth
        self.screen = self.settings.screen
        p.display.set_caption("Chess Engine")
        self.clock = p.time.Clock()
        self.fps = self.settings.fps
        self.positionSmoother = (self.addon / 20)

        # START GAME
        self.deployPawns()
        self.deployRooks()
        self.deployKnights()
        self.deployBishops()
        self.deployQueens()
        self.deployKings()


    def getTableRect(self, posX, posY):
        rect = p.Rect(posX, posY, self.addon, self.addon)

        return rect


    def drawTable(self):
        for i in range(1,9):
            if i % 2 == 0:
                tableColor = self.bright
            else: tableColor = self.dark
            for j in range(1,9):
                p.draw.rect(self.screen, tableColor, self.getTableRect(j*self.addon, i*self.addon))
                if tableColor == self.dark:
                    tableColor = self.bright
                else:
                    tableColor = self.dark


    def drawBorder(self):
        color = self.dark
        borderColor = self.borderColor
        rectSize = self.addon * 8
        for k in range(2):
            p.draw.rect(self.screen, borderColor, p.Rect(self.addon, self.addon+k*rectSize, rectSize, 5))
            p.draw.rect(self.screen, borderColor, p.Rect(self.addon+k*rectSize, self.addon, 5, rectSize+5))


    def events(self):
        #EVENTS
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False
            if event.type == p.MOUSEBUTTONDOWN:
                x, y = p.mouse.get_pos()

 ####################
 ####   PAWNS    ####
 ####################

    def createPawn(self, pawnNum, color):
        if color == "b":
            y = 2
        else:
            y = 7
        pawn = Piece("pawn", color)
        pawn.x, pawn.y = self.addon * pawnNum + int(self.settings.addon * 0.1), self.addon * y + int(self.settings.addon * 0.1) - 5
        pawn.rect.x = pawn.x
        pawn.rect.y = pawn.y
        self.pawns.add(pawn)

    def deployPawns(self):
        for pawNum in range(1, 9):
            self.createPawn(pawNum, "w")
        for pawNum in range(1, 9):
            self.createPawn(pawNum, "b")

 ####################

 ####################
 ####   ROOKS    ####
 ####################

    def createRook(self, rookNum, color):
        if color == "b":
            y = 1
        else:
            y = 8
        rook = Piece("rook", color)
        rook.x, rook.y = self.addon * rookNum + int(self.settings.addon * 0.1), self.addon * y + int(self.settings.addon * 0.1) - 5
        rook.rect.x = rook.x
        rook.rect.y = rook.y
        self.rooks.add(rook)

    def deployRooks(self):
        for rookNum in range(1, 9, 7):
            self.createRook(rookNum, "w")
        for rookNum in range(1, 9, 7):
            self.createRook(rookNum, "b")


 ####################

 ####################
 ####  KNIGHTS   ####
 ####################

    def createKnight(self, knightNum, color):
        if color == "b":
            y = 1
        else:
            y = 8
        knight = Piece("knight", color)
        knight.x, knight.y = self.addon * knightNum + int(self.settings.addon * 0.1), self.addon * y + int(self.settings.addon * 0.1) - 5
        knight.rect.x = knight.x
        knight.rect.y = knight.y
        self.knights.add(knight)

    def deployKnights(self):
        for knightNum in range(2, 8, 5):
            self.createKnight(knightNum, "w")
        for knightNum in range(2, 8, 5):
            self.createKnight(knightNum, "b")


 ####################


####################
####  BISHOPS   ####
####################

    def createBishop(self, bishopNum, color):
        if color == "b":
            y = 1
        else:
            y = 8
        bishop = Piece("bishop", color)
        bishop.x, bishop.y = self.addon * bishopNum + int(self.settings.addon * 0.1), self.addon * y + int(self.settings.addon * 0.1) - 5
        bishop.rect.x = bishop.x
        bishop.rect.y = bishop.y
        self.bishops.add(bishop)

    def deployBishops(self):
        for bishopNum in range(3, 7, 3):
            self.createBishop(bishopNum, "w")
        for bishopNum in range(3, 7, 3):
            self.createBishop(bishopNum, "b")


####################

####################
####   KINGS    ####
####################

    def createKings(self, kingNum, color):
        if color == "b":
            y = 1
        else:
            y = 8
        king = Piece("king", color)
        king.x, king.y = self.addon * kingNum + int(self.settings.addon * 0.1), self.addon * y + int(self.settings.addon * 0.1) - 5
        king.rect.x = king.x
        king.rect.y = king.y
        self.kings.add(king)

    def deployKings(self):
        self.createKings(5, "w")
        self.createKings(5, "b")


####################

####################
####   QUEENS   ####
####################

    def createQueens(self, queenNum, color):
        if color == "b":
            y = 1
        else:
            y = 8
        queen = Piece("queen", color)
        queen.x, queen.y = self.addon * queenNum + int(self.settings.addon * 0.1), self.addon * y + int(self.settings.addon * 0.1) - 5
        queen.rect.x = queen.x
        queen.rect.y = queen.y
        self.queens.add(queen)

    def deployQueens(self):
        self.createQueens(4, "w")
        self.createQueens(4, "b")


####################



    def updatePieces(self):
        self.pawns.update()
        self.rooks.update()
        self.knights.update()
        self.bishops.update()
        self.queens.update()
        self.kings.update()
        
               
    def run(self):

        # SCREEN
        self.screen.fill((255, 255, 255))

        # TABLE
        self.drawTable()
        self.drawBorder()

        


        # PIECES
        self.pawns.draw(self.screen)
        self.rooks.draw(self.screen)
        self.knights.draw(self.screen)
        self.bishops.draw(self.screen)
        self.queens.draw(self.screen)
        self.kings.draw(self.screen)
        self.updatePieces()



        
        #MOVE


        #FPS, FLIP
        p.display.flip()
        self.clock.tick(self.fps)

   
p.quit()