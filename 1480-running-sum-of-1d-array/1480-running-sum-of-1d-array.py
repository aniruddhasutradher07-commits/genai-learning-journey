class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total

        return nums    