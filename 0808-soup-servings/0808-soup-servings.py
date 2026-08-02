from math import ceil

class Solution(object):
    def soupServings(self, n):
        if n > 4800:
            return 1.0
        
        N = int(ceil(n / 25.0))
        memo = {}
        
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            key = (a, b)
            if key in memo:
                return memo[key]
            
            p1 = dp(a - 4, b)
            p2 = dp(a - 3, b - 1)
            p3 = dp(a - 2, b - 2)
            p4 = dp(a - 1, b - 3)
            result = 0.25 * (p1 + p2 + p3 + p4)
            
            memo[key] = result
            return result
        
        return dp(N, N)