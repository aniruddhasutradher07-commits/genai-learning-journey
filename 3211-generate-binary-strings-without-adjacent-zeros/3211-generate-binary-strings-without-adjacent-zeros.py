class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def backtrack(s):
            if len(s) == n:
                ans.append(s)
                return
            backtrack(s + "1")
            if not s or s[-1] == "1":
                backtrack(s + "0")

        backtrack("")

        return ans