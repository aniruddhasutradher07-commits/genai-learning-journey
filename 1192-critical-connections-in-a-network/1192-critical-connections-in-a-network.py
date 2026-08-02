class Solution(object):
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        disc = [-1] * n
        low = [0] * n
        parent = [-1] * n
        it = [0] * n  # tracks how many neighbors of each node we've processed
        result = []
        timer = 0
        
        for s in range(n):
            if disc[s] != -1:
                continue
            
            stack = [s]
            disc[s] = low[s] = timer
            timer += 1
            
            while stack:
                u = stack[-1]
                
                if it[u] < len(graph[u]):
                    v = graph[u][it[u]]
                    it[u] += 1
                    
                    if v == parent[u]:
                        continue
                    
                    if disc[v] == -1:
                        disc[v] = low[v] = timer
                        timer += 1
                        parent[v] = u
                        stack.append(v)
                    else:
                        low[u] = min(low[u], disc[v])
                else:
                    stack.pop()
                    if stack:
                        p = stack[-1]
                        low[p] = min(low[p], low[u])
                        if low[u] > disc[p]:
                            result.append([p, u])
        
        return result