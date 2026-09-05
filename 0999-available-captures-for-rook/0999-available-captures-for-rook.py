class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break

        count = 0

        for i in range(r - 1, -1, -1):
            if board[i][c] == 'B':
                break
            if board[i][c] == 'p':
                count += 1
                break

        for i in range(r + 1, 8):
            if board[i][c] == 'B':
                break
            if board[i][c] == 'p':
                count += 1
                break

        for j in range(c - 1, -1, -1):
            if board[r][j] == 'B':
                break
            if board[r][j] == 'p':
                count += 1
                break

        for j in range(c + 1, 8):
            if board[r][j] == 'B':
                break
            if board[r][j] == 'p':
                count += 1
                break

        return count