from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        result = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(1, n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = sum(x != 0 for x in graph[c])

        q = deque()

        for c in range(1, n):
            result[0][c][0] = 1
            result[0][c][1] = 1
            q.append((0, c, 0))
            q.append((0, c, 1))

        for m in range(1, n):
            result[m][m][0] = 2
            result[m][m][1] = 2
            q.append((m, m, 0))
            q.append((m, m, 1))

        while q:
            mouse, cat, turn = q.popleft()
            winner = result[mouse][cat][turn]

            if turn == 0:
                prev_states = []

                for prev_cat in graph[cat]:
                    if prev_cat != 0:
                        prev_states.append((mouse, prev_cat, 1))

            else:
                prev_states = [
                    (prev_mouse, cat, 0)
                    for prev_mouse in graph[mouse]
                ]

            for pm, pc, prev_turn in prev_states:
                if result[pm][pc][prev_turn] != 0:
                    continue
                if (prev_turn == 0 and winner == 1) or \
                   (prev_turn == 1 and winner == 2):

                    result[pm][pc][prev_turn] = winner
                    q.append((pm, pc, prev_turn))

                else:
                    degree[pm][pc][prev_turn] -= 1
                    if degree[pm][pc][prev_turn] == 0:

                        if prev_turn == 0:
                            result[pm][pc][prev_turn] = 2
                        else:
                            result[pm][pc][prev_turn] = 1

                        q.append((pm, pc, prev_turn))

        return result[1][2][0]