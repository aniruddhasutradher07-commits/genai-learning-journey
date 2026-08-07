class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def maxReduction(t: int, T: int) -> int:
            if T <= 0:
                return 0
            lo, hi = 0, 200000 
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if t * mid * (mid + 1) // 2 <= T:
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        def feasible(T: int) -> bool:
            total = 0
            for t in workerTimes:
                total += maxReduction(t, T)
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        lo, hi = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo