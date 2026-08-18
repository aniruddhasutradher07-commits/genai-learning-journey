class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}
        for s in range(n - k + 1):
            for x in set(nums[s:s+k]):
                count[x] = count.get(x, 0) + 1

        ans = -1
        for x, c in count.items():
            if c == 1:
                ans = max(ans, x)
        return ans                