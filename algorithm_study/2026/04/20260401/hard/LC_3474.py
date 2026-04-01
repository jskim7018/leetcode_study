class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # 1. LPS
        # 2. F 들에 제일 작은 것들을 어떻게 넣을지가 중요

        n = len(str1)
        m = len(str2)

        def z_algorithm(s: str) -> list[int]:
            n = len(s)
            z = [0] * n
            z[0] = n

            l, r = 0, 0

            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])

                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1

            return z

        z_array = z_algorithm(str2)

        ans = []
        can_change = [False] * n
        for i, ch in enumerate(str1):
            curr_used_len = len(ans) - i
            if ch == 'T':
                if 0 < curr_used_len != z_array[-curr_used_len]:
                    return ""
                for e in str2[curr_used_len:]:
                    ans.append(e)
            else:
                if curr_used_len == 0:
                    ans.append('a')
                    can_change[len(ans)-1] = True

        while len(ans) < n+m-1:
            ans.append('a')

        # Check/Fix all F. Can do O(n*m) since m is only 500
        for i in range(n):
            if str1[i] != 'F':
                continue

            last_f_idx = -1
            is_same = True
            for j in range(m):
                if ans[i+j] != str2[j]:
                    is_same = False
                    break
                elif str1[i+j] == 'F' and can_change[i+j]:
                    last_f_idx = i+j
            if is_same:
                if last_f_idx >= 0 and can_change[last_f_idx]:
                    ans[last_f_idx] = 'b'
                else:
                    return ""

        return ''.join(ans)
