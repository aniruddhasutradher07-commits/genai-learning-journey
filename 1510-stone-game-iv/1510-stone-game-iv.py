class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = bytearray(n + 1) 
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1
        
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                if not dp[i - sq]:
                    dp[i] = 1
                    break
        
        return bool(dp[n])