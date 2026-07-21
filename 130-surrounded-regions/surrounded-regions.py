class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i,j,m,n):
            return (0<= i < m and 0 <= j <n)
        def dfs(i,j,m,n, board):
            board[i][j] = '*'
            for k in range(4):
                row = i + x[k]
                col = j + y[k]

                if isValid(row,col, m ,n ) and board[row][col] == 'O':
                    dfs(row,col, m, n , board)

            return
        m = len(board)
        n = len(board[0])

        x = [-1 ,1 ,0 , 0]
        y = [0, 0 , -1, 1]

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j,m,n,board)
        for j in range(n):
            if board[-1][j] == 'O':
                dfs(m-1,j,m,n,board)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0,m,n,board)
        for i in range(m):
            if board[i][n-1] == 'O':
                dfs(i,n-1,m,n,board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                
                else:
                    board[i][j] = 'X'



        