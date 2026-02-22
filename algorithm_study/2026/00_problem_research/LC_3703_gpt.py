class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []  # each element = [char, count]

        for ch in s:
            # build run-length stack
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

            # only possible to remove if last char is ')'
            if len(stack) >= 2 and stack[-1][0] == ')':
                # if we have k consecutive ')'
                if stack[-1][1] >= k:
                    # and previous run is '(' with at least k
                    if stack[-2][0] == '(' and stack[-2][1] >= k:

                        # remove k from both runs
                        stack[-1][1] -= k
                        stack[-2][1] -= k

                        # remove empty runs
                        if stack[-1][1] == 0:
                            stack.pop()
                        if stack and stack[-1][1] == 0:
                            stack.pop()

        # rebuild final string
        result = []
        for ch, count in stack:
            result.append(ch * count)

        return ''.join(result)