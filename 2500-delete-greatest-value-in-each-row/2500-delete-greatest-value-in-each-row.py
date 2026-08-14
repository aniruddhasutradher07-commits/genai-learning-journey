class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        n = len(grid[0])
        answer = 0

        for col in range(n):
            answer += max(row[col] for row in grid) 

        return answer       