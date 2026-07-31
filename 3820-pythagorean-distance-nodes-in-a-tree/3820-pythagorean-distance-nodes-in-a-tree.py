class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(src):
            dist = [-1] * n
            dist[src] = 0
            q = deque([src])
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        q.append(nei)

            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        count = 0
        for i in range(n):
            a,b,c = sorted([dx[i], dy[i], dz[i]])
            if a * a + b * b == c * c:
                count += 1
        return count
                                     
        