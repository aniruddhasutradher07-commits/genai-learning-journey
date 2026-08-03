class Solution:
    def minFlips(self, s):
        n = len(s)
        s2 = s + s

        diffA = 0
        for k in range(n):
            expected = k % 2
            if int(s2[k]) != expected:
                diffA += 1

        ans = min(diffA, n - diffA)

        for i in range(1, n):
            left_pos = i - 1
            if int(s2[left_pos]) != (left_pos % 2):
                diffA -= 1

            right_pos = i + n - 1
            if int(s2[right_pos]) != (right_pos % 2):
                diffA += 1


            ans = min(ans, diffA, n - diffA)


        return ans                    