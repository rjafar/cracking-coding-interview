# 1.8 Algorithm that zeroes out the row and col of a matrix if a 0 entry is found
# Input: MxN matrix
# Output: MxN matrix with some 0s
# Time Complexity: O(MN) 

def zeroMatrix(matrix):
    M = len(matrix)  # set up variables and arrays
    N = len(matrix[0])
    row = [None]*M
    col = [None]*N

    for i in range(M): # check whole matrix for 0's and mark it in the row or col array
        for j in range(N):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(M): # using marker where 0 is in row array, change the columns of matrix along row to 0
        if row[i] == True:
            for j in range(N):
                matrix[i][j] = 0
    for i in range(N): # using marker where 0 is in col array, change the rows of matrix along row to 0
        if col[i] == True:
            for j in range(M):
                matrix[j][i] = 0   
    return matrix

matrix = [[5,2],
        [3,0],
        [4,5]]
result = zeroMatrix(matrix) 
print(result)

