class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x = [-1, 1, 0, 0] #x coordinates when up down left right
        y = [0, 0, -1, 1]#y coordinates when up down left right

        def isValid(i,j,m,n):
            return 0<= i < m and 0<= j < n
        
        m = len(grid)
        n = len(grid[0])
        fresh = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    grid[i][j] = -2 #marking the 2s to any other number to mark the 2 as visited

                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
                
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                for k in range (4):
                    row, col = i + x[k], j + y[k]

                    if (
                        isValid(row,col, m,n)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = -2
                        fresh -= 1
                        q.append([row, col])




        if fresh > 0:
            return -1

        return time
