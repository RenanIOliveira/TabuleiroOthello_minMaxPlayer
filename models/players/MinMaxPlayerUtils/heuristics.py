

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


stable_pieces = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]


def stability(board, myPieces):
    global corners
    if(myPieces == board.WHITE):
        theirPieces = board.BLACK
    else:
        theirPieces = board.WHITE

    resetStables()

    for corner in corners:
        setStables(board, myPieces, corner[0], corner[1])

    myStables = countAndResetStables()

    for corner in corners:
        setStables(board, theirPieces, corner[0], corner[1])

    theirStables = countAndResetStables()

    return myStables - theirStables


def resetStables():
    for i in range(1, 9):
        for j in range(1, 9):
            stable_pieces[i][j] = 0


def countAndResetStables():
    total = 0
    for i in range(1, 9):
        for j in range(1, 9):
            stable_piece = stable_pieces[i][j]
            if stable_piece == 1:
                total += 1
                stable_pieces[i][j] = 0
    return total


in_queue = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]


def setStables(board, myPieces, x, y):
    global stable_pieces
    global in_queue
    q = queue()
    in_queue[x][y] = 1
    q.enqueue([x, y])

    if (stable_pieces[x][y] == 1):
        return

    while(not q.empty()):
        position = q.dequeue()
        x = position[0]
        y = position[1]
        in_queue[x][y] = 0
        if checkNeighborsStablity(x, y) and board.get_square_color(x, y) == myPieces:
            stable_pieces[x][y] = 1

            if(stable_pieces[x][y+1] == 0 and in_queue[x][y] == 0):
                q.enqueue([x, y+1])
                in_queue[x][y+1] = 1
            if stable_pieces[x][y-1] == 0 and in_queue[x][y] == 0:
                q.enqueue([x, y-1])
                in_queue[x][y-1] = 1
            if(stable_pieces[x+1][y] == 0)and in_queue[x+1][y] == 0:
                q.enqueue([x+1, y])
                in_queue[x+1][y] = 1
            if(stable_pieces[x-1][y] == 0)and in_queue[x-1][y] == 0:
                q.enqueue([x-1, y])
                in_queue[x-1][y] = 1


def checkNeighborsStablity(x, y):
    # returns true if the cell has stable neighbors in four or more directions
    horizontal_neighbors = [[x, y+1], [x, y-1]]
    vertical_neighbors = [[x+1, y], [x-1, y]]
    up_diagonal = [[x-1, y+1], [x+1, y-1]]
    down_diagonal = [[x+1, y+1], [x-1, y-1]]

    neighbors = [horizontal_neighbors,
                 vertical_neighbors, up_diagonal, down_diagonal]

    n_stable_directions = 0
    for direction in neighbors:
        is_stable_direction = False
        for position in direction:
            if stable_pieces[position[0]][position[1]]:
                is_stable_direction = True
        if is_stable_direction is True:
            n_stable_directions += 1

    if(n_stable_directions >= 4):
        return True

    return False


def board_weights(board, myPieces):
    if(myPieces == board.WHITE):
        theirPieces = board.BLACK
    else:
        theirPieces = board.WHITE

    s_weigths = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 200, -100, 100,  50,  50, 100, -100,  200],
                 [0, - 100, -200, -50, -50, -50, -50, -200, -100],
                 [0, 100,  -50, 100,   0,   0, 100,  -50,  100],
                 [0,  50,  -50,   0,   0,   0,   0,  -50,   50],
                 [0,  50,  -50,   0,   0,   0,   0,  -50,   50],
                 [0, 100,  -50, 100,   0,   0, 100,  -50,  100],
                 [0, -100, -200, -50, -50, -50, -50, -200, -100],
                 [0, 200, -100, 100,  50,  50, 100, -100,  200]]

    total = 0
    for i in range(1, 9):
        for j in range(1, 9):
            thisColor = board.get_square_color(i, j)
            if(thisColor == myPieces):
                total += s_weigths[i][j]
            elif(thisColor == theirPieces):
                total += s_weigths[i][j]
    return total


class queue:
    content = []

    def __init__(self, List=None):
        if List is None:
            self.content = []
        else:
            self.content = List

    def enqueue(self, element):
        self.content.append(element)

    def dequeue(self):
        return self.content.pop(0)

    def empty(self):
        if(len(self.content) == 0):
            return True
        return False
