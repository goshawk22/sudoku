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
        square = self.subtractSet - self.checkSquare(self.getThreeOfSquare(square, puzzle), puzzle)
        valids = vertical.intersection(horizontal).intersection(square)
        return list(valids)

    # Gets which 3x3 square a number/square is in.
    '''
    [0 1 2
     3 4 5
     6 7 8]
    '''
    def getThreeOfSquare(self, square, puzzle):

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

    def getSolved(self, puzzle):
        if 0 in puzzle:
            return False
        else:
            return True

