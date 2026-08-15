class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        has_nonzero = False
        for x in nums:
            total ^= x
            if x != 0:
                has_nonzero = True

        if total != 0:
            return n
        elif has_nonzero:
            return n - 1
        else:
            return 0