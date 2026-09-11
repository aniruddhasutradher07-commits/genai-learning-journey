from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        result = []

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1

            result.append(k % 10)
            k //= 10

        result.reverse()

        return result        