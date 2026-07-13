class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = []
        curr = root
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        # Two pointers
        left, right = 0, len(res) - 1

        while left < right:
            total = res[left] + res[right]

            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False