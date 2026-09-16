class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i - t.index(char)) for i, char in enumerate(s))