class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indexed = sorted(range(n), key=lambda i: score[i], reverse=True)
        answer = [""] * n
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for rank, i in enumerate(indexed):
            if rank < 3:
                answer[i] = medals[rank]
            else:
                answer[i] = str(rank + 1)

        return answer            