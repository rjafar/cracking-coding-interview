# 1.7 Algorithm to rotate a NxN matrix 90 degrees clockwise
# Input: NxN matrix
# Output: 90 degree rotated NxN matrix 
# Time Complexity: O(N^2) where N is the matrix size

def rotateMatrix(matrix):
    N = len(matrix) # length of matrix
    for row in range(int(N/2)): # row iterates until middle
        for col in range(row, N-row-1): 
            temp = matrix[row][col] # save top val
            matrix[row][col] = matrix[N-1-col][row] # rotate left to top
            matrix[N-1-col][row] = matrix[N-1-row][N-1-col] # rotate bottom to left
            matrix[N-1-row][N-1-col] = matrix[col][N-1-row] # rotate right to bottom
            matrix[col][N-1-row] = temp # put saved top in right
    return matrix

matrix = [[0 for x in range(3)] for y in range(3)]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(rotateMatrix(matrix))