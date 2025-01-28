from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.strip()
        words = re.sub(r"[!?',;.]"," ", paragraph).lower()

        words = words.split()

        words_count = Counter(words)

        for b in banned:
            del words_count[b]

        return words_count.most_common(1)[0][0]
