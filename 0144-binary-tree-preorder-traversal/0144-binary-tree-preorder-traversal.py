class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return result        
        