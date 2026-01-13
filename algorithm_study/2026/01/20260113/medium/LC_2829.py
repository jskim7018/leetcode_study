class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        _sum = 0

        cnt = 0
        i = 1
        pass_st = set()
        while cnt < n:
            if i in pass_st:
                i += 1
                continue
            _sum += i
            pass_st.add(k-i)
            cnt += 1
            i += 1

        return _sum
