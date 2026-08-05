from collections import deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)

        suspicious = set([k])
        queue = deque([k])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    queue.append(nxt)

        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        return [m for m in range(n) if m not in suspicious]