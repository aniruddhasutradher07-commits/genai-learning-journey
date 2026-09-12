class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num

        count = 0

        def dfs(i, current_or):
            nonlocal count

            if i == len(nums):
                if current_or == max_or:
                    count += 1
                return

            dfs(i + 1, current_or)

            dfs(i + 1, current_or | nums[i])

        dfs(0, 0)
        return count                   