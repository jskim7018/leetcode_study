class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        used = set()

        stack = list()
        for i, ch in enumerate(s):
            if locked[i] == '1':
                if ch == '(':
                    stack.append(i)
                else:
                    if stack:
                        used.add(stack.pop())
                        used.add(i)

        unlocked_cnt = 0
        locked_left_cnt = 0

        for i, ch in enumerate(s):
            if i not in used:
                if locked[i] == '0':
                    if locked_left_cnt > 0:
                        locked_left_cnt -= 1
                    else:
                        unlocked_cnt += 1
                else:
                    if s[i] == ')':
                        if unlocked_cnt > 0:
                            unlocked_cnt -= 1
                        else:
                            return False
                    else:
                        locked_left_cnt += 1

        if locked_left_cnt == 0 and unlocked_cnt % 2 == 0:
            return True
        else:
            return False
