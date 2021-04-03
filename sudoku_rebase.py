import numpy as np
import time
from BasicLogic import BasicLogic
bs = BasicLogic()

start_time = time.time()
subtractSet = {1,2,3,4,5,6,7,8,9}

hardPuzzle = np.array(
    [0,4,9,0,0,0,0,0,5,
     0,0,0,8,3,1,0,0,0,
     0,0,0,0,0,0,0,0,8,
     0,0,0,0,9,0,8,1,0,
     0,0,0,0,0,7,6,0,0,
     0,0,1,0,0,0,3,0,0,
     7,8,0,4,1,0,0,0,9,
     2,9,4,7,0,0,0,0,0,
     6,0,0,9,0,0,0,0,0]
)

easyPuzzle = np.array(
    [7,0,3,1,0,0,9,0,4,
    4,0,5,0,0,0,0,7,3,
    0,2,0,3,0,4,1,0,5,
    6,7,0,0,3,0,0,8,9,
    0,3,1,6,4,0,0,5,0,
    0,0,0,0,2,0,0,1,0,
    0,0,0,4,0,0,2,0,8,
    0,0,6,2,0,8,5,0,0,
    0,0,4,7,5,0,6,9,0]
)

puzzle = hardPuzzle.reshape(9,9)

def SimpleSolver():
    recursionCounter = 0
    while not bs.getSolved(puzzle):
        recursionCounter += 1
        for x in range(9):
            for y in range(9):
                if puzzle[x][y] == 0:
                    valids = bs.getPossible((x,y), puzzle)
                    if len(valids) == 1:
                        puzzle[x][y] = valids[0]

                        # If we successfully fill in a number then we are still solving
                        recursionCounter -= 1
        
        if recursionCounter > 5:
            return (0, puzzle)

    return (1, puzzle)


def SimpleSolverTwo(puzzle):
    puzzle = puzzle.copy()
    recursionCounter = 0
    while not bs.getSolved(puzzle):

        recursionCounter += 1

        # Rows
        for x in range(9):
            valids = bs.getPossibleForNumber(puzzle, 1, x)
            for number in [1,2,3,4,5,6,7,8,9]:
                valids_temp = valids[number - 1].tolist()
                if valids_temp.count(1) == 1:
                    square = np.where(np.array(valids_temp) == 1)[0][0]
                    assert puzzle[x][square] == 0 
                    puzzle[x][square] = number
                    
                    # If we successfully fill in a number then we are still solving
                    recursionCounter -= 1

        # Columns
        for x in range(9):
            valids = bs.getPossibleForNumber(puzzle, 2, x)
            for number in [1,2,3,4,5,6,7,8,9]:
                valids_temp = valids[number - 1].tolist()
                if valids_temp.count(1) == 1:
                    square = np.where(np.array(valids_temp) == 1)[0][0]
                    assert puzzle[square][x] == 0
                    puzzle[square][x] = number
                    
                    # If we successfully fill in a number then we are still solving
                    recursionCounter -= 1
                    print(puzzle)


        
        # Squares
        for x in range(9):
            threeCoords = bs.getSquaresInBigSquares(x)
            valids = bs.getPossibleForNumber(puzzle, 3, x)
            for number in [1,2,3,4,5,6,7,8,9]:
                valids_temp = valids[number - 1].tolist()
                if valids_temp.count(1) == 1:
                    square = np.where(np.array(valids_temp) == 1)[0]
                    coord= threeCoords[square[0]]
                    print(x)
                    print(coord)
                    print(number)
                    assert puzzle[coord[0]][coord[1]] == 0
                    puzzle[coord[0]][coord[1]] = number
                    
                    # If we successfully fill in a number then we are still solving
                    recursionCounter -= 1

                    print(puzzle)
                    raise RecursionError
        
        if recursionCounter > 5:
            return (0, puzzle)

    return (1, puzzle)



result = SimpleSolver()

result = SimpleSolverTwo(puzzle)

if result[0] == 1:
    print("Solved Successfully with result: \n", result[1])
elif result[0] == 0:
    print("Could not solve! Maybe this puzzle requires logic not yet implemented! Here is where it got stuck: \n", result[1])

