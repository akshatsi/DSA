class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        arr = []
        up = 0
        right = n - 1
        left = 0
        bottom = m - 1

        while up<= bottom and left<= right:
            for i in range(left , right+1):
                arr.append(matrix[up][i])
            up += 1
            for i in range(up,bottom+1):
                arr.append(matrix[i][right])
            right -= 1
            if up <= bottom:
                for i in range(right,left-1, -1):
                    arr.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom,up-1,-1):
                    arr.append(matrix[i][left])
                left+=1
        return arr    
            
        