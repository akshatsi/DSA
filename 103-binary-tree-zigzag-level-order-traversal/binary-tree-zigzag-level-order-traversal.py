class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [root]
        leftToRight = True

        while queue:
            level_size = len(queue)
            temp = []

            for i in range(level_size):
                node = queue.pop(0)
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not leftToRight:
                temp.reverse()

            ans.append(temp)
            leftToRight = not leftToRight

        return ans