class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        lo, hi = 2, num // 2

        while lo <= hi:
            mid = (lo + hi) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False                    