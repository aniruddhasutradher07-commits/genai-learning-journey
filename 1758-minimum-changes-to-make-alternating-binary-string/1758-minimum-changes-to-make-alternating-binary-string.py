class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count0 = 0
        i = 0
        while i < n:
            if i % 2 == 0:
                expected = '0'
            else:
                expected = '1'
            if s[i] != expected:
                count0 += 1
            i += 1
        count1 = n - count0
        if count0 < count1:
            return count0
        else:
            return count1