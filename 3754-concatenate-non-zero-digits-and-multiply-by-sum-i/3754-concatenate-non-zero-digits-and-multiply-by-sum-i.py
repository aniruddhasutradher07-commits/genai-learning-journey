class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = str(n)

        x = ""
        total = 0

        for digit in digits:
            if digit != '0':
                x += digit
                total += int(digit)

        if x == "":
            return 0

        x = int(x)

        return x * total