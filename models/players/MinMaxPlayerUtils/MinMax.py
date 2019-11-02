from models.players.MinMaxPlayerUtils.Board_evaluator import evaluateBoard
from models.board import Board
import models.players.MinMaxPlayerUtils.heuristics as heuristics
import copy
import time

INF = 0x3f3f3f3f
INITIAL_SEARCH_DEPTH = 2
INITIAL_TIME = None
MAX_TIME = 3

final_board_state_heuristic = [heuristics.piecesDiference]
game_heuristics = [heuristics.cornersHeuristic,
                   heuristics.stability, heuristics.mobility]
game_weights = [1000, 100, 10]


def calculatePlay(Board, mypieces):
    INITIAL_TIME = time.time()
    global INITIAL_TIME
    move = iterativeDepeningMinMax(INITIAL_SEARCH_DEPTH, Board, mypieces)
    print "search time: ", time.time() - INITIAL_TIME
    return move


def iterativeDepeningMinMax(initial_depth, Board, mypieces):
    best_move = None
    max_depth = 0
    for depth in range(INITIAL_SEARCH_DEPTH, 15):
        move = minMax(Board, 0, depth,
                      True, mypieces, -INF, INF)
        if move is not None:
            max_depth = depth
            best_move = move
    print "search depth: ", max_depth
    return best_move


def minMax(Board, current_depth, max_depth, IsMaxNode, myPieces, alpha, beta):

    whiteMoves = Board.valid_moves(Board.WHITE)
    blackMoves = Board.valid_moves(Board.BLACK)
    numberOfWhiteMoves = whiteMoves.__len__()
    numberOfBlackMoves = blackMoves.__len__()

    if(time.time()-INITIAL_TIME + 0.02 > MAX_TIME):
        return None

    # if end game
    if(numberOfWhiteMoves == 0 and numberOfBlackMoves == 0):
        pieces_diference = evaluateBoard(
            Board, myPieces, final_board_state_heuristic)
        # if we won
        if(pieces_diference > 0):
            return INF+pieces_diference
        # if we lose or draw
        if(pieces_diference < 0):
            return -INF+pieces_diference
        if(pieces_diference == 0):
            return -INF+pieces_diference

    if(current_depth == max_depth):
        return evaluateBoard(Board, myPieces, game_heuristics, game_weights)

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
        maximum = -INF*2

        for move in moves:
            new_board = copy.deepcopy(Board)
            new_board.play(move, myPieces)
            current_child_value = minMax(
                new_board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)
            if(current_child_value is None):
                return None

            if(maximum <= current_child_value):
                maximum = current_child_value
                best_move = move
            alpha = max(alpha, maximum)
            # if(alpha >= beta):
            #     break
        if(current_depth != 0):
            return maximum
        else:
            # print("best move evaluation: ", maximum,
            #   " move: ", (best_move.x, best_move.y))
            return best_move
    else:
        # in this case the other player pieces plays
        if(myPieces == Board.WHITE):
            theirPieces = Board.BLACK
            moves = blackMoves
        else:
            theirPieces = Board.WHITE
            moves = whiteMoves

        # if there are no plays pass the turn
        if(moves.__len__() == 0):
            return minMax(Board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)

        # calculate the best move
        minimum = INF*2

        for move in moves:
            new_board = copy.deepcopy(Board)
            new_board.play(move, theirPieces)

            current_child_value = minMax(
                new_board, current_depth+1, max_depth, not IsMaxNode, myPieces, alpha, beta)

            if(current_child_value is None):
                return None

            if(current_child_value <= minimum):
                minimum = current_child_value
                best_move = move
            beta = min(beta, minimum)
            # if(alpha >= beta):
            #     break
        if(current_depth != 0):
            return minimum
        else:
            return best_move


def main():
    print calculatePlay(Board(None), Board.BLACK)
