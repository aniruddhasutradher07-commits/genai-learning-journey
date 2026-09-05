class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        squares = []
        ans = []
        max_height = 0

        for left, size in positions:
            right = left + size
            base_height = 0

            for l, r, h in squares:
                if left < r and right > l:
                    base_height = max(base_height, h)

            height = base_height + size
            squares.append((left, right, height))

            max_height = max(max_height, height)
            ans.append(max_height)

        return ans