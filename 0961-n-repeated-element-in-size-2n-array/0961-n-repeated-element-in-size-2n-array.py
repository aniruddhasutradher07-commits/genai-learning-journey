from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] > 1:
                return num
        