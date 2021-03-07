import numpy as np
class BasicLogic():
    def __init__(self):
        self.subtractSet = {1,2,3,4,5,6,7,8,9}

    # Returns all the current values in the horizontal y.
    def checkHorizontal(self, y, puzzle):
        horizontal = []
        for x in range(9):
            if puzzle[y,x] != 0:
                horizontal.append(puzzle[y,x])
        return set(horizontal)

    # Returns all the current values in the vertical x.
    def checkVertical(self, x, puzzle):
        vertical = []
        for y in range(9):
            if puzzle[y,x] != 0:
                vertical.append(puzzle[y,x])
        return set(vertical)

    # Checks possible values in a 3x3 split
    def checkSquare(self, square, puzzle):
        splits = [] #Contains a list of all the squares (len 9)
        numbers = [] #Contains all the numbers in the square square
        horizontalSplit = np.hsplit(puzzle, 3)
        for split in horizontalSplit:
            for vSplit in np.vsplit(split, 3):
                splits.append(vSplit)

        split = splits[square]
        split = split.reshape(9)
        for x in range(9):
            numbers.append(split[x])
    
        numbers = set(numbers)

        return numbers

    # Gets the possible numbers for a square
    def getPossible(self, square, puzzle):
        vertical = self.subtractSet - self.checkVertical(square[1], puzzle)
        horizontal = self.subtractSet - self.checkHorizontal(square[0], puzzle)
        square = self.subtractSet - self.checkSquare(self.getThreeOfSquare(square), puzzle)
        valids = vertical.intersection(horizontal).intersection(square)
        return list(valids)
    
    # Returns a 9x9 grid of all the possible values for each square. 
    # If the square is currently empty (0) then it gets the possible numbers and if it is full (1-9) then it just puts the filled number in.
    def getPossibleWholeGrid(self, puzzle):
        puzzleValids = np.zeros(9,9)
        for x in range(9):
            for y in range(9):
                if puzzle[x][y] == 0:
                    puzzleValids[x][y] = self.getPossible((x,y), puzzle)
                else:
                    puzzleValids[x][y] = puzzle[x][y]
        
        return puzzleValids
    
    # Gets the possible places a number can go in any given row, column or small square.
    # Returns a 9x9 grid where the x axis corralates to the number it is checking and the y axis is a boolean for whether the number can go in each square in the set.
    # typeCheck is a value for row (1), column (2), small square (3) and rcs_number (row column square number) is the row/column/small square to check
    def getPossibleForNumber(self, puzzle, typeCheck, rcs_number):
        possiblePlaces = np.zeros(9,9)
        if typeCheck == 1:
            for i in range(9):
                valids = self.getPossible((rcs_number, i), puzzle)
                for number in [1,2,3,4,5,6,7,8,9]:
                    if number in valids:
                        possiblePlaces[number, i] = 1
        
            return possiblePlaces

        if typeCheck == 2:
            for i in range(9):
                valids = self.getPossible((i, rcs_number), puzzle)
                for number in [1,2,3,4,5,6,7,8,9]:
                    if number in valids:
                        possiblePlaces[number, i] = 1
        
            return possiblePlaces

        if typeCheck == 3:
            for i in self.getSquaresInBigSquares(rcs_number):
                valids = self.getPossible(i, puzzle)
                for number in [1,2,3,4,5,6,7,8,9]:
                    if number in valids:
                        possiblePlaces[number, i] = 1
        
            return possiblePlaces


    # Gets which 3x3 square a number/square is in.
    '''
    [0 1 2
     3 4 5
     6 7 8]
    '''
    def getThreeOfSquare(self, square):

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
    
    # Gets a list of coordinates that make up a big square.
    def getSquaresInBigSquares(self, big_square):
        coords = []
        for x in range(9):
            for y in range(9):
                if self.getThreeOfSquare([x,y]) == big_square:
                    coords.append([x,y])
    
        assert len(coords) == 9
        return coords

    # Checks if the puzzle has been solved, but does not check if it is correct.
    def getSolved(self, puzzle):
        if 0 in puzzle:
            return False
        else:
            return True

