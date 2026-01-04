from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits.append(-1) # sentinel
        n = len(fruits)
        fruits_accum = []

        curr_fruit = fruits[0]
        cnt = 1
        for i in range(1, n):
            fruit = fruits[i]
            if fruit == curr_fruit:
                cnt += 1
            else:
                fruits_accum.append((curr_fruit, cnt))
                cnt = 1
                curr_fruit = fruit

        st = set()
        ans = 0
        tmp = 0
        for i in range(len(fruits_accum)):
            if len(st) == 2 and fruits_accum[i][0] not in st:
                st.clear()
                st.update([fruits_accum[i-1][0], fruits_accum[i][0]])
                tmp = fruits_accum[i-1][1] + fruits_accum[i][1]
            else:
                st.add(fruits_accum[i][0])
                tmp += fruits_accum[i][1]

            ans = max(ans, tmp)

        return ans
