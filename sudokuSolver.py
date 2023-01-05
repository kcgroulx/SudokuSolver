
#Created by Kyle Groulx, Jan 2nd, 2023.
#A Python script take user input for an unsolved Sudoku puzzle and prints the solved puzzle.

#Checks for duplicates of num in array
def hasDuplicates(array, x, y):
    if array[x][y] == 0:
        return False
    row = array[x]
    column = [row[x] for row in array]
    return row.count(array[x][y]) > 1 or column.count(array[x][y]) > 1


def solveSudoku(array):
    size = len(array[0])

    #if there are no 0s, the array is solved and returned
    if sum(x.count(0) for x in array) == 0:
        return array

    #interates through for a 0.
    for row in range(size):
        for column in range(size):
            if array[row][column] == 0:
                for i in range(1, size+1):
                    array[row][column] = i
                    if hasDuplicates(array, row, column) == False:
                        return solveSudoku(array)

    

#Gets 2D array Input from user and saves it into 2D array, numbers.
inputString = input("Enter 9x9 Sudoku puzzle: \n")
rows = inputString.split(',')
numbers = [row.split() for row in rows] 
numbers = [[int(x) for x in row] for row in numbers]

solveSudoku(numbers)

print(numbers)
            







