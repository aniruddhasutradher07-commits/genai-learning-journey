class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        submatrix = []

        for i in range(x, x + k):
            row_part = grid[i][y:y+k]
            submatrix.append(row_part)


        submatrix.reverse()

        for i in range(k):
            grid_row = x + i
            for j in range(k):
                grid_col = y + j
                grid[grid_row][grid_col]=submatrix[i][j]

        return grid        