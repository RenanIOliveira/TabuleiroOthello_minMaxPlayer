from models.players.MinMaxPlayerUtils.Board_evaluator import evaluateBoard
from models.board import Board
import models.players.MinMaxPlayerUtils.heuristics as heuristics
import copy

INF = 0x3f3f3f3f
MAXIMUM_SEARCH_DEPTH = 3


def calculatePlay(Board, mypieces):
    move = minMax(Board, 0, MAXIMUM_SEARCH_DEPTH, True, mypieces)
    return move


def minMax(Board, current_depth, max_depth, IsMaxNode, myPieces):
    whiteMoves = Board.valid_moves(Board.WHITE)
    blackMoves = Board.valid_moves(Board.BLACK)
    numberOfWhiteMoves = whiteMoves.__len__()
    numberOfBlackMoves = blackMoves.__len__()

    # if end game
    if(numberOfWhiteMoves == 0 and numberOfBlackMoves == 0):
        # if we won
        if(evaluateBoard(Board, myPieces, [heuristics.piecesDiference]) > 0):
            return INF
        # if we lose or draw
        if(evaluateBoard(Board, myPieces, [heuristics.piecesDiference]) <= 0):
            return -INF

    if(current_depth == max_depth):
        return evaluateBoard(Board, myPieces, [heuristics.piecesDiference])

    if(IsMaxNode):
        # if is maxnode myPieces plays
        if(myPieces == Board.WHITE):
            moves = whiteMoves
        else:
            moves = blackMoves

        # if there are no plays pass the turn
        if(moves.__len__() == 0):
            return minMax(Board, current_depth+1, max_depth, not IsMaxNode, myPieces)

        # calculate the best move
        maximum = -INF

        for move in moves:
            new_board = copy.deepcopy(Board)
            new_board.play(move, Board.WHITE)
            current_child_value = minMax(
                new_board, current_depth+1, max_depth, not IsMaxNode, myPieces)
            if(maximum <= current_child_value):
                maximum = current_child_value
                best_move = move
        if(current_depth != 0):
            return maximum
        else:
            return best_move
    else:
        # in this case the other player pieces plays
        if(myPieces == Board.WHITE):
            moves = blackMoves
        else:
            moves = whiteMoves

        # if there are no plays pass the turn
        if(moves.__len__() == 0):
            return minMax(Board, current_depth+1, max_depth, not IsMaxNode, myPieces)

        # calculate the best move
        min = INF
        for move in moves:
            new_board = copy.deepcopy(Board)
            new_board.play(move, Board.BLACK)
            current_child_value = minMax(
                new_board, current_depth+1, max_depth, not IsMaxNode, myPieces)
            if(current_child_value <= min):
                min = current_child_value
                best_move = move
        if(current_depth != 0):
            return min
        else:
            return best_move


def main():
    print calculatePlay(Board(None), Board.BLACK)
