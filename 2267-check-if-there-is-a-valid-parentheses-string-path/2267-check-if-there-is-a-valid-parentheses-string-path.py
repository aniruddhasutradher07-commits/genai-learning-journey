class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):
                if not dp[r][c]:
                    continue

                if c + 1 < n:
                    delta = 1 if grid[r][c+1] == '(' else - 1
                    for bal in dp[r][c]:
                        if bal + delta >= 0:
                            dp[r][c+1].add(bal + delta)

                if r + 1 < m:
                    delta = 1 if grid[r+1][c] == '(' else -1
                    for bal in dp[r][c]:
                        if bal + delta >= 0:
                            dp[r+1][c].add(bal + delta)

        return 0 in dp[m -1][n-1]
                                                    