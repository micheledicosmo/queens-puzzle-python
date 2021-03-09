class Piece:
    def __init__(self):
        self.board = None
        self.i = None
        self.j = None

    def isOnBoard(self):
        return self.board != None

    def placeOn(self, board, i, j):
        if (not self.isOnBoard()
            and (0 <= i)
            and (i < board.size())
            and (0 <= j)
            and (j < board.size()) ):
                self.board = board;
                self.i = i;
                self.j = j;
                board.add( self );

    def removeFromBoard(self):
        if (self.isOnBoard()):
            self.board.remove(self)
            self.board = None

    def attacks(self, piece):
        raise Exception("An abstract method has been invoked")

    def isMindfulOf(self, piece):
        return ((piece!=None)
                and self.isOnBoard()
                and piece.isOnBoard()
                and self.board == piece.board
                and self != piece)
    
    def rowIndex(self):
        if (self.isOnBoard()):
            return self.i
        else:
            return self.UNKNOWN
    
    def colIndex(self):
        if (self.isOnBoard()):
            return self.j;
        else:
            return self.UNKNOWN

    UNKNOWN = -1