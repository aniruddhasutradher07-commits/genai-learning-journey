class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False            