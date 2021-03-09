from Piece import Piece

class Queen(Piece):
    def __init__(self):
        Piece.__init__(self)

    def attacks(self, piece):
        i = self.rowIndex()
        j = self.colIndex()

        u = piece.rowIndex()
        v = piece.colIndex()

        return (
            self.isMindfulOf(piece)
            and ((i == u)
                or (j == v) 
                or (i-j == u-v)
                or (i+j == u+v)) )