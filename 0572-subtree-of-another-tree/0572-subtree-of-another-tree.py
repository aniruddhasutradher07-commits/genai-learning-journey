# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val !=b.val:
                return False
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)                           