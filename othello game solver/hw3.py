import gamePlay
import simpleGreedy
from copy import deepcopy

def nextMove(board, color):
    (value, move) = max_value(board, "W", float('-inf'), float('inf'), 3)
    return move

def max_value(board, color, alpha = float('-inf'), beta = float('inf'), depth = 3):
    if depth == 0 or gamePlay.gameOver(board):
        return (simpleGreedy.value(board), None)
    val = float('-inf')
    #find all valid successors:
    max_moves = []
    bestMove = None
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, "W", (i, j)):
                max_moves.append((i, j))
    if(len(max_moves) == 0):
        return ("pass", "pass")
    #for each position in successors:
    for s in max_moves:
        newBoard = deepcopy(board)
        gamePlay.doMove(newBoard, "W", s)
        cmp, x = min_value(newBoard, "B", alpha, beta, depth-1)
        if cmp >= val:
            val = cmp
            bestMove = s
        alpha = max(alpha, val)
        #alpha beta pruning
        if beta <= alpha:
            break
    return (val, bestMove)

def min_value(board, color, alpha = float('-inf'), beta = float('inf'), depth = 3):
    if depth == 0 or gamePlay.gameOver(board):
        return (simpleGreedy.value(board), None)
    val = float('inf')
    #find all valid successors:
    min_moves = []
    bestMove = None
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, "B", (i, j)):
                min_moves.append((i, j))
    if(len(min_moves) == 0):
        return ("pass", "pass")
    #for each positions in successors:
    for s in min_moves:
        newBoard = deepcopy(board)
        gamePlay.doMove(newBoard, "B", s)
        cmp, x = max_value(newBoard, "W", alpha, beta, depth-1)
        if cmp <= val:
            val = cmp
            bestMove = s
        beta = min(beta, val)
        if beta <= alpha:
            break
    return (val, bestMove)

#Bonus:
#I calculate the value by finding the difference in coins between 2 players:
def my_value(board):
    count_white = 0
    count_black = 0
    for row in board:
        for ele in row:
            if ele == "W":
                count_white += 1
            elif ele == "B":
                count_black += 1
    value = (100 * (count_white - count_black)) / (count_white + count_black)
    return value

#test for my_value:
test = [["W", "B", "W"],["W", "W", "W"],["B", "B", "B"]]
print(my_value(test))
