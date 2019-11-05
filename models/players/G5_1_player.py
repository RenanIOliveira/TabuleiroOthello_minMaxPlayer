import models.players.MinMaxPlayerUtilsG5.MinMax as MinMax


class G5Player1:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return MinMax.calculatePlay(board, self.color)
