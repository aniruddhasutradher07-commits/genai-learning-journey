from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for a in range(1, 10):       
            for b in range(10):     
                for c in range(0, 10, 2):

                    need = [0] * 10
                    need[a] += 1
                    need[b] += 1
                    need[c] += 1

                    possible = True

                    for d in range(10):
                        if need[d] > freq[d]:
                            possible = False
                            break

                    if possible:
                        ans += 1

        return ans