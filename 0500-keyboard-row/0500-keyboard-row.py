from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        result = []
        for word in words:
            w_set = set(word.lower())
            for row in rows:
                if w_set <= row:
                    result.append(word)
                    break
        return result            