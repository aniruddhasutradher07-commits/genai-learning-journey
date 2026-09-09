class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        greater = []

        for x in nums:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return smaller + equal + greater            
