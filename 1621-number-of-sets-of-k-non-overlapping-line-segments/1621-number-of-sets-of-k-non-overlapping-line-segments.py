class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1
            
        for segs in range(1, k + 1):
            prefix = 0
            for i in range(1, n):
                prefix = (prefix + dp[i-1][segs-1]) % MOD
                dp[i][segs] = (dp[i-1][segs] + prefix) % MOD
                
        return dp[n-1][k]