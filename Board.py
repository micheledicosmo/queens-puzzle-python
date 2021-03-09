class Board:
    def __init__(self, size):
        self.n = size
        self.pieces = set()

    def size(self):
        return self.n

    def admissiblePlacementFor(self, piece):
        for other in self.pieces:
            if ((other != piece)
                and other.attacks(piece)
                or piece.attacks(other)):
                    return False
        return True

    def add(self, piece):
        self.pieces.add(piece)

    def remove(self, piece):
        self.pieces.remove(piece)