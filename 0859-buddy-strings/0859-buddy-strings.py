class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) == 2:
            i = diff[0]
            j = diff[1]

            return s[i] == goal[j] and s[j] == goal[i]
        if len(diff) == 0:
            return len(set(s)) < len(s)

        return False