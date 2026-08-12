class Solution:
    def areSimilar(self, mat, k):
        for i, row in enumerate(mat):
            n = len(row)
            shift = k % n
            if shift == 0:
                continue
            if i % 2 == 0:
                shifted = row[shift:] + row[:shift]
            else:
                shifted = row[-shift:] + row[:-shift]
            if shifted != row:
                return False
        return True