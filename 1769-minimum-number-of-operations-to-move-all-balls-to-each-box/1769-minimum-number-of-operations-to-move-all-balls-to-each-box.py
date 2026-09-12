class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = []

        for i in range(n):
            operations = 0

            for j in range(n):
                if boxes[j] == '1':
                    operations += abs(i - j)

            answer.append(operations)

        return answer            