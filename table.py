import pygame as p
from settings import Settings
from pieces import Piece
from math import ceil

p.init()

class Table:

    def __init__(self):
        self.settings = Settings()

        #### PIECES
        """
        self.pawns = p.sprite.Group()
        self.rooks = p.sprite.Group()
        self.bishops = p.sprite.Group()
        self.knights = p.sprite.Group()
        self.queens = p.sprite.Group()
        self.kings = p.sprite.Group()
        """
        self.pieces = p.sprite.LayeredUpdates()
        ##########
        self.running = self.settings.running
        self.dark = self.settings.dark
        self.bright = self.settings.bright
        self.addon = self.settings.addon
        self.borderColor = self.settings.borderColor
        self.boardSize = self.settings.boardSize
        self.cellWidth = self.settings.cellWidth
        self.screen = self.settings.screen
        p.display.set_caption("Chess Engine")
        self.clock = p.time.Clock()
        self.fps = self.settings.fps
        self.dragging = False
        self.clickedPiece = None
        self.heightOptimizer = self.settings.heightOptimizer
        self.oldX, self.oldY = None, None
        self.turn = "w"
        self.hit = False

        # START GAME
        self.deployPawns()
        self.deployRooks()
        self.deployKnights()
        self.deployBishops()
        self.deployQueens()
        self.deployKings()


    def getTableRect(self, posX, posY):

        return p.Rect(posX, posY, self.cellWidth, self.cellWidth)

        


    def drawTable(self):
        for i in range(8):
            if i % 2 == 0:
                tableColor = self.bright
            else: tableColor = self.dark
            for j in range(8):
                p.draw.rect(self.screen, tableColor, self.getTableRect(self.addon + j*self.cellWidth, self.addon / self.heightOptimizer + i*self.cellWidth))
                if tableColor == self.dark:
                    tableColor = self.bright
                else:
                    tableColor = self.dark


    def drawBorder(self):
        color = self.dark
        borderColor = self.borderColor
        rectSize = self.cellWidth * 8
        for k in range(2):
            p.draw.rect(self.screen, borderColor, p.Rect(self.addon, self.addon / self.heightOptimizer+k*rectSize, rectSize, 5))
            p.draw.rect(self.screen, borderColor, p.Rect(self.addon+k*rectSize, self.addon / self.heightOptimizer, 5, rectSize+5))


 ####################
 ####   PAWNS    ####
 ####################

    def createPawn(self, pawnNum, color):
        if color == "b":
            y = 1
        else:
            y = 6
        pawn = Piece("pawn", color)
        pawn.x, pawn.y = self.addon + self.cellWidth * pawnNum + int(self.settings.cellWidth * 0.1), self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5
        pawn.rect.x = pawn.x
        pawn.rect.y = pawn.y
        self.pieces.add(pawn)

    def deployPawns(self):
        for pawNum in range(8):
            self.createPawn(pawNum, "w")
        for pawNum in range(8):
            self.createPawn(pawNum, "b")

 ####################

 ####################
 ####   ROOKS    ####
 ####################

    def createRook(self, rookNum, color):
        if color == "b":
            y = 0
        else:
            y = 7
        rook = Piece("rook", color)
        rook.x, rook.y = self.addon + self.cellWidth * rookNum + int(self.settings.cellWidth * 0.1), self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5
        rook.rect.x = rook.x
        rook.rect.y = rook.y
        self.pieces.add(rook)

    def deployRooks(self):
        for rookNum in range(0, 8, 7):
            self.createRook(rookNum, "w")
        for rookNum in range(0, 8, 7):
            self.createRook(rookNum, "b")


 ####################

 ####################
 ####  KNIGHTS   ####
 ####################

    def createKnight(self, knightNum, color):
        if color == "b":
            y = 0
        else:
            y = 7
        knight = Piece("knight", color)
        knight.x, knight.y = self.addon + self.cellWidth * knightNum + int(self.settings.cellWidth * 0.1), self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5
        knight.rect.x = knight.x
        knight.rect.y = knight.y
        self.pieces.add(knight)

    def deployKnights(self):
        for knightNum in range(1, 7, 5):
            self.createKnight(knightNum, "w")
        for knightNum in range(1, 7, 5):
            self.createKnight(knightNum, "b")


 ####################


