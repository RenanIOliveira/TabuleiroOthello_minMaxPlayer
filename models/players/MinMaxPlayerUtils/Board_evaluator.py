

def evaluateBoard(board, heuristics_list, *weights_list):
    if len(weights_list) != 0:
        weights = weights_list[0]
        return evaluateBoardWithWeights(board, heuristics_list, weights)
    else:
        return evaluateBoardWithoutWeights(board, heuristics_list)


def evaluateBoardWithoutWeights(board, heuristics_list):
    board_value = 0
    for heuristic in heuristics_list:
        board_value += heuristic(board)

    return board_value


def evaluateBoardWithWeights(board, heuristics_list, weights):

    if len(heuristics_list) != len(weights):
        raise Exception('heuristics_list and weights_list have diferent sizes')
    board_value = 0
    for i in range(0, len(heuristics_list)):
        board_value += weights[i] * heuristics_list[i](board)

    return board_value
