from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        def isValid(i, j, m, n):
            return 0 <= i < m and 0 <= j < n

        m = len(mat)
        n = len(mat[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            i, j = q.popleft()

            for k in range(4):
                row = i + x[k]
                col = j + y[k]

                if isValid(row, col, m, n) and mat[row][col] == -1:
                    mat[row][col] = mat[i][j] + 1
                    q.append((row, col))

        return mat