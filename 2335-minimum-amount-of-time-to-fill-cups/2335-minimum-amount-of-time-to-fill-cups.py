class Solution:
    def fillCups(self, amount: List[int]) -> int:
        seconds = 0

        while sum(amount) > 0:
            amount.sort(reverse=True)
            amount[0] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            seconds += 1

        return seconds        