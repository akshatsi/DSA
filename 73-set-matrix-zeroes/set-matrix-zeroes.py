class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        '''for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for col in range(len(matrix[0])):
                        if matrix[i][col] != 0:
                            matrix[i][col] = -298964
                    for row in range(len(matrix)):
                        if matrix[row][j] != 0:
                            matrix[row][j] = -298964
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -298964:
                    matrix[i][j] = 0'''
        '''better
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * m
        col= [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0 '''
        '''best'''

        m = len(matrix)
        n = len(matrix[0])

        first_row = False
        first_col = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break
        
        for i in range(n):
            if matrix[0][i] == 0:
                first_row = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for i in range(n):
                matrix[0][i] = 0
        if first_col:
            for j in range(m):
                matrix[j][0] = 0
        