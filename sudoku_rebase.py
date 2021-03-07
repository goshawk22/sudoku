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

while not bs.getSolved(puzzle1):
    for x in range(9):
        for y in range(9):
            if puzzle1[x][y] == 0:
                valids = bs.getPossible((x,y), puzzle1)
                if len(valids) == 1:
                    puzzle1[x][y] = valids[0]

print(puzzle1)