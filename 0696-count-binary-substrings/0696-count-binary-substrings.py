class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        previous = 0
        current = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                result += min(previous, current)
                previous = current
                current = 1

        result += min(previous, current)

        return result            