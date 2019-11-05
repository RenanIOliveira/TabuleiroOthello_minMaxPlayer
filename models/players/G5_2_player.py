import models.players.MinMaxPlayerUtilsG5.MinMax2 as MinMax


class G5Player2:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return MinMax.calculatePlay(board, self.color)
