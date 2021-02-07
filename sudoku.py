import numpy as np
import time
start_time = time.time()
subtractSet = {1,2,3,4,5,6,7,8,9}
reference_grid = np.array(range(81)).reshape(9,9)

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
    [2,0,4,0,0,0,1,0,0,
    1,0,7,0,9,0,8,0,2,
    0,0,0,0,0,0,7,0,0,
    6,0,0,0,3,1,9,0,4,
    0,4,0,0,2,0,6,1,3,
    8,3,1,6,4,9,2,5,7,
    4,0,0,9,6,0,3,7,0,
    0,0,0,0,0,0,4,2,9,
    0,0,0,3,0,0,5,6,0]
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


# Returns all the current values in the horizontal y.
def checkHorizontal(y, puzzle):
    horizontal = []
    for x in range(9):
        if puzzle[y,x] != 0:
            horizontal.append(puzzle[y,x])

    return set(horizontal)

# Returns all the current values in the vertical x.
def checkVertical(x, puzzle):
    vertical = []
    for y in range(9):
        if puzzle[y,x] != 0:
            vertical.append(puzzle[y,x])
    return set(vertical)

#Checks possible values in a 3x3 split
def checkSquare(square, puzzle):
    splits = [] #Contains a list of all the squares (len 9)
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

#Gets the possible numbers for a square
def getPossible(square, puzzle):
    vertical = subtractSet - checkVertical(square[1], puzzle)
    horizontal = subtractSet - checkHorizontal(square[0], puzzle)
    square = subtractSet - checkSquare(getThreeOfSquare(square), puzzle)
    valids = vertical.intersection(horizontal).intersection(square)
    return list(valids)

# Gets which 3x3 square a number/square is in.
def getThreeOfSquare(square):
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


### Harder Logic ###

# Returns a list of coordinates that are empty
def getEmptySquares(puzzle):
    return list(np.argwhere(puzzle == 0))

# Returns a list of length 9 with the valid numbers for each square in the row
def getValidsForRow(row_num, puzzle):
    valids = []
    for i in range(9):
        if puzzle[row_num, i] == 0:
            valids.append(getPossible([row_num, i], puzzle))
        else:
            valids.append([])
    
    return valids

# Returns a list of length 9 with the valid numbers for each square in the column
def getValidsForColumn(column_num, puzzle):
    valids = []
    for i in range(9):
        if puzzle[i, column_num] == 0:
            valids.append(getPossible([i, column_num], puzzle))
        else:
            valids.append([])
    
    return valids

# Gets a list of coordinates of squares that make up a 3x3 square
def getSquaresInBigSquares(big_square):
    coords = []
    for x in range(9):
        for y in range(9):
            if getThreeOfSquare([x,y]) == big_square:
                coords.append([x,y])
    
    assert len(coords) == 9
    return coords

# Returns a list of length 9 with the valid numbers for each square in the 3x3 square and a list of coordinates that each valids corresponds to
def getValidsForSquare(square_num, puzzle):
    valids = []
    squares = getSquaresInBigSquares(square_num)
    for i in squares:
        if puzzle[tuple(i)] == 0:
            valids.append(getPossible(i, puzzle))
        else:
            valids.append([])
    
    return valids, squares

#Gets the possible numbers for a square
def getPossibleWithList(square, puzzle):
    vertical = subtractSet - checkVertical(square[1], puzzle)
    horizontal = subtractSet - checkHorizontal(square[0], puzzle)
    square = subtractSet - checkSquare(getThreeOfSquare(square), puzzle)
    valids = vertical.intersection(horizontal).intersection(square)
    return list(valids)

def hardSolver(puzzle):
    tempPuzzle = puzzle
    for num in range(9):

        # Naked Pairs
        # Rows
        valids = getValidsForRow(num, puzzle)
        for valid in valids:
            if (valids.count(valid) > 1) and (valid != []):
                duplicate_valids = []
                for v in range(len(valids)):
                    if valids[v] == valid:
                        duplicate_valids.append(v)

                for i in duplicate_valids:
                    print(valid)
                    tempPuzzle[num,i] = valid

        # Columns
        valids = getValidsForColumn(num, puzzle)
        for valid in valids:
            if (valids.count(valid) > 1) and (valid != []):
                duplicate_valids = []
                for v in range(len(valids)):
                    if valids[v] == valid:
                        duplicate_valids.append(v)

                for i in duplicate_valids:
                    print(valid)
                    tempPuzzle[i,num] = valid
        
        # Squares
        valids, coords = getValidsForSquare(num, puzzle)
        for valid in valids:
            if (valids.count(valid) > 1) and (valid != []):
                duplicate_valids = []
                for v in range(len(valids)):
                    if valids[v] == valid:
                        duplicate_valids.append(v)
                for i in duplicate_valids:
                    print(valid)
                    tempPuzzle[tuple(coords[i])] = valid

    return tempPuzzle

def getSolved(puzzle):
    if 0 in puzzle:
        return False
    else:
        return True

def solve(puzzle):
    depth = 0
    while not getSolved(puzzle):
        for coordinate in getEmptySquares(puzzle):
            oldPuzzle = puzzle.copy()
            valid = getPossible(coordinate, puzzle)
            if len(valid) == 1:

                puzzle[coordinate[0], coordinate[1]] = valid[0]

                assert not np.array_equiv(puzzle, oldPuzzle)
                
                '''
                tempPuzzle = hardSolver(puzzle)
                results = solveDepthOne(tempPuzzle)
                if results == None:
                    continue
                else:
                    puzzle[results[0], results[1]] = results[3]
                '''

        if np.array_equiv(oldPuzzle, puzzle):
            depth += 1
        
        if depth == 10:
            print(puzzle)
            raise RecursionError

def solveDepthOne(puzzle):
    for coordinate in getEmptySquares(puzzle):
        valid = getPossible(coordinate, puzzle)
        if len(valid) == 1:
            puzzle[coordinate[0], coordinate[1]] = valid[0]
            return (coordinate[0], coordinate[1], valid[0])
    


solve(puzzle1.copy())

print("--- %s seconds ---" % (time.time() - start_time))