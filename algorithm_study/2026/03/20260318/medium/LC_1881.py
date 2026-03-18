class Solution:
    def maxValue(self, n: str, x: int) -> str:
        ans = []

        is_neg = n[0] == '-'

        start = 0
        if is_neg:
            ans.append(n[0])
            start = 1

        x = str(x)
        for i in range(start, len(n)):
            digit = n[i]
            if is_neg:
                if x < digit:
                    ans.append(x)
                    ans.append(n[i:])
                    return ''.join(ans)
            else:
                if x > digit:
                    ans.append(x)
                    ans.append(n[i:])
                    return ''.join(ans)
            ans.append(digit)

        ans.append(x)
        return ''.join(ans)
