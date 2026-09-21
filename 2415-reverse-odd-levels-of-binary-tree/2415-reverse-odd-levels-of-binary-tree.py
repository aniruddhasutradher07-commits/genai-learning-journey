from collections import deque

class Solution:
    def reverseOddLevels(self, root):
        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            nodes = []

            for _ in range(size):
                node = queue.popleft()
                nodes.append(node)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                values = [node.val for node in nodes]
                values.reverse()

                for node, value in zip(nodes, values):
                    node.val = value

            level += 1

        return root