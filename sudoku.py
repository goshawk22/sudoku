import numpy as np
import time
start_time = time.time()
subtractSet = {1,2,3,4,5,6,7,8,9}

puzzle1 = np.array(
    [4,0,1,8,0,0,0,5,3,
    8,0,5,0,7,4,0,0,6,
    0,0,7,5,3,0,0,1,8,
    6,0,0,7,0,0,1,4,9,
    0,5,3,4,0,8,6,0,0,
    0,7,4,0,9,6,0,3,0,
    0,1,6,0,0,5,3,8,0,
    3,0,0,0,8,1,5,0,7,
    5,8,0,3,4,0,9,0,0]
)

puzzle1 = np.array(
    [0,5,0,6,0,0,0,2,0,
    0,0,3,8,0,0,7,0,6,
    7,0,0,0,4,0,0,0,0,
    0,0,0,0,7,4,9,0,0,
    0,0,0,1,0,8,0,0,0,
    0,0,1,3,5,0,0,0,0,
    0,0,0,0,9,0,0,0,8,
    2,0,4,0,0,1,6,8,8,
    0,8,0,0,0,6,0,3,0]
)

puzzle1 = puzzle1.reshape(9,9)
print(puzzle1)


def checkHorizontal(y, puzzle):
    #Returns all the current values in the horizontal y.
    horizontal = []
    for x in range(9):
        if puzzle[y,x] != 0:
            horizontal.append(puzzle[y,x])
    return set(horizontal)


def checkVertical(x, puzzle):
    #Returns all the current values in the vertical x.
    vertical = []
    for y in range(9):
        if puzzle[y,x] != 0:
            vertical.append(puzzle[y,x])
    return set(vertical)


def checkSquare(square, puzzle):
    #Checks possible values in a 3x3 split
    splits = [] #COntains a list of all the squares (len 9)
    numbers = [] #Contains all the numbers in the square square
    horizontalSplit = np.hsplit(puzzle, 3)
    for split in horizontalSplit:
        for vSplit in np.vsplit(split, 3):
            splits.append(vSplit)

    split = splits[square]
    #print(split)
    split = split.reshape(9)
    for x in range(9):
        numbers.append(split[x])
    
    numbers = set(numbers)

    return numbers


def getPossible(square, puzzle):
    #Gets the possible numbers for a square
    vertical = subtractSet - checkVertical(square[1], puzzle)
    horizontal = subtractSet - checkHorizontal(square[0], puzzle)
    square = subtractSet - checkSquare(getThreeOfSquare(square, puzzle), puzzle)
    #print(vertical, horizontal, square)
    valids = vertical.intersection(horizontal).intersection(square)
    return list(valids)


def getThreeOfSquare(square, puzzle):
    #Gets which 3x3 square a number/square is in.
    if square[1] < 3:
        if square[0] < 3:
            threeSquare = 0
        elif square[0] < 6:
            threeSquare = 1
        elif square[0] < 9:
            threeSquare = 2
    elif square[1] < 6:
        if square[0] < 3:
            threeSquare = 3
        elif square[0] < 6:
            threeSquare = 4
        elif square[0] < 9:
            threeSquare = 5
    elif square[1] < 9:
        if square[0] < 3:
            threeSquare = 6
        elif square[0] < 6:
            threeSquare = 7
        elif square[0] < 9:
            threeSquare = 8

    return threeSquare


def getSolved(puzzle):
    if 0 in puzzle:
        return False
    else:
        return True

#iter = 0
depth = 0
while True:
    #iter += 1
    #print(iter)
    #if iter % 1000:
        #print(puzzle)
    oldPuzzle = puzzle1
    for x in range(9):
        for y in range(9):
            if puzzle1[x,y] == 0:
                valid = getPossible([x,y], puzzle1.copy())
                if len(valid) == 1:
                    puzzle1[x,y] = valid[0]
                    #print(valid)


    if np.array_equiv(oldPuzzle, puzzle1):
        depth += 1
        
    if depth == 10:
        print("-------------------------------")
        print(puzzle1)
        raise RecursionError


print(puzzle1)
#print(0 in puzzle)

print("--- %s seconds ---" % (time.time() - start_time))