class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        A = sum(aliceSizes)
        B = sum(bobSizes)

        diff = (B -A) // 2

        bob = set(bobSizes)

        for a in aliceSizes:
            b = a + diff

            if b in bob:
                return [a, b]

        