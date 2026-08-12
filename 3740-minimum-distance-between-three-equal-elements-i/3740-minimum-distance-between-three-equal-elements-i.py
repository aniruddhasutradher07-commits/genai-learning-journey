class Solution:
    def minimumDistance(self, nums):
        positions = {}
        for idx, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(idx)
        
        min_dist = -1
        
        for num in positions:
            idxs = positions[num]
            if len(idxs) >= 3:
                for i in range(len(idxs) - 2):
                    gap = idxs[i+2] - idxs[i]
                    if min_dist == -1 or gap < min_dist:
                        min_dist = gap
        
        if min_dist == -1:
            return -1
        return 2 * min_dist