from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = Counter()
        mp2 = Counter()

        for a in s:
            mp1[a]+=1
        for a in t:
            mp2[a]+=1

        return mp1 == mp2

# Better way to use Counter.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return collections.Counter(s) == collections.Counter(t)
