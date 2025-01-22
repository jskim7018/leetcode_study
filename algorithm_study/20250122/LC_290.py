class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = dict()
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for idx, a in enumerate(words):
            if a in mp.keys():
                if pattern[idx] != mp[a]:
                    return False
            else:
                if pattern[idx] in mp.values():
                    return False
                mp[a] = pattern[idx]

        return True
