class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
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
                    matrix[i][j] = 0



        