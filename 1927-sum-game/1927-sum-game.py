class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        sum1 = sum2 = cnt1 = cnt2 = 0

        for i in range(half):
            if num[i] == '?':
                cnt1 += 1
            else:
                sum1 += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                sum2 += int(num[i])

        if (cnt1 + cnt2) % 2 == 1:
            return True 

        return sum1 - sum2 != (cnt2 - cnt1) * 9 // 2
                       
