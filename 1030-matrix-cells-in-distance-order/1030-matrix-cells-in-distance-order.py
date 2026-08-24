class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        cells = []

        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                cells.append((distance, r, c))

        cells.sort()

        return [[r, c] for distance, r, c in cells]        