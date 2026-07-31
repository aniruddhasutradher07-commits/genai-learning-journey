class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sub , k):
            sub[:k] = sub[:k][::-1]

        n = len(arr)
        result = []

        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))

            if max_idx == size -1:
                continue

            if max_idx != 0:
                flip(arr, max_idx +1)
                result.append(max_idx + 1)

            flip(arr, size)
            result.append(size)

        return result                   