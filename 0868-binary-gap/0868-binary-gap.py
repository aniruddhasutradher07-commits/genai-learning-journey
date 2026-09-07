class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        ans = 0
        pos = 0

        while n > 0:
            if n & 1:
                if prev != -1:
                    ans = max(ans, pos - prev)

                prev = pos

            n >>= 1
            pos += 1

        return ans            