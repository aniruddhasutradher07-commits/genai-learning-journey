class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        maxLocal = []  
        
        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = max(
                    grid[r][c] 
                    for r in range(i, i + 3) 
                    for c in range(j, j + 3)
                )
                row.append(max_val)
            maxLocal.append(row)
            
        return maxLocal