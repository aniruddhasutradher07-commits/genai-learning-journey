class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n =len(grid)

        top = 0
        front = 0
        side = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1

            front += max(grid[i])

        for j in range(n):
            column_max = 0

            for i in range(n):
                column_max = max(column_max, grid[i][j])

            side += column_max

        return top + front + side                    