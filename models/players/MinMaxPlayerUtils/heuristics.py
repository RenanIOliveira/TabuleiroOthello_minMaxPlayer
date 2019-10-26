

def piecesDiference(board, myPieces):
    [white, black] = board.score()
    if(myPieces == board.WHITE):
        return white - black
    else:
        return black - white
