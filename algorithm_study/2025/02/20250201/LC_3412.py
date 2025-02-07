class Solution:
    def calculateScore(self, s: str) -> int:
        total_score = 0
        n = len(s)

        def get_mirror(c):
            return chr(ord('z')-ord(c) + ord('a'))

        mp = dict()
        for i in range(n):
            mirror = get_mirror(s[i])
            if mirror in mp:
                j = mp[mirror].pop()
                total_score += i-j
                if len(mp[mirror]) == 0:
                    del mp[mirror]
            else:
                if s[i] in mp:
                    mp[s[i]].append(i)
                else:
                    mp[s[i]] = [i]

        return total_score
