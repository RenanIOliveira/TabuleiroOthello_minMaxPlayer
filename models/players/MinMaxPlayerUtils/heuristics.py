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


corners = [[1, 1], [1, 8], [8, 1], [8, 8]]
UP, DOWN, LEFT, RIGHT = [-1, 0], [1, 0], [0, -1], [0, 1]


def stability(board, myPieces):
    global corners
    for corner in corners:
        calculateStables(board, myPieces, corner)


stable_pieces = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], ]


def calculateStables(board, myPieces, initial_position):
    global UP, DOWN, LEFT, RIGHT
    global stable_pieces

    if initial_position == corners[0]:
        horizontal_step = RIGHT
        vertical_step = DOWN
     if initial_position==corners[1]:
        horizontal_step = LEFT
        vertical_step = DOWN
    if initial_position==corners[2]:
        horizontal_step = RIGHT
        vertical_step = UP
    if initial_position==corners[2]:
        horizontal_step = LEFT
        vertical_step = UP

    n_stables,n_unstables,n_semi_stables = 0
    current_position = initial_position
    for i in range(1,9):

        for j in range(1,9):


    return number_of_stables
