import numpy as np

def diagonal_checker(matrix):
    """return number of diagonal xmas"""
    xmas_count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "X":
                try:
                    if matrix[y+1][x+1] == "M" and matrix[y+2][x+2] == "A" and matrix[y+3][x+3] == "S":
                        xmas_count += 1
                except:
                    break
    return xmas_count

def horizonal_checker(matrix):
    """return number of horizontal xmas"""
    xmas_count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "X":
                try:
                    if matrix[y][x + 1] == "M" and matrix[y][x + 2] == "A" and matrix[y][x + 3] == "S":
                        xmas_count += 1
                except:
                    break
    return xmas_count

def rotator(matrix):
    """do the checks, rotate the matrix"""
    total_count = 0
    for _ in range(4):
        total_count += horizonal_checker(matrix)
        total_count += diagonal_checker(matrix)
        matrix = np.rot90(matrix)
    return total_count
#
def mas_check(matrix):
    """check for mas cross"""
    xmas_count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "M":
                try:
                    if matrix[y][x+2] == "M" and matrix[y+1][x + 1] == "A" and matrix[y+2][x] == "S" and matrix[y+2][x+2] == "S":
                        xmas_count += 1
                except:
                    break
    return xmas_count

def mas_rotator(matrix):
    """"do the check, rotate the matrix"""
    total_count = 0
    for _ in range(4):
        total_count += mas_check(matrix)
        matrix = np.rot90(matrix)
    return total_count


with open("data.txt") as f:
    wordsearch = f.read().split("\n")
    wordsearch = [list(word) for word in wordsearch]
    wordsearch = np.array(wordsearch)

#part1
print(rotator(wordsearch))

#part2
print(mas_rotator(wordsearch))


