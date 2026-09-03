class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minimum = root.val
        second_min = float('inf')

        def dfs(node):
            nonlocal second_min

            if not node:
                return 

            if minimum < node.val < second_min:
                second_min = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return -1 if second_min == float('inf') else second_min            