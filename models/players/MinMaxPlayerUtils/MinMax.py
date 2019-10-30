from models.players.MinMaxPlayerUtils.Board_evaluator import evaluateBoard
from models.board import Board
import models.players.MinMaxPlayerUtils.heuristics as heuristics
import copy
import datetime

INF = 0x3f3f3f3f
MAXIMUM_SEARCH_DEPTH = 3
MIN_TIME = datetime.datetime.now()


def calculatePlay(Board, mypieces):
    global MIN_TIME
    MIN_TIME = datetime.datetime.now()
    move = minMax(Board, 0, MAXIMUM_SEARCH_DEPTH,
                  True, mypieces, -INF, INF)
    print datetime.datetime.now() - MIN_TIME
    return move


def minMax(Board, current_depth, max_depth, IsMaxNode, myPieces, alpha, beta):
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
        if(evaluateBoard(Board, myPieces, [heuristics.piecesDiference]) < 0):
            return -INF
        if(evaluateBoard(Board, myPieces, [heuristics.piecesDiference]) == 0):
            return -INF+1

    if(current_depth == max_depth):
        # current_time = datetime.datetime.now()
        # step_time_difference = current_time - initial_time
        # time_difference = current_time - MIN_TIME
        # if ((time_difference + step_time_difference).total_seconds() >= 3):
        return evaluateBoard(Board, myPieces, [heuristics.piecesDiference])
        # else:
        #     return minMax(Board, current_depth, max_depth+1, IsMaxNode, myPieces, alpha, beta, datetime.datetime.now())

    if(IsMaxNode):
        # if is maxnode myPieces plays
        if(myPieces == Board.WHITE):
            moves = whiteMoves
        else:
            moves = blackMoves

        # if there are no plays pass the turn
        if(moves.__len__() == 0):
            return minMax(Board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)

        # calculate the best move
        maximum = -INF

        for move in moves:
            new_board = copy.deepcopy(Board)
            new_board.play(move, Board.WHITE)
            current_child_value = minMax(
                new_board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)
            if(maximum <= current_child_value):
                maximum = current_child_value
                best_move = move
            alpha = max(alpha, maximum)
            if(alpha >= beta):
                break
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
            return minMax(Board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)

        # calculate the best move
        minimum = INF
        for move in moves:
            new_board = copy.deepcopy(Board)
            new_board.play(move, Board.BLACK)
            current_child_value = minMax(
                new_board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)
            if(current_child_value <= minimum):
                minimum = current_child_value
                best_move = move
            beta = min(beta, minimum)
            if(alpha >= beta):
                break
        if(current_depth != 0):
            return minimum
        else:
            return best_move


def main():
    print calculatePlay(Board(None), Board.BLACK)
