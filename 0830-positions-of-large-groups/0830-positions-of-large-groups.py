class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)

        start = 0

        for i in range(1, n + 1):
            if i == n or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])

                start = i

        return result            