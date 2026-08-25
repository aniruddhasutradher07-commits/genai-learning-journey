from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        
        total_sum = sum(nums)
        current_sum = 0
        subsequence = []
        
        for num in nums:
            current_sum += num
            subsequence.append(num)
            if current_sum > (total_sum - current_sum):
                break
                
        return subsequence