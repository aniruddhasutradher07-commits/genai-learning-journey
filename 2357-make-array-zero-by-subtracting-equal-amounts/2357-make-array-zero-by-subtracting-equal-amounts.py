class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct_nonzero = set(x for x in nums if x != 0)
        return len(distinct_nonzero)