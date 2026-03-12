class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''new_sub = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                new_sub.append(arr[i:j+1])
        sum = 0
        for i in new_sub:
            sum += min(i)
            

        return sum'''

        mod = 10**9 + 7
        res = 0
        stack = []
        for i in range(len(arr) + 1):
            while (stack and (i == len(arr) or arr[stack[-1]]>= arr[i])):
                mid = stack.pop()
                left = mid - (stack[-1] if stack else -1)
                right = i - mid
                res += arr[mid] * left * right
            stack.append(i)

        return res % mod





        

