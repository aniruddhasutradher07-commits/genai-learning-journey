class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s

            for i in range(1, len(s)):
                rotated = s[i:] + s[:i]
                ans = min(ans, rotated)

            return ans

        return ''.join(sorted(s))        