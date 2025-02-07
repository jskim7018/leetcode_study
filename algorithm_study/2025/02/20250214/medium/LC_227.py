class Solution:
    def calculate(self, s: str) -> int:

        def calc(exp: str)->int:
            exp = exp.strip()
            exps = exp.split("+")

            if len(exps) >= 2:
                ret = calc(exps[0])
                for exp in exps[1:]:
                    ret += calc(exp)
                return ret
            exps = exp.split("-")
            if len(exps) >= 2:
                ret = calc(exps[0])
                for exp in exps[1:]:
                    ret -= calc(exp)
                return ret

            i = len(exp)-1
            while i:
                if exp[i] == '/':
                    ret = calc(exp[:i]) // calc(exp[i+1:])
                    return ret
                elif exp[i] == '*':
                    ret = calc(exp[:i]) * calc(exp[i+1:])
                    return ret
                i-=1
            return int(exp)
        return calc(s)
