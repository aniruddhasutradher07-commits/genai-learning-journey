class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        answer = []

        for cx, cy, r in queries:
            count = 0

            for px, py in points:
                dx = px - cx
                dy = py - cy

                if dx * dx + dy * dy <= r * r:
                    count += 1

            answer.append(count)

        return answer            