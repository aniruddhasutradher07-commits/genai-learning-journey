class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True

        window = 0

        for i in range(1, n):
            add = i - minJump
            if add >= 0 and reachable[add]:
                window += 1

            remove = i - maxJump - 1
            if remove >= 0 and reachable[remove]:
                window -= 1

            if s[i] == '0' and window > 0:
                reachable[i] = True

        return reachable[-1]