class Solution:
    def bitwiseComplement(self, n):
        if n == 0:
            return 1


        bit_length = n.bit_length()

        all_ones = (1 << bit_length) - 1

        return all_ones - n    