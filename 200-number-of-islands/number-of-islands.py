class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        def isValid(i, j, m, n):
            return 0 <= i < m and 0 <= j < n

        def dfs(grid, i, j, m, n, visited):
            visited[i][j] = 1

            for k in range(4):
                row = i + x[k]
                col = j + y[k]

                if (
                    isValid(row, col, m, n)
                    and grid[row][col] == '1'
                    and not visited[row][col]
                ):
                    dfs(grid, row, col, m, n, visited)

        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, i, j, m, n, visited)
                    res += 1

        return res