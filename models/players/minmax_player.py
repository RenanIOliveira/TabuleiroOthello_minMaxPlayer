import models.players.MinMaxPlayerUtils.MinMax as MinMax


class MinMaxPlayer:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return MinMax.calculatePlay(board, self.color)
