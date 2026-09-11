from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])

        ans = 0

        for col in range(cols):
            for row in range(rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    ans += 1
                    break

        return ans            
        