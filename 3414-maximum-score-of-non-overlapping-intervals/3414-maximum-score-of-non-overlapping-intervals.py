from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]
        arr.sort()

        starts = [x[0] for x in arr]
        nxt = [0] * n

        for i in range(n):
            r = arr[i][1]
            nxt[i] = bisect_right(starts, r)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):

            for k in range(1, 5):
                skip = dp[i + 1][k]
                next_i = nxt[i]

                take_score = arr[i][2] + dp[next_i][k - 1][0]

                take_indices = (
                    arr[i][3],
                ) + dp[next_i][k - 1][1]
                take_indices = tuple(sorted(take_indices))

                take = (take_score, take_indices)

                dp[i][k] = better(skip, take)

        return list(dp[0][4][1])