class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort(key=lambda x: x[0], reverse=True)
        top_k = indexed[:k]

        top_k.sort(key=lambda x: x[1])

        return [num for num, i in top_k]