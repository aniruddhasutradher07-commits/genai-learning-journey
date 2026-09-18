class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        for i in range(n):
            idx = ord(s[i]) - ord('a')

            if i != first[idx]:
                continue

            l = i
            r = last[idx]
            valid = True

            j = l

            while j <= r:
                c = ord(s[j]) - ord('a')

                if first[c] < l:
                    valid = False
                    break

                r = max(r, last[c])

                j += 1
            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans                               