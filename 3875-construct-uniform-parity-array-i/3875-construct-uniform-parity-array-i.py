class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = sum(num % 2 for num in nums1)
        even = len(nums1) - odd

        if odd == 0 or even == 0:
            return True

        return True    