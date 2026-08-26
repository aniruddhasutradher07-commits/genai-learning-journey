class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        minimum_diff = float("inf")

        def inorder(node):
            nonlocal prev, minimum_diff

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                minimum_diff = min(minimum_diff, node.val - prev)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return minimum_diff