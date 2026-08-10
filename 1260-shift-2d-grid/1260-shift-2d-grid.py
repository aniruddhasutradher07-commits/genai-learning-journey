class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        flat = [grid[i][j] for i in range(m) for j in range(n)]

        shifted = flat[-k:] + flat[:-k] if k != 0 else flat

        result = [[0] * n for _ in range(m)]
        for idx, val in enumerate(shifted):
            result[idx // n][idx % n] = val

        return result    