class Solution(object):
    def sortArrayByParityII(self, nums):
        result = [0] * len(nums)

        even = 0
        odd = 1

        for num in nums:
            if num % 2 == 0:
                result[even] = num
                even += 2
            else:
                result[odd] = num
                odd += 2

        return result        
