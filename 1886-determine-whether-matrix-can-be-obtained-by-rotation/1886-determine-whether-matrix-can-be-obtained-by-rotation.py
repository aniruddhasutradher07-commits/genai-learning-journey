class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)

            return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]

        current = mat
        for _ in range(4):
            if current == target:
                return True
            current = rotate(current)

        return False            