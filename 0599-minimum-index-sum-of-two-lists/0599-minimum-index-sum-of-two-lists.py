from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {name: i for i, name in enumerate(list1)}

        min_sum = float('inf')
        result = []

        for j, name in enumerate(list2):
            if name in index1:
                total = index1[name] + j
                if total < min_sum:
                    min_sum = total
                    result = [name]
                elif total == min_sum:
                    result.append(name)

        return result                
        