from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                deplicate = abs(num)
            else:
                nums[idx] = -nums[idx]

        missing = -1
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1

        return [deplicate, missing]                    

        