class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        has_odd = False

        for count in freq.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True
        return length + 1 if has_odd else length        