class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_or = 0

        for num in nums:
            xor_or |= num

        return xor_or * (2 ** (len(nums) -1))    