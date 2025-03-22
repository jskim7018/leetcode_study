class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        abcs = [[a,'a'], [b,'b'], [c,'c']]

        ans = []
        while True:
            abcs.sort(reverse=True)
            if len(ans) >= 2:
                if ans[-1] == abcs[0][1] and ans[-2] == abcs[0][1]:
                    if abcs[1][0] != 0:
                        ans.append(abcs[1][1])
                        abcs[1][0] -= 1
                    else:
                        break
                else:
                    if abcs[0][0] != 0:
                        ans.append(abcs[0][1])
                        abcs[0][0] -= 1
                    else:
                        break
            else:
                if abcs[0][0] != 0:
                    ans.append(abcs[0][1])
                    abcs[0][0] -= 1
                else:
                    break

        return ''.join(ans)
