from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def count_multiples(x):
            total = 0
            for r in range(1, n + 1):
                for combo in combinations(coins, r):
                    l = 1
                    for c in combo:
                        l = lcm(l, c)
                        if l > x:
                            break
                    if l <= x:
                        cnt = x // l
                        if r % 2 == 1:
                            total += cnt
                        else:
                            total -= cnt
            return total
        
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_multiples(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
        