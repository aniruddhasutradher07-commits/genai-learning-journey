class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        
        def dfs(orig):
            if orig in visited:
                return visited[orig]
            
            copy = Node(orig.val)
            visited[orig] = copy
            
            for neighbor in orig.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)