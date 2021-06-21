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
        self.squares = []
        self.pieceSquare = self.settings.pieceSquare
        self.moveableSquares = self.settings.moveableSquares
        self.possibleMoves = None
        p.font.init()
        self.infoFont = p.font.SysFont('Comic Sans MS', 30)
        self.turnFont = p.font.SysFont('Comic Sans MS', 100)
        self.flag = True
        self.bKingRow, self.bKingColumn = None, None
        self.wKingRow, self.wKingColumn = None, None
        self.colorBKing = False
        self.colorWKing = False

        # START GAME
        self.deployPawns()
        self.deployRooks()
        self.deployKnights()
        self.deployBishops()
        self.deployQueens()
        self.deployKings()



    def getTableRect(self, posX, posY):
        rect = p.Rect(posX, posY, self.cellWidth, self.cellWidth)
        self.squares.append(rect)
        return rect

        

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
        elif piece == "pawn" and ((typeOfMove == "vertical" and not hit) or (hit and typeOfMove == "diagonal")):
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
                if piece.piece == "pawn":
                    if not self.checkPawnDirection(oldY, newY):
                        return False
                return "vertical"
            elif oldY == newY:
                return "horizontal"
            elif (oldX == newX - 2 and oldY == newY - 1) or (oldX == newX - 2 and oldY == newY + 1) or (oldX == newX + 2 and oldY == newY - 1) or (oldX == newX + 2 and oldY == newY + 1) or (oldX == newX - 1 and oldY == newY - 2) or (oldX == newX + 1 and oldY == newY - 2) or (oldX == newX - 1 and oldY == newY + 2) or (oldX == newX + 1 and oldY == newY + 2): # NOT THE MOST BEAUTIFUL, BUT WORKS
                return "L"
            elif abs(oldX - newX) == abs(oldY - newY):
                if piece.piece == "pawn":
                    if not self.checkPawnDirection(oldY, newY):
                        return False
                if oldX > newX:
                    if oldY > newY:
                        if 8 - ((7 - oldX) + newX) == 8 - ((7 - oldY) + newY):
                            return "diagonal"
                    elif newY > oldY:
                        if 8 - ((7 - oldX) + newX) == 8 - ((7 - newY) + oldY):
                            return "diagonal"
                elif newX > oldX:
                    if oldY > newY:
                        if 8 - ((7 - newX) + oldX) == 8 - ((7 - oldY) + newY):
                            return "diagonal"
                    elif newY > oldY:
                        if 8 - ((7 - newX) + oldX) == 8 - ((7 - newY) + oldY):
                            return "diagonal"
            return False # INVALID MOVE
        else:
            if abs(oldX - newX) <= 1 and abs(oldY - newY) <= 1:
                return "kingMove"
            return False

    def moveBack(self, piece):
        piece.rect.x,  piece.rect.y = self.oldX, self.oldY


    def isSteppedOverAnotherPiece(self, oldX, oldY, newX, newY, typeOfMove):
        if self.clickedPiece.piece != "king":
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
            return True
        return False


    def getWhiteMoves(self):
        whiteMoves = set()
        for piece in self.pieces:
            if piece.color == "w":
                for move in self.getPossibleMoves(piece, True):
                    whiteMoves.add(tuple(self.translatePosition(move[0], move[1])))

        return whiteMoves


    def getBlackMoves(self):
        blackMoves = set()
        for piece in self.pieces:
            if piece.color == "b":
                for move in self.getPossibleMoves(piece, True):
                    blackMoves.add(tuple(self.translatePosition(move[0], move[1])))

        return blackMoves


    def isChess(self):
        for piece in self.pieces:
            if piece.piece == "king":
                if piece.color == "w":
                    self.wKingRow, self.wKingColumn = piece.getCurrentPos(piece.rect.x, piece.rect.y)[0],piece.getCurrentPos(piece.rect.x, piece.rect.y)[1]
                else:
                    self.bKingRow, self.bKingColumn = piece.getCurrentPos(piece.rect.x, piece.rect.y)[0],piece.getCurrentPos(piece.rect.x, piece.rect.y)[1]
        wKingRow, wKingColumn = self.translatePosition(self.wKingRow, self.wKingColumn)
        bKingRow, bKingColumn = self.translatePosition(self.bKingRow, self.bKingColumn)
        whiteMoves = self.getWhiteMoves()
        blackMoves = self.getBlackMoves()
        for pos in whiteMoves:
            if [pos[0], pos[1]] == [bKingRow, bKingColumn]:
                return 'b'
        for pos in blackMoves:
            if [pos[0], pos[1]] == [wKingRow, wKingColumn]:
                return 'w'

        return False


    def colorPossibleSquares(self, piece, chess=False, kX=None, kY=None):
        if chess:
            p.draw.rect(self.screen, (253, 73, 77), self.squares[kX + kY * 8])
        else:
            posX, posY = piece.getCurrentPos(self.oldX, self.oldY)
            p.draw.rect(self.screen, self.settings.pieceSquare, self.squares[posX + posY * 8])
            if self.possibleMoves:
                for val in self.possibleMoves:
                    p.draw.rect(self.screen, self.settings.moveableSquares, self.squares[val[0] + val[1] * 8])


    def checkPawnDirection(self, oldY, newY):
        if self.clickedPiece.color == "w":
            if oldY < newY:
                return False
        else:
            if oldY > newY:
                return False
        
        return True

    def translatePosition(self, posX, posY):
        return [self.settings.boardLetters[posX],self.settings.boardNums[7-posY]]


    def getPossibleMoves(self, piece, flag=False):
        currPiece = piece
        color = piece.color
        typeOfPiece = piece.piece
        possibleMoves = []
        if not flag:
            currPieceX, currPieceY = piece.getCurrentPos(self.oldX, self.oldY)
        else:
            currPieceX, currPieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
            if currPiece == "pawn":
                piece.moved = True
        if typeOfPiece == "king":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= currPieceX + i < 8 and 0 <= currPieceY + j < 8:
                        if i != 0 or j != 0:
                            possibleMoves.append([currPieceX + i, currPieceY + j])
            for otherPiece in self.pieces:
                currentPos = list(otherPiece.getCurrentPos(otherPiece.rect.x, otherPiece.rect.y))
                if currentPos in possibleMoves and otherPiece.color == color:
                    possibleMoves.remove(currentPos)
                elif currentPos in possibleMoves and otherPiece.color != color:
                    ### CHECK FOR CHESS
                    pass
        elif typeOfPiece == "pawn":
            canHitL = False
            canHitR = False
            if color == "w":
                if not currPiece.moved:
                    possibleMoves.append([currPieceX, currPieceY-2])
                possibleMoves.append([currPieceX, currPieceY-1])
                possibleMoves.append([currPieceX-1, currPieceY-1])
                possibleMoves.append([currPieceX+1, currPieceY-1])
            else:
                if not currPiece.moved:
                    possibleMoves.append([currPieceX, currPieceY+2])
                possibleMoves.append([currPieceX, currPieceY+1])
                possibleMoves.append([currPieceX+1, currPieceY+1])
                possibleMoves.append([currPieceX-1, currPieceY+1])
            for otherPiece in self.pieces:
                currentPos = list(otherPiece.getCurrentPos(otherPiece.rect.x, otherPiece.rect.y))
                if currentPos in possibleMoves and currentPos[0] == currPieceX:
                    possibleMoves.remove(currentPos)
                if currentPos[0] > currPieceX and currentPos in possibleMoves and otherPiece.color != color:
                    canHitR = True
                if currentPos[0] < currPieceX and currentPos in possibleMoves and otherPiece.color != color:
                    canHitL = True
            if color == "w":
                Y = -1
            else:
                Y = 1
            if not canHitR:
                possibleMoves.remove([currPieceX+1, currPieceY+Y])
                
            if not canHitL:
                possibleMoves.remove([currPieceX-1, currPieceY+Y])
        elif typeOfPiece == "knight":
            # NOT THE MOST BEAUTIFUL, BUT WORKS
            if 0 <= currPieceX - 2 <= 7 and 0 <= currPieceY - 1 <= 7:
                possibleMoves.append([currPieceX - 2, currPieceY - 1])
            if 0 <= currPieceX - 2 <= 7 and 0 <= currPieceY + 1 <= 7:
                possibleMoves.append([currPieceX - 2, currPieceY + 1])
            if 0 <= currPieceX + 2 <= 7 and 0 <= currPieceY - 1 <= 7:
                possibleMoves.append([currPieceX + 2, currPieceY - 1])
            if 0 <= currPieceX + 2 <= 7 and 0 <= currPieceY + 1 <= 7:
                possibleMoves.append([currPieceX + 2, currPieceY + 1])
            if 0 <= currPieceX - 1 <= 7 and 0 <= currPieceY - 2 <= 7:
                possibleMoves.append([currPieceX - 1, currPieceY - 2])
            if 0 <= currPieceX + 1 <= 7 and 0 <= currPieceY - 2 <= 7:
                possibleMoves.append([currPieceX + 1, currPieceY - 2])
            if 0 <= currPieceX - 1 <= 7 and 0 <= currPieceY + 2 <= 7:
                possibleMoves.append([currPieceX - 1, currPieceY + 2])
            if 0 <= currPieceX + 1 <= 7 and 0 <= currPieceY + 2 <= 7:
                possibleMoves.append([currPieceX + 1, currPieceY + 2])

            possibleMoves = self.checkSameColor(color, possibleMoves)

        elif typeOfPiece in ["rook", "queen", "bishop"]:
            if typeOfPiece in ["rook", "queen"]:
                xRight, xLeft, yUp, yDown = None, None, None, None
                for otherPiece in self.pieces:
                    if otherPiece != currPiece:
                        otherPieceX, otherPieceY = otherPiece.getCurrentPos(otherPiece.rect.x, otherPiece.rect.y)
                        if otherPieceY == currPieceY:
                            if currPieceX > otherPieceX:
                                if not xLeft or (currPieceX - otherPieceX < xLeft):
                                    xLeft = currPieceX - otherPieceX
                            else:
                                if not xRight or (otherPieceX - currPieceX < xRight):
                                    xRight = otherPieceX - currPieceX
                        elif otherPieceX == currPieceX:
                            if currPieceY > otherPieceY:
                                if not yUp or (currPieceY - otherPieceY < yUp):
                                    yUp = currPieceY - otherPieceY
                            else:
                                if not yDown or (otherPieceY - currPieceY < yDown):
                                    yDown = otherPieceY - currPieceY
                if not xLeft:
                    xLeft = currPieceX + 1
                else:
                    xLeft += 1
                if not xRight:
                    xRight = 7 - currPieceX + 1
                else:
                    xRight += 1
                if not yUp:
                    yUp = currPieceY + 1
                else:
                    yUp += 1
                if not yDown:
                    yDown = 7 - currPieceY + 1
                else:
                    yDown += 1
                for xLeftMovement in range(1, xLeft):
                    possibleMoves.append([currPieceX-xLeftMovement,currPieceY])            
                for xRightMovement in range(1, xRight):
                    possibleMoves.append([currPieceX+xRightMovement,currPieceY])
                for yUpMovement in range(1, yUp):
                    possibleMoves.append([currPieceX,currPieceY-yUpMovement])
                for yDownMovement in range(1, yDown):
                    possibleMoves.append([currPieceX,currPieceY+yDownMovement])
                if typeOfPiece == "rook":
                    possibleMoves = self.checkSameColor(color, possibleMoves)
                    return possibleMoves
                    
            if typeOfPiece in ["bishop", "queen"]:
                for y in range(8):
                    for x in range(8):
                        move = self.typeOfMove(currPieceX, currPieceY, x, y, currPiece)
                        if move == "diagonal":
                            if not self.isSteppedOverAnotherPiece(currPieceX, currPieceY, x, y, move):
                                    possibleMoves.append([x, y])
                possibleMoves = self.checkSameColor(color, possibleMoves)

        return possibleMoves

    def checkSameColor(self, color, possibleMoves):
        for otherPiece in self.pieces:
            if otherPiece.color == color:
                posX, posY = otherPiece.getCurrentPos(otherPiece.rect.x, otherPiece.rect.y)
                for move in possibleMoves:
                    if move == [posX, posY]:
                        possibleMoves.remove(move)
        return possibleMoves

    def changeTurn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
        if not self.clickedPiece.moved:
            self.clickedPiece.moved = True

    def events(self):
        #EVENTS
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False
            
            elif event.type == p.KEYDOWN:
                if event.key == p.K_q:
                    self.running = False

            elif event.type == p.MOUSEBUTTONDOWN:
                for piece in self.pieces:
                    if piece.check_click(event.pos):
                        self.clickedPiece = piece
                        if self.flag:
                            self.oldX, self.oldY = self.clickedPiece.rect.x, self.clickedPiece.rect.y
                            self.possibleMoves = self.getPossibleMoves(self.clickedPiece)
                            self.flag = False
                        self.dragging = True
                        self.pieces.move_to_front(piece)
                        
                        self.clickedPiece.rect.x = event.pos[0] - self.cellWidth / 2
                        self.clickedPiece.rect.y = event.pos[1] - self.cellWidth / 2

            elif event.type == p.MOUSEBUTTONUP:
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
                                    if [self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1]] in self.possibleMoves:
                                        collidedPiece = self.clickedPiece.checkHit(self.clickedPiece, self.pieces)
                                        if collidedPiece:
                                            collidedPiece.kill()
                                        isChess = self.isChess()
                                        if not isChess:
                                            self.colorBKing, self.colorWKing = False, False
                                            self.changeTurn()
                                        else:
                                            if isChess == "w" and self.turn == "b":
                                                self.colorWKing = True
                                                self.changeTurn()
                                            elif isChess == "b" and self.turn == "w":
                                                self.colorBKing = True
                                                self.changeTurn()
                                            else:
                                                if collidedPiece:
                                                    self.pieces.add(collidedPiece)
                                                self.moveBack(self.clickedPiece)    
                                    else:
                                        self.moveBack(self.clickedPiece)
                                else:
                                    self.moveBack(self.clickedPiece)
                                    
                self.dragging = False
                self.clickedPiece = None
                self.possibleMoves = None
                self.flag = True

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


        # TURN
        self.screen.blit(self.turnFont.render(self.turn, False, (0, 0, 0)), (self.screen.get_width() / 1.2, self.screen.get_height() / 2))

        if self.colorWKing:
            self.colorPossibleSquares(self.clickedPiece, True, self.wKingRow, self.wKingColumn)
        elif self.colorBKing:
            self.colorPossibleSquares(self.clickedPiece, True, self.bKingRow, self.bKingColumn)
        
        if self.clickedPiece:
            self.colorPossibleSquares(self.clickedPiece)
            ####
            # ONLY FOR INFO, WILL HAVE TO BE DELETED
            for x, move in enumerate(self.possibleMoves):
                self.screen.blit(self.infoFont.render(str(self.translatePosition(move[0], move[1])), False, (0, 0, 0)), (self.screen.get_width() / 2, 100 + x * 30))
            if self.typeOfMove(self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[0],self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[1],self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1], self.clickedPiece):
                self.screen.blit(self.infoFont.render(self.typeOfMove(self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[0],self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[1],self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1], self.clickedPiece), False, (0,0,0)), (self.screen.get_width() / 1.2, 540))

        # PIECES
        self.pieces.draw(self.screen)
        self.updatePieces()


        #FPS, FLIP
        self.clock.tick(self.fps)
        p.display.flip()


   
p.quit()