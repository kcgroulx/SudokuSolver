
#Created by Kyle Groulx, Jan 2nd, 2023.
#A Python script take user input for an unsolved Sudoku puzzle and prints the solved puzzle.

#Checks for Sudoku Violation in array, ignoring zero.
def hasDuplicates(array, row, col):
    num = array[row][col]
    if num == 0:
        return False
    rowArray = array[row]
    colArray = [rows[col] for rows in array]
    return rowArray.count(num) > 1 or colArray.count(num) > 1


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



    

#Gets 2D array Input from user and saves it into 2D array, numbers.
inputString = input("Enter 9x9 Sudoku puzzle: \n")
rows = inputString.split(',')
numbers = [row.split() for row in rows] 
numbers = [[int(x) for x in row] for row in numbers]

solvedSudoku = solveSudoku(numbers)
for row in solvedSudoku:
    print(row)
            







