class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        answer = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] == 2:
                answer.append(num)

        return answer        