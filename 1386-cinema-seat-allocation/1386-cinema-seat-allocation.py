class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}

        # Store reserved seats as a bitmask for each affected row
        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # Masks for the three possible blocks
        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        ans = (n - len(rows)) * 2

        for mask in rows.values():

            # Both left and right groups can sit
            if (mask & left) == 0 and (mask & right) == 0:
                ans += 2

            # Otherwise, if either one is possible
            elif (mask & left) == 0 or (mask & middle) == 0 or (mask & right) == 0:
                ans += 1

        return ans