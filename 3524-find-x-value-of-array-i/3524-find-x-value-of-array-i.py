class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            cur = [0] * k
            cur[num % k] += 1
            for r in range(k):
                cur[(r * (num % k)) % k] += dp[r]
            for r in range(k):
                ans[r] += cur[r]

            dp = cur

        return ans