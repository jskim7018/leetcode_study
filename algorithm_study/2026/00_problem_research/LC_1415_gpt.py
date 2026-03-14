class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        res = []
        prev = ""

        for i in range(n):
            for c in "abc":
                if c == prev:
                    continue

                count = 1 << (n - i - 1)

                if k > count:
                    k -= count
                else:
                    res.append(c)
                    prev = c
                    break

        return "".join(res)