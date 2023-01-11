
#Created by Kyle Groulx, Jan 2nd, 2023.
#A Python script take user input for an unsolved Sudoku puzzle and prints the solved puzzle.


import math
import time

#Checks for Sudoku Violation in array, ignoring zero.
def hasDuplicates(array, row, col):
    num = array[row][col]
    if num == 0:
        return False
    rowArray = array[row]
    colArray = [rows[col] for rows in array]
    length = int(math.sqrt(len(array[0])))
    squareRow = int((row // length) * length)
    squareCol = int((col // length) * length)
    squareArray = []
    for row in range(squareRow, squareRow + length):
        for col in range(squareCol, squareCol + length):
            squareArray.append(array[row][col])

    return rowArray.count(num) > 1 or colArray.count(num) > 1 or squareArray.count(num) > 1


def solveSudoku(array):
    size = len(array[0])
    #if there are no 0s, the array is solved and returned
    if sum(x.count(0) for x in array) == 0:
        return array
    #interates through for a 0.
    for row in range(size):
        for col in range(size):
            if array[row][col] == 0:
                for i in range(1, size+1):
                    array[row][col] = i
                    if hasDuplicates(array, row, col) == False:
                        result = solveSudoku(array)
                        if result != False:
                            return result
                array[row][col] = 0
                return False    


#Sample 2D unsolved sudokus.

unsolvedSudoku9x9 = [[8, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 3, 6, 0, 0, 0, 0, 0], 
                     [0, 7, 0, 0, 9, 0, 2, 0, 0], 
                     [0, 5, 0, 0, 0, 7, 0, 0, 0], 
                     [0, 0, 0, 0, 4, 5, 7, 0, 0], 
                     [0, 0, 0, 1, 0, 0, 0, 3, 0], 
                     [0, 0, 1, 0, 0, 0, 0, 6, 8], 
                     [0, 0, 8, 5, 0, 0, 0, 1, 0], 
                     [0, 9, 0, 0, 0, 0, 4, 0, 0]]

unsolvedSudoku16x16 = [[ 0, 7, 0, 0, 0,10,14, 5, 2, 0, 0, 0, 0, 8,11, 0],
                       [ 0, 3, 0, 0, 8,13, 0, 0, 0, 0, 0, 4, 0, 1, 0,14],
                       [ 2, 0, 0,11, 0,12, 0, 0, 1, 0, 3, 6, 0, 0,15, 0],
                       [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                       [ 0,14, 0,15, 0, 0, 0,11,10, 5, 2, 9, 8, 0, 0, 0],
                       [ 0, 9, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0,13,11, 0, 0],
                       [11, 0, 0, 0, 0, 0,15, 0, 0, 0, 0, 0, 9,10, 0, 0],
                       [ 0,12, 4, 0, 0, 0, 0, 0,14, 0, 0, 0, 0, 0, 0, 0],
                       [ 0, 0, 0,13, 0,14, 0, 1, 0, 0, 0,10, 0, 0, 0, 9],
                       [ 0, 0, 0,14, 0,11, 2, 6, 0, 0, 0, 8, 0,13, 0, 0],
                       [ 0,10, 7, 3, 0, 0,13, 0,12, 1, 0, 0, 0, 0, 0, 8],
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0,11, 0, 0, 0],
                       [12, 0, 0, 0, 0, 0, 0, 8, 0,15, 0, 0, 6, 5, 0,10],
                       [15, 0, 0, 0, 0, 0, 7, 0,11, 0, 4,14, 0, 0, 2, 0],
                       [ 0, 0,13, 0, 0, 0,10, 0, 5, 9, 0, 0, 0, 0, 0, 7],
                       [ 0, 1, 0, 2, 0,14, 6, 0, 0, 0, 0,12, 0, 0, 0, 0]]


unsolvedSudoku25x25 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

start = time.perf_counter()
print("\nSolving...\n")
solvedSudoku = solveSudoku(unsolvedSudoku16x16)
end = time.perf_counter()
if solvedSudoku != False: 
    print("Solution:\n")
    for row in solvedSudoku:
        print(row)
    print(f"Time to solve: {end - start:0.6f} seconds\n")
else:
    print("Unable to find Solution\n")
