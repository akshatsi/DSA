class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, level):
            if not node:
                return

            if level == len(ans):
                ans.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return ans