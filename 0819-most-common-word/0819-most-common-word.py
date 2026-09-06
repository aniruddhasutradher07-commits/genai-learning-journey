import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-z]', ' ', paragraph)
        words = paragraph.split()
        banned = set(banned)
        count = Counter(word for word in words if word not in banned)
        return count.most_common(1)[0][0]