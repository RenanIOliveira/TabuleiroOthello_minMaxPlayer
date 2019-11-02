import math


def piecesDiference(board, myPieces):
    [white, black] = board.score()
    if(myPieces == board.WHITE):
        return white - black
    else:
        return black - white


def cornersHeuristic(board, myPieces):
    corners = [[1, 1], [1, 8], [8, 1], [8, 8]]
    my_corners = 0
    their_corners = 0
    for corner in corners:
        if(board.get_square_color(corner[0], corner[1]) == myPieces):
            my_corners += 1
        if(board.get_square_color(corner[0], corner[1]) != myPieces and board.get_square_color(corner[0], corner[1]) != board.EMPTY):
            their_corners += 1

    return 100*(my_corners-their_corners)/(1+my_corners+their_corners)


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


stable_pieces = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], ]


def stability(board, myPieces):
    global corners
    if(myPieces == board.WHITE):
        theirPieces = board.BLACK
    else:
        theirPieces = board.WHITE

    countStables()

    for corner in corners:
        setStables(board, myPieces, corner)
    myStables = countStables()

    for corner in corners:
        setStables(board, theirPieces, corner)
    theirStables = countStables()

    return myStables - theirStables


def countStables():
    total = 0
    for i in range(1, 9):
        for j in range(1, 9):
            stable_piece = stable_pieces[i][j]
            if stable_piece == 1:
                total += 1
                stable_pieces[i][j] = 0
    return total


def setStables(board, myPieces, initial_position):
    global UP, DOWN, LEFT, RIGHT
    global stable_pieces

    if initial_position == corners[0]:
        horizontal_step = RIGHT
        vertical_step = DOWN
    if initial_position == corners[1]:
        horizontal_step = LEFT
        vertical_step = DOWN
    if initial_position == corners[2]:
        horizontal_step = RIGHT
        vertical_step = UP
    if initial_position == corners[3]:
        horizontal_step = LEFT
        vertical_step = UP

    current_position = [0, 0]
    current_position[0] = initial_position[0]
    current_position[1] = initial_position[1]

    vertical_limit = initial_position[0]+8*vertical_step[0]

    while(1):
        if board.get_square_color(current_position[0], current_position[1]) != myPieces:
            break
        while(1):
            if board.get_square_color(current_position[0], current_position[1]) == myPieces:
                stable_pieces[current_position[0]][current_position[1]] = 1
                current_position[0] += vertical_step[0]
                current_position[1] += vertical_step[1]
            else:
                current_position[1] += horizontal_step[1]
                vertical_limit = current_position[0]
                current_position[0] = initial_position[0]
                break
