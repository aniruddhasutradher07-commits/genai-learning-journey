class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n -1))
        if k > total:
            return ""
        k -= 1
        result = []
        letters = ['a','b','c']

        block_size = 2 ** (n - 1)
        first_idx = k // block_size
        result.append(letters[first_idx])
        k %= block_size

        for _ in range(n -1):
            block_size //= 2
            choice_idx = k // block_size
            k %= block_size

            prev = result[-1]
            options = [c for c in letters if c != prev]
            result.append(options[choice_idx])

        return ''.join(result) 