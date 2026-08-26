class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        max_area = 0.0
        n = len(points)
        for i in range(n):
            Ax, Ay = points[i]
            for j in range(i + 1, n):
                Bx, By = points[j]
                for k in range(j + 1, n):
                    Cx, Cy = points[k]
                    current_area = 0.5 * abs(Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
                    if current_area > max_area:
                        max_area = current_area
                        
        return max_area