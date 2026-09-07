class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):

        def get_leaves(root):
            leaves = []

            def dfs(node):
                if node is None:
                    return

                if node.left is None and node.right is None:
                    leaves.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        return get_leaves(root1) == get_leaves(root2)