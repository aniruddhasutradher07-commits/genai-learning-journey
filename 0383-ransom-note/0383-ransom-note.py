from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True            