####################
####  BISHOPS   ####
####################

    def createBishop(self, bishopNum, color):
        if color == "b":
            y = 0
        else:
            y = 7
        bishop = Piece("bishop", color)
        bishop.x, bishop.y = self.addon + self.cellWidth * bishopNum + int(self.settings.cellWidth * 0.1), self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5
        bishop.rect.x = bishop.x
        bishop.rect.y = bishop.y
        self.pieces.add(bishop)

    def deployBishops(self):
        for bishopNum in range(2, 6, 3):
            self.createBishop(bishopNum, "w")
        for bishopNum in range(2, 6, 3):
            self.createBishop(bishopNum, "b")


####################

####################
####   KINGS    ####
####################

    def createKings(self, kingNum, color):
        if color == "b":
            y = 0
        else:
            y = 7
        king = Piece("king", color)
        king.x, king.y = self.addon + self.cellWidth * kingNum + int(self.settings.cellWidth * 0.1), self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5
        king.rect.x = king.x
        king.rect.y = king.y
        self.pieces.add(king)

    def deployKings(self):
        self.createKings(4, "w")
        self.createKings(4, "b")


####################

####################
####   QUEENS   ####
####################

    def createQueens(self, queenNum, color):
        if color == "b":
            y = 0
        else:
            y = 7
        queen = Piece("queen", color)
        queen.x, queen.y = self.addon + self.cellWidth * queenNum + int(self.settings.cellWidth * 0.1), self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5
        queen.rect.x = queen.x
        queen.rect.y = queen.y
        self.pieces.add(queen)

    def deployQueens(self):
        self.createQueens(3, "w")
        self.createQueens(3, "b")


