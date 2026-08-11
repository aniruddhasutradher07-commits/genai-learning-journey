class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n // 2 + 1):
            if n % length == 0:
                pattern = s[:length]
                repeat_count = n // length
                if pattern * repeat_count == s:
                    return True
        return False            