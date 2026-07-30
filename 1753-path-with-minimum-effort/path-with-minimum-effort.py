class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def isValid(i,j,m,n):
            return 0 <= i < m and 0 <= j < n
        m = len(heights)
        n = len(heights[0])
        x = [-1,1,0,0]
        y = [0,0, -1,1]
        res = [[float('inf')] * n for _ in range(m)]
        
        pq = []
        heapq.heappush(pq, [0,0,0])
        res[0][0] = 0

        while pq:
            dis, row,col = heapq.heappop(pq)

            if dis > res[row][col]:
                continue

            for k in range(4):
                r = row + x[k]
                c = col + y[k]
                if not isValid(r,c,m,n):
                    continue

                diff = abs(heights[row][col] - heights[r][c])

                ans = max(diff, dis)

                if ans < res[r][c]:
                    res[r][c] = ans

                    heapq.heappush(pq,[ans,r,c])

        return res[m-1][n-1]