####################

    def isValidMove(self, x, y):
        x = self.clickedPiece.getCurrentPos(x, y)[0]
        y = self.clickedPiece.getCurrentPos(x, y)[1]
        for piece in self.pieces:
            if piece != self.clickedPiece and piece.color == self.clickedPiece.color and piece.getCurrentPos(piece.rect.x, piece.rect.y)[0] == x and piece.getCurrentPos(piece.rect.x, piece.rect.y)[1] == y:
                return False
        return True

    def validateMove(self, piece, typeOfMove, hit):
        piece = piece.piece
        if piece == "knight" and typeOfMove == "L":
            return True
        elif piece == "bishop" and typeOfMove == "diagonal":
            return True
        elif piece == "rook" and (typeOfMove in ["horizontal", "vertical"]):
            return True
        elif piece == "pawn" and ((typeOfMove == "vertical") or (hit and typeOfMove == "diagonal")):
            return True
        elif piece == "queen" and (typeOfMove in ["horizontal", "vertical", "diagonal"]):
            return True
        elif piece == "king" and typeOfMove == "kingMove":
            return True
        return False

    def movePieceToNearestSquare(self, x, y):
        x -= self.addon
        y -= self.addon / self.heightOptimizer
        x, y = int(ceil(x / 100.0))-1, int(ceil(y / 100.0))-1
        self.clickedPiece.rect.x, self.clickedPiece.rect.y = self.addon + self.cellWidth * x + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * y + int(self.settings.cellWidth * 0.1) - 5

    def updatePieces(self):
        self.pieces.update()

    def typeOfMove(self, oldX, oldY, newX, newY, piece):
        if piece.piece != "king":
            if oldX == newX:
                return "vertical"
            elif oldY == newY:
                return "horizontal"
            elif (oldX == newX - 2 and oldY == newY - 1) or (oldX == newX - 2 and oldY == newY + 1) or (oldX == newX + 2 and oldY == newY - 1) or (oldX == newX + 2 and oldY == newY + 1) or (oldX == newX - 1 and oldY == newY - 2) or (oldX == newX + 1 and oldY == newY - 2) or (oldX == newX - 1 and oldY == newY + 2) or (oldX == newX + 1 and oldY == newY + 2): # NOT THE MOST BEAUTIFUL, BUT WORKS
                return "L"
            elif abs(oldX - newX) == abs(oldY - newY):
                return "diagonal"
            
            else:
                return False # INVALID MOVE
        else:
            if abs(oldX - newX) <= 1 and abs(oldY - newY) <= 1:
                return "kingMove"
            else:
                return False

    def moveBack(self, piece):
        piece.rect.x,  piece.rect.y = self.oldX, self.oldY


    def isSteppedOverAnotherPiece(self, oldX, oldY, newX, newY, typeOfMove):
        if typeOfMove == "horizontal":
            if oldX < newX:
                for piece in self.pieces:
                    pieceX, pieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                    if pieceY == oldY:
                        if oldX < pieceX and newX > pieceX:
                            return True
                return False
            elif oldX > newX:
                for piece in self.pieces:
                    pieceX, pieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                    if pieceY == oldY:
                        if oldX > pieceX and newX < pieceX:
                            return True
                return False

        elif typeOfMove == "vertical":
            if oldY < newY:
                for piece in self.pieces:
                    pieceX, pieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                    if pieceX == oldX:
                        if oldY < pieceY and newY > pieceY:
                            return True
                return False
            elif oldY > newY:
                for piece in self.pieces:
                    pieceX, pieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                    if pieceX == oldX:
                        if oldY > pieceY and newY < pieceY:
                            return True
                return False

        elif typeOfMove == "diagonal":
            for piece in self.pieces:
                pieceX, pieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                if abs(oldX - pieceX) == abs(oldY - pieceY):
                    if oldX < newX and oldY < newY:
                        if oldX < pieceX < newX and oldY < pieceY < newY:
                            return True

                    elif oldX > newX and oldY > newY:
                        if oldX > pieceX > newX and oldY > pieceY > newY:
                            return True

                    elif oldX < newX and oldY > newY:
                        if oldX < pieceX < newX and oldY > pieceY > newY:
                            return True

                    elif oldX > newX and oldY < newY:
                        if oldX > pieceX > newX and oldY < pieceY < newY:
                            return True
            return False


    def events(self):
        #EVENTS
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False
            
            elif event.type == p.KEYDOWN:
                if event.key == p.K_q:
                    self.running = False

            elif event.type == p.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for piece in self.pieces:
                        if piece.check_click(event.pos):
                            self.dragging = True
                            self.clickedPiece = piece
                            self.pieces.move_to_front(piece)
                            self.oldX, self.oldY = self.clickedPiece.rect.x, self.clickedPiece.rect.y
                            self.clickedPiece.rect.x = event.pos[0] - self.cellWidth / 2
                            self.clickedPiece.rect.y = event.pos[1] - self.cellWidth / 2

            elif event.type == p.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.clickedPiece and self.dragging:
                        posX, posY = event.pos
                        if self.clickedPiece.isOutofTable(posX, posY) or self.clickedPiece.color != self.turn:
                            self.moveBack(self.clickedPiece)
                        else:
                            self.movePieceToNearestSquare(posX, posY)
                            if not self.isValidMove(posX, posY):
                                self.moveBack(self.clickedPiece)
                            else:
                                typeOfMove = self.typeOfMove(self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[0],self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[1],self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1], self.clickedPiece)
                                if not typeOfMove:
                                    self.moveBack(self.clickedPiece)
                                else:
                                    if self.validateMove(self.clickedPiece, typeOfMove, self.clickedPiece.checkHit(self.clickedPiece, self.pieces, True)):
                                        if not self.isSteppedOverAnotherPiece(self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[0],self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[1],self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1], typeOfMove):
                                            self.clickedPiece.checkHit(self.clickedPiece, self.pieces)
                                            if self.turn == "w":
                                                self.turn = "b"
                                            else:
                                                self.turn = "w"
                                        else:
                                            self.moveBack(self.clickedPiece)
                                    else:
                                        self.moveBack(self.clickedPiece)
                                        
                self.dragging = False

            elif event.type == p.MOUSEMOTION:
                if self.dragging:
                    x, y = event.pos
                    self.clickedPiece.rect.x = x - self.cellWidth / 2
                    self.clickedPiece.rect.y = y - self.cellWidth / 2
        
    def run(self):

        # SCREEN
        self.screen.fill((255, 255, 255))

        # TABLE
        self.drawTable()
        self.drawBorder()

        


        # PIECES
        self.pieces.draw(self.screen)
        self.updatePieces()


        #FPS, FLIP
        self.clock.tick(self.fps)
        p.display.flip()


   
p.quit()