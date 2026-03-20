from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
                                rightChild: List[int]) -> bool:
        # two-pass는 쉬움. root 찾고 dfs.
        # one-pass는
        # => 부모가 둘이상이면 안됨, 싸이클이 있어서는 안됨, 뒤 조건 만족하면서 root가 1개면 됨.

        visited = [False] * n
        parent_found = [False] * n
        no_parent_cnt = n
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            curr_st = set()
            stck = [i]
            while stck:
                curr = stck.pop()
                curr_st.add(curr)
                left = leftChild[curr]
                right = rightChild[curr]

                check = []
                if left != -1:
                    check.append(left)
                if right != -1:
                    check.append(right)

                for chk in check:
                    if left in curr_st:  # cycle
                        return False
                    if parent_found[chk]:  # more than 1 parent
                        return False
                    parent_found[chk] = True
                    no_parent_cnt -= 1

                    if not visited[chk]:
                        visited[chk] = True
                        stck.append(chk)

        if no_parent_cnt == 1:
            return True

        return False
