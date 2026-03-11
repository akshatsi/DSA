class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        n = len(nums)
        for i in range(2 *n -1, -1, -1):
            ind = i % n
            curr = nums[ind]
            while stack and nums[ind] >= stack[-1]:
                stack.pop()

            if i < n:
                if stack:
                    ans[i] = stack[-1]

            stack.append(curr)

        return ans


