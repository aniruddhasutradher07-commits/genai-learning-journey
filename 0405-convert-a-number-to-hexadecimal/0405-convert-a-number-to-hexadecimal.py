class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_digits = "0123456789abcdef"
        num &= 0xFFFFFFFF

        result = []
        while num != 0:
            digit = num & 15
            result.append(hex_digits[digit])
            num >>= 4
        return "".join(reversed(result))    

