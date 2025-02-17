class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        sequence = []
        def solve(used, cnt, size) -> int:
            nonlocal sequence
            if cnt == size and used:
                return 1
            if cnt == size:
                return 0
            letter_used = set()
            ret = 0
            for i in range(n):
                if i not in used and tiles[i] not in letter_used:
                    letter_used.add(tiles[i])
                    used.add(i)
                    sequence.append(tiles[i])
                    ret += solve(used, cnt + 1, size)
                    used.remove(i)
                    sequence.pop()
            return ret
        ans = 0
        for i in range(1, n+1):
            used = set()
            ans += solve(used, 0, i)

        return ans
