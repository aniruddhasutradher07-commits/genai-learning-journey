class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = [0] * 10

        while n != 0:
            digit = n % 10
            freq[digit] += 1
            n = n // 10

        score = 0
        for d in range(10):
            score += d * freq[d]

        return score        