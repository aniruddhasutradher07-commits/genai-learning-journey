class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()

        answer = 0

        for house in houses:
            left = 0
            right = len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            distance = float('inf')

            if left < len(heaters):
                distance = min(distance, heaters[left] - house)

            if right >= 0:
                distance = min(distance, house - heaters[right])

            answer = max(answer, distance)

        return answer                        
        