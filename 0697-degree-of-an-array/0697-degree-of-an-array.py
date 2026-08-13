from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        degree = max(count.values())
        
        result = len(nums)
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                result = min(result, length)
        
        return result