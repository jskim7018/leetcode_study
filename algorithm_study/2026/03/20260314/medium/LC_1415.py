class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 모든 경우 만들다가 k번째에서 멈추면 됨. (O(k))
        chars = ['a', 'b', 'c']

        _k = 0
        curr = []
        def dfs(curr_n: int, prev: str) -> str:
            nonlocal _k
            if curr_n >= n:
                _k += 1
                if _k == k:
                    return ''.join(curr)
                else:
                    return ''

            ret = ''
            for ch in chars:
                if ch != prev:
                    curr.append(ch)
                    ret = dfs(curr_n+1, ch)
                    curr.pop()
                    if ret != '':
                        return ret
            return ret

        return dfs(0, '')
