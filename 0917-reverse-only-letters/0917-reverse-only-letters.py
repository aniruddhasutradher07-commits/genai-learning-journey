class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s) - 1

        def isLetter(c):
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

        while left < right:
            if not isLetter(s[left]):
                left += 1
            elif not isLetter(s[right]):
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)                    