import models.players.MinMaxPlayerUtils.MinMax2 as MinMax


class MinMaxPlayer2:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return MinMax.calculatePlay(board, self.color)
