class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x = [-1,1,0,0]
        y = [0,0,-1,1]

        def isValid(i,j,m,n):
            return 0<= i < m and 0<= j < n

        m = len(image)
        n = len(image[0])
        q = deque()
        a = image[sr][sc]
        if a == color:
            return image
        image[sr][sc] = color
        q.append([sr,sc])
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                for k in range(4):
                    row = i + x[k]
                    col = j + y[k]

                    if isValid(row,col,m,n) and image[row][col] == a:
                        image[row][col] = color
                        q.append([row,col])
                        

        return image


