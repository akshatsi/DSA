# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res):
            if not node:
                return 0

            left_depth = diameter(node.left,res)
            right_depth = diameter(node.right,res)
            res[0] = max(res[0], left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        res = [0]
        diameter(root,res)
        return res[0]