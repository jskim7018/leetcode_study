from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # TODO: 이 문제는 확실히 이해 해야 한다. 꼭 다시 풀어보자. monotonic stack대체 어떻게? 왜 가능?
        def binary_search(l:int, r: int, val:int) -> int:
            while l <= r:
                mid = (l + r) // 2
                if preorder[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def check_if_possible(left: int, right: int) -> [int, int, bool]:
            if left == right:
                return [preorder[left], preorder[left], True]
            elif left > right:
                return [float('inf'), float('-inf'), True]

            root = preorder[left]
            r_start = binary_search(left+1, right, root)
            l_min, l_max, l_possible = check_if_possible(left+1, r_start-1)
            r_min, r_max, r_possible = check_if_possible(r_start, right)
            possible = False
            if l_max < root < r_min and l_possible and r_possible:
                possible = True
            return [min(l_min,r_min,root), max(root, l_max, r_max), possible]

        return check_if_possible(0, len(preorder)-1)[2]
