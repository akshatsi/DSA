class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def isValid(i, j, m, n):
            return 0 <= i < m and 0 <= j < n

        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        m = len(grid)
        n = len(grid[0])
        q = deque()


        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0


        while q:
            i, j = q.popleft()

            for k in range(4):
                row = i + x[k]
                col = j + y[k]

                if isValid(row, col, m, n) and grid[row][col] == 1:
                    grid[row][col] = 0
                    q.append((row, col))


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1

        return res