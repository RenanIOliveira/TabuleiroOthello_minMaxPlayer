

def EvaluateBoard(board, heuristics_list, *weights_list):
    """Computes the distance from the origin to the point (x, y)
    
    :param board: the point's x-coordinate
    :param heuristics_list: the point's y-coordinate
    :return: number. the distance from (0, 0) to the point (x, y)
     """
    if len(weights_list) != 0:
        weights = weights_list[0]
        return EvaluateBoardWithWeights(board, heuristics_list, weights)
    else:
        return EvaluateBoardWithoutWeights(board, heuristics_list)
    

def EvaluateBoardWithoutWeights(board, heuristics_list):
    board_value = 0
    for heuristic in heuristics_list:
        board_value += heuristic(board)

    return board_value


def EvaluateBoardWithWeights(board, heuristics_list, weights):
    
    if len(heuristics_list) != len(weights):
        raise Exception('heuristics_list and weights_list have diferent sizes')
    board_value = 0
    for i in range(0, len(heuristics_list)):
        board_value += weights[i] * heuristics_list[i](board)
    
    return board_value


