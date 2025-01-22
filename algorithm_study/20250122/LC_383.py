from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_r = Counter(ransomNote)
        c_m = Counter(magazine)

        for k, v in c_r.items():
            if c_m[k] < v:
                return False

        return True
