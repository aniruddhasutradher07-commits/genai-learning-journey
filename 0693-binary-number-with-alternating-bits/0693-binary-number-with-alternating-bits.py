class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        previous = n & 1
        n >>= 1

        while n > 0:
            current = n & 1

            if current == previous:
                return False

            previous = current
            n >>= 1

        return True        