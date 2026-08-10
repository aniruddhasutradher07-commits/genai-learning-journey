class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n * n
        sum_even = n * (n + 1)
        return gcd(sum_odd, sum_even)