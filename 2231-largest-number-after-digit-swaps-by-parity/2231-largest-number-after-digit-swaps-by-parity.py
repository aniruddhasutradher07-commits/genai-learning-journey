class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))

        odd_digits = sorted([d for d in digits if int(d) % 2 == 1], reverse=True)
        even_digits = sorted([d for d in digits if int(d) % 2 == 0], reverse=True)

        odd_i, even_i = 0, 0
        result = []

        for d in digits:
            if int(d) % 2 == 1:
                result.append(odd_digits[odd_i])
                odd_i += 1          # yeh line missing thi
            else:
                result.append(even_digits[even_i])
                even_i += 1
        return int("".join(result))