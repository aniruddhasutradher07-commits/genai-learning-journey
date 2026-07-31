class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            s = str(x)
            for d in set(s):
                if s.count(d) != int(d):
                    return False
            return True

        candidate = n + 1
        while not is_balanced(candidate):
            candidate += 1
        return candidate                