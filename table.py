import pygame as p
from settings import Settings
from pieces import Piece
from math import ceil

p.init()

class Table:

    def __init__(self):
        self.settings = Settings()

        #### PIECES
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
        p.font.init()
        self.infoFont = p.font.SysFont('Comic Sans MS', 30)
        self.turnFont = p.font.SysFont('Comic Sans MS', 100)
        self.checkmateFont = p.font.SysFont('Comic Sans MS', 120)
        self.flag = True
        self.bKingRow, self.bKingColumn = 4, 0
        self.wKingRow, self.wKingColumn = 4, 7
        self.colorBKing = False
        self.colorWKing = False
        self.checkmate = None
        self.chess = False
        self.numOfTurn = 1
        self.swapTurn = {
            "w" : "b",
            "b" : "w"
        }
        self.checkMateChecker = False
        
        # START GAME
        self.deployPawns()
        self.deployRooks()
        self.deployKnights()
        self.deployBishops()
        self.deployQueens()
        self.deployKings()

        self.whiteMoves = self.getWhiteMoves()
        self.blackMoves = self.getBlackMoves()
        self.possibleMoves = self.officialMoves()
        self.whiteMovesSet = set()
        self.blackMovesSet = set()
        self.castleRook = None

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
        elif piece == "king" and typeOfMove in ["kingMove", "castle"]:
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
        typeOfPiece = piece.piece
        if typeOfPiece == "king":
            if abs(oldX - newX) <= 1 and abs(oldY - newY) <= 1:
                return "kingMove"
            elif oldY == newY and abs(oldX - newX) == 2:
                return "castle"
            return False
        elif typeOfPiece == "knight":
            if (oldX == newX - 2 and oldY == newY - 1) or (oldX == newX - 2 and oldY == newY + 1) or (oldX == newX + 2 and oldY == newY - 1) or (oldX == newX + 2 and oldY == newY + 1) or (oldX == newX - 1 and oldY == newY - 2) or (oldX == newX + 1 and oldY == newY - 2) or (oldX == newX - 1 and oldY == newY + 2) or (oldX == newX + 1 and oldY == newY + 2): # NOT THE MOST BEAUTIFUL, BUT WORKS
                return "L"
        elif typeOfPiece == "pawn":
            if oldX == newX:
                if not self.checkPawnDirection(oldY, newY):
                    return False
                return "vertical"
            elif abs(oldX - newX) == abs(oldY - newY):
                if not self.checkPawnDirection(oldY, newY):
                    return False
                return "diagonal"
        else:
            if oldX == newX:
                return "vertical"
            elif oldY == newY:
                return "horizontal"
            elif abs(oldX - newX) == abs(oldY - newY):
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
            

    def moveBack(self, piece):
        piece.rect.x,  piece.rect.y = self.oldX, self.oldY


    def isSteppedOverAnotherPiece(self, oldX, oldY, newX, newY, typeOfMove, piece=None):
        if not piece:
            piece = self.clickedPiece
        if piece.piece in ["king", "knight"] or typeOfMove in ["kingMove", "L"]:
            return False
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


    def getWhiteMoves(self):
        moves = []
        for piece in self.pieces:
            if piece.color == "w":
                tempList = []
                tempList.append(piece) # THE PIECE
                tempList.append([piece.getCurrentPos(piece.rect.x, piece.rect.y)[0], piece.getCurrentPos(piece.rect.x, piece.rect.y)[1]]) # CURR POS
                for move in self.getPossibleMoves(piece, True):
                    tempList.append([move[0], move[1]]) # POSSIBLEMOVES
                moves.append(tempList)
        return moves


    def getBlackMoves(self):
        blackMoves = []
        for piece in self.pieces:
            if piece.color == "b":
                tempList = []
                tempList.append(piece)
                tempList.append([piece.getCurrentPos(piece.rect.x, piece.rect.y)[0], piece.getCurrentPos(piece.rect.x, piece.rect.y)[1]]) # CURR POS
                for move in self.getPossibleMoves(piece, True):
                    tempList.append([move[0], move[1]])
                blackMoves.append(tempList)
        return blackMoves


    def isCheckMate(self, color):
        if color == "b":
            self.whiteMoves = self.getWhiteMoves() # REGENERATING THE MOVES
        else:
            self.blackMoves = self.getBlackMoves()
        self.checkMateChecker = True
        for piece in self.pieces:
            if piece.color != color:
                if self.officialMoves(piece, self.swapTurn[color]):
                    print(self.officialMoves(piece, self.swapTurn[color]))
                    self.checkMateChecker = False
                    return False
                
        winner = {
            "w" : "White",
            "b" : "Black"
        }
        self.checkmate = winner[color]


    def officialMoves(self, piece=None, color=None):
        if not color:
            color = self.turn
        officialMoves = []
        if color == "w":
            moves = self.whiteMoves
        else:
            moves = self.blackMoves
        if piece:
            for pieceInfo in moves:
                if pieceInfo[0] == piece:
                    oldX, oldY = pieceInfo[1][0], pieceInfo[1][1]
                    length = len(pieceInfo)
                    if length > 2:
                        for i in range(2, length):
                            self.chess = False
                            piece.rect.x, piece.rect.y = self.addon + self.cellWidth * pieceInfo[i][0] + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * pieceInfo[i][1] + int(self.settings.cellWidth * 0.1) - 5
                            self.pieces.move_to_front(piece) # I searched for a lot of hours till I found that this was missing from here :)
                            collision = self.checkCollision(piece)
                            if collision and collision.piece != "king":
                                collision.kill()
                            if piece.piece == "king":
                                self.isChess(color, piece.getCurrentPos(piece.rect.x, piece.rect.y)[0], piece.getCurrentPos(piece.rect.x, piece.rect.y)[1])
                            else:
                                self.isChess(color)
                            if not self.checkMateChecker:
                                if not self.chess or self.chess != color:
                                    officialMoves.append([pieceInfo[i][0], pieceInfo[i][1]])
                            else:
                                if not self.chess:
                                    officialMoves.append([pieceInfo[i][0], pieceInfo[i][1]])
                            piece.rect.x, piece.rect.y = self.addon + self.cellWidth * oldX + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * oldY + int(self.settings.cellWidth * 0.1) - 5
                            if collision:
                                self.pieces.add(collision)
                        break
        else:
            for i in range(len(moves)):
                piece = moves[i][0]
                oldX, oldY = moves[i][1][0], moves[i][1][1]
                length = len(moves[i])
                if length > 2:
                    for j in range(2, length):
                        piece.rect.x, piece.rect.y = self.addon + self.cellWidth * moves[i][j][0] + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * moves[i][j][1] + int(self.settings.cellWidth * 0.1) - 5
                        collision = self.checkCollision(piece)
                        if collision and collision.piece != "king":
                            collision.kill()
                        self.isChess(color)
                        if not self.chess or self.chess != color:
                            officialMoves.append([moves[i][0], moves[i][1]])
                        piece.rect.x, piece.rect.y = self.addon + self.cellWidth * oldX + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * oldY + int(self.settings.cellWidth * 0.1) - 5
                        if collision:
                            self.pieces.add(collision)
        if officialMoves == []:
            return False
            
        return officialMoves


    def getKingPos(self, color):
        for piece in self.pieces:
            if piece.color == color:
                if piece.piece == "king":
                    return piece.getCurrentPos(piece.rect.x, piece.rect.y)[0],piece.getCurrentPos(piece.rect.x, piece.rect.y)[1]


    def isChess(self, color, kingX=None, kingY=None):
        if color == "w":
            moves = self.getBlackMoves()
            if not kingX:
                kingRow, kingColumn = self.wKingRow, self.wKingColumn
            else:
                kingRow, kingColumn = kingX, kingY
        else:
            moves = self.getWhiteMoves()
            if not kingX:
                kingRow, kingColumn = self.bKingRow, self.bKingColumn
            else:
                kingRow, kingColumn = kingX, kingY
            
        for piecePos in moves:
            length = len(piecePos)
            if length > 2:
                for i in range(2, length):
                    if piecePos[i] == [kingRow, kingColumn]:
                        if color == "w":
                            self.colorWKing = True
                        else:
                            self.colorBKing = True
                        self.chess = color
                        break


    def colorPossibleSquares(self, piece, chess=False, kX=None, kY=None):
        if chess:
            p.draw.rect(self.screen, (253, 73, 77), self.squares[kX + kY * 8])
        
        if piece:
            if piece.color == "w":
                moves = self.whiteMoves
            else:
                moves = self.blackMoves
                
        
            if self.turn == piece.color:
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
        if typeOfPiece == "king":
            if not currPiece.moved:
                rooks = []
                for piece in self.pieces:
                    if piece.piece == "rook" and not piece.moved and piece.color == color:
                        rooks.append(piece)
                if len(rooks):
                    for rook in rooks:
                        between = False
                        castleRookX, castleRookY = rook.getCurrentPos(rook.rect.x, rook.rect.y)
                        for piece in self.pieces:
                            if piece != rook and piece != currPiece:
                                pieceX, pieceY = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                                if currPieceY == pieceY:
                                    if castleRookX > currPieceX:
                                        if currPieceX < pieceX < castleRookX:
                                            between = True
                                            break
                                    else:
                                        if currPieceX > pieceX > castleRookX:
                                            between = True
                                            break
                        if not between:
                            if castleRookX > currPieceX:
                                possibleMoves.append([currPieceX + 2, currPieceY])
                            else:
                                possibleMoves.append([currPieceX - 2, currPieceY])
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
                if not currPiece.moved and currPieceY == 6:
                    possibleMoves.append([currPieceX, currPieceY-2])
                possibleMoves.append([currPieceX, currPieceY-1])
                possibleMoves.append([currPieceX-1, currPieceY-1])
                possibleMoves.append([currPieceX+1, currPieceY-1])
            else:
                if not currPiece.moved and currPieceY == 1:
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
                            if not self.isSteppedOverAnotherPiece(currPieceX, currPieceY, x, y, move, currPiece):
                                    possibleMoves.append([x, y])
                possibleMoves = self.checkSameColor(color, possibleMoves)
        return possibleMoves


    def checkSameColor(self, color, possibleMoves):
        for otherPiece in self.pieces:
            if otherPiece.color == color:
                if otherPiece != self.clickedPiece:
                    posX, posY = otherPiece.getCurrentPos(otherPiece.rect.x, otherPiece.rect.y)
                    for move in possibleMoves:
                        if move == [posX, posY]:
                            possibleMoves.remove(move)
        return possibleMoves
    
    
    def handleCastling(self, color, oldX, newX, kingY):
        for piece in self.pieces:
            if piece.piece == "rook" and piece.color == color:
                x, y = piece.getCurrentPos(piece.rect.x, piece.rect.y)
                if oldX < newX:
                    if [x, y] == [7, kingY]:
                        piece.rect.x, piece.rect.y = self.addon + self.cellWidth * 5 + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * kingY + int(self.settings.cellWidth * 0.1) - 5
                        return True
                else:
                    if [x, y] == [0, kingY]:
                        piece.rect.x, piece.rect.y = self.addon + self.cellWidth * 3 + int(self.settings.cellWidth * 0.1),self.addon / self.heightOptimizer + self.cellWidth * kingY + int(self.settings.cellWidth * 0.1) - 5
                        return True
        return False
                        


    def checkCollision(self, piece=None):
        if not piece:
            piece = self.clickedPiece
        return piece.checkHit(piece, self.pieces)


    def changeTurn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
            self.numOfTurn += 1
        if not self.clickedPiece.moved:
            self.clickedPiece.moved = True
        
        # GENERATE AVALIABLE MOVES
        self.whiteMoves = self.getWhiteMoves()
        self.blackMoves = self.getBlackMoves()
        self.chess = False


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
                            self.wKingRow, self.wKingColumn, self.bKingRow, self.bKingColumn = self.getKingPos("w")[0], self.getKingPos("w")[1], self.getKingPos("b")[0], self.getKingPos("b")[1]
                            self.oldX, self.oldY = piece.rect.x, piece.rect.y
                            self.possibleMoves = self.officialMoves(piece, piece.color)
                            self.flag = False
                            
                        self.dragging = True
                        self.pieces.move_to_front(piece)
                        
                        piece.rect.x = event.pos[0] - self.cellWidth / 2
                        piece.rect.y = event.pos[1] - self.cellWidth / 2
                        break

            elif event.type == p.MOUSEBUTTONUP:
                if self.clickedPiece and self.dragging:
                    posX, posY = event.pos
                    if not self.clickedPiece.isOutofTable(posX, posY) and self.clickedPiece.color == self.turn:
                        oldPos = self.clickedPiece.getCurrentPos(self.oldX, self.oldY)
                        newPos = self.clickedPiece.getCurrentPos(posX, posY)
                        if newPos != self.clickedPiece.getCurrentPos(self.oldX, self.oldY):
                            self.movePieceToNearestSquare(posX, posY)
                            if self.possibleMoves:
                                if [newPos[0], newPos[1]] in self.possibleMoves:
                                    typeOfMove = self.typeOfMove(oldPos[0],oldPos[1],newPos[0], newPos[1], self.clickedPiece)
                                    if typeOfMove:
                                        if self.validateMove(self.clickedPiece, typeOfMove, self.clickedPiece.checkHit(self.clickedPiece, self.pieces, True)):
                                            if typeOfMove == "castle":
                                                self.handleCastling(self.clickedPiece.color, oldPos[0], newPos[0], oldPos[1])
                                            if not self.isSteppedOverAnotherPiece(oldPos[0],oldPos[1],newPos[0], newPos[1], typeOfMove):
                                                collision = self.checkCollision()
                                                if collision:
                                                    collision.kill()
                                                self.isChess(self.swapTurn[self.turn])
                                                if not self.chess:
                                                    self.colorWKing, self.colorBKing = False, False
                                                else:
                                                    self.isCheckMate(self.turn)
                                                self.changeTurn() # GET OPPONENT MOVES ASWELL
                                                self.dragging = False
                                                self.clickedPiece = None
                                                self.possibleMoves = None
                                                self.flag = True
                                                self.wKingRow, self.wKingColumn, self.bKingRow, self.bKingColumn = self.getKingPos("w")[0], self.getKingPos("w")[1], self.getKingPos("b")[0], self.getKingPos("b")[1]
                                                break
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

        if self.colorWKing and not self.colorBKing and self.turn == "w":
            self.colorPossibleSquares(self.clickedPiece, True, self.wKingRow, self.wKingColumn)
        elif self.colorBKing and not self.colorWKing and self.turn == "b":
            self.colorPossibleSquares(self.clickedPiece, True, self.bKingRow, self.bKingColumn)
        
        if self.clickedPiece:
            self.colorPossibleSquares(self.clickedPiece)
            ####
            # ONLY FOR INFO, WILL HAVE TO BE DELETED
            if self.possibleMoves:
                for x, move in enumerate(self.possibleMoves):
                    self.screen.blit(self.infoFont.render(str(self.translatePosition(move[0], move[1])), False, (0, 0, 0)), (self.screen.get_width() / 2, 100 + x * 30))
            if self.typeOfMove(self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[0],self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[1],self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1], self.clickedPiece):
                self.screen.blit(self.infoFont.render(self.typeOfMove(self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[0],self.clickedPiece.getCurrentPos(self.oldX, self.oldY)[1],self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[0], self.clickedPiece.getCurrentPos(self.clickedPiece.rect.x, self.clickedPiece.rect.y)[1], self.clickedPiece), False, (0,0,0)), (self.screen.get_width() / 1.2, 540))

        # PIECES
        self.pieces.draw(self.screen)
        self.updatePieces()

        # CHECKMATE
        if self.checkmate:
            self.screen.blit(self.checkmateFont.render(f"Game Over! {self.checkmate} Won!", False, (255, 0, 0),(0, 0, 0)), (200, self.screen.get_height() / 6))
            ###### RESTART GAME, QUIT....

        #FPS, FLIP
        self.clock.tick(self.fps)
        p.display.flip()


   
p.quit()