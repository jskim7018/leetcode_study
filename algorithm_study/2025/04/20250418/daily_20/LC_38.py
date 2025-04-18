class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for j in range(2,n+1):
            cnt = 0
            curr = ans[0]
            ret = []
            for i in range(0, len(ans)):
                if ans[i] == curr:
                    cnt += 1
                else:
                    ret.append(str(cnt))
                    ret.append(curr)
                    curr = ans[i]
                    cnt = 1
            if cnt != 0:
                ret.append(str(cnt))
                ret.append(curr)
            ans = ''.join(ret)
        return ans
