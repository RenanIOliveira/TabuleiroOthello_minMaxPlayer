

def piecesDiference(board, myPieces):
    [white, black] = board.score()
    if(myPieces == board.WHITE):
        return white - black
    else:
        return black - white

def mobility(board, myPieces):
    numberOfWhiteMoves = board.valid_moves(board.WHITE).__len__()
    numberOfBlackMoves = board.valid_moves(board.BLACK).__len__()

    if (numberOfWhiteMoves + numberOfBlackMoves != 0):
        if(myPieces == board.WHITE):
            return (numberOfWhiteMoves - numberOfBlackMoves)/(numberOfWhiteMoves + numberOfBlackMoves)
        else:
            return (numberOfBlackMoves - numberOfWhiteMoves)/(numberOfWhiteMoves + numberOfBlackMoves)
    else:
        return 0