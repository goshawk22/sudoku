import numpy as np
import time
from BasicLogic import BasicLogic
bs = BasicLogic()
import random

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

def SimpleSolver(puzzle_in):
    puzzle = puzzle_in.copy()
    assert bs.isValid(puzzle)
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
            return puzzle

    return puzzle

def makeGuess(puzzle_in):
    puzzle = puzzle_in.copy()
    assert bs.isValid(puzzle)
    assert (0 in puzzle)
    empty = bs.getEmptySquares(puzzle)
    valids = []
    for square in empty:
        valids.append(bs.getPossible(square, puzzle))
       
    lengths = [len(x) for x in valids]
    min_len = min(lengths)
        
    for i in range(len(valids)):
        if len(valids[i]) == min_len:
            number = random.randint(0,1)
            assert puzzle[tuple(empty[i])] == 0
            puzzle[tuple(empty[i])] = valids[i][number]

            solution = solve(puzzle)
            if solution is not False:
                return solution
            
            puzzle[empty[i]] = 0

    return (1, puzzle)


result = SimpleSolver()

if result[0] == 1:
    print("Solved Successfully with result: \n", result[1])
elif result[0] == 0:
    print("Could not solve! Maybe this puzzle requires logic not yet implemented! Here is where it got stuck: \n", result[1])

