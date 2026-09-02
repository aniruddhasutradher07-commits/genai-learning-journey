class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        consecutive_late = 0

        for ch in s:
            if ch == 'A':
                absent_count += 1

                if absent_count >= 2:
                    return False

                consecutive_late = 0

            elif ch == 'L':
                consecutive_late += 1

                if consecutive_late >= 3:
                    return False

            else:
                consecutive_late = 0

        return True                        