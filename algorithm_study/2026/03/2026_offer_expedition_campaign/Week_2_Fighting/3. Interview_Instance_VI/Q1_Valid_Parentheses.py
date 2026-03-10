class Solution:
    def isValid(self, s: str) -> bool:
        stck = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stck.append(ch)
            else:
                if not stck:
                    return False
                if ch == ")" and stck[-1] != "(":
                    return False
                if ch == "]" and stck[-1] != "[":
                    return False
                if ch == "}" and stck[-1] != "{":
                    return False

                stck.pop()

        return not stck
