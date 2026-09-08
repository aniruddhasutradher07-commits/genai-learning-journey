import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  
        large = []  

        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def prune_small():
            while small and delayed[-small[0]] > 0:
                x = -heapq.heappop(small)
                delayed[x] -= 1

        def prune_large():
            while large and delayed[large[0]] > 0:
                x = heapq.heappop(large)
                delayed[x] -= 1

        def balance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                x = -heapq.heappop(small)
                heapq.heappush(large, x)

                small_size -= 1
                large_size += 1

                prune_small()

            elif small_size < large_size:
                x = heapq.heappop(large)
                heapq.heappush(small, -x)

                large_size -= 1
                small_size += 1

                prune_large()

        def add(x):
            nonlocal small_size, large_size

            if not small or x <= -small[0]:
                heapq.heappush(small, -x)
                small_size += 1
            else:
                heapq.heappush(large, x)
                large_size += 1

            balance()

        def remove(x):
            nonlocal small_size, large_size

            delayed[x] += 1

            if x <= -small[0]:
                small_size -= 1

                if x == -small[0]:
                    prune_small()
            else:
                large_size -= 1

                if large and x == large[0]:
                    prune_large()

            balance()

        def get_median():
            prune_small()
            prune_large()

            if k % 2 == 1:
                return float(-small[0])

            return (-small[0] + large[0]) / 2.0
        for i in range(k):
            add(nums[i])

        ans = [get_median()]
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])

            ans.append(get_median())

        return ans