class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h == 0:
                    continue

                ans += 2

                ans += 4 * h

                if j + 1 < n:
                    ans -= 2 * min(h, grid[i][j + 1])

                if i + 1 < n:
                    ans -= 2 * min(h, grid[i + 1][j])

        return ans                    