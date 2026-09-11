from typing import Optional

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, None)]

        while queue:
            next_level = []
            found_x = None
            found_y = None

            for node, parent in queue:
                if node.val == x:
                    found_x = parent

                if node.val == y:
                    found_y = parent

                if node.left:
                    next_level.append((node.left, node))

                if node.right:
                    next_level.append((node.right, node))
                    
            if found_x is not None and found_y is not None:
                return found_x != found_y
            if found_x is not None or found_y is not None:
                return False

            queue = next_level

        return False