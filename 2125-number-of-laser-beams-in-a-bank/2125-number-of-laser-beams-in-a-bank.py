class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        prev = 0

        for row in bank:
            devices = row.count('1')

            if devices == 0:
                continue

            ans += prev * devices
            prev = devices

        return ans        