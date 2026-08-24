class Solution(object):
    def dominantIndex(self, nums):
        largest = max(nums)
        index = nums.index(largest)

        second_largest = -1

        for num in nums:
            if num != largest:
                second_largest = max(second_largest, num)

        if largest >= 2 * second_largest:
            return index

        return - 1            
       
        