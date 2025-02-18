class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)

        ans = ""
        def solve(idx, befNum, used, seq) -> bool:
            nonlocal ans

            if idx >= n:
                ans = ''.join([str(i) for i in seq])
                return True

            start = 1
            end = befNum
            if pattern[idx] == 'I':
                start = befNum + 1
                end = 10

            for i in range(start, end):
                if i not in used:
                    used.add(i)
                    seq.append(i)
                    ret = solve(idx+1, i, used, seq)
                    if ret:
                        return ret
                    seq.pop()
                    used.remove(i)

        for i in range(1, 10):
            ret = solve(0, i, {i}, [i])
            if ret:
                break
        return ans
