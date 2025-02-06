from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i = 0
        st = set()
        while True:
            j = 0
            is_ans_exist = False
            while True:
                curr = x ** i + y ** j
                print(curr)
                if curr <= bound:
                    is_ans_exist = True
                    st.add(curr)
                else:
                    break

                if y == 1:
                    break
                j += 1
            if x ** i > bound or not is_ans_exist or x == 1:
                break
            i += 1
        return list(st)
