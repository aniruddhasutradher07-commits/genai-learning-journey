class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                result.append(self.formatRange(start, nums[i-1]))
                start = nums[i]
        result.append(self.formatRange(start, nums[-1]))
        
        return result
    
    def formatRange(self, a, b):
        if a == b:
            return str(a)
        return f"{a}->{b}"