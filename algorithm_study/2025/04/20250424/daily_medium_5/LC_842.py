from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        MAXIM = int(pow(2,31))-1
        n = len(num)

        for i in range(1,n-1):
            fib1 = num[:i]
            fib1_num = int(fib1)
            if fib1_num > MAXIM:
                break
            for j in range(i+1, n):
                fib2 = num[i:j]
                fib2_num = int(num[i:j])
                if fib2_num > MAXIM:
                    break
                arr = [fib1_num, fib2_num]
                curr_len = len(fib1) + len(fib2)
                while curr_len < n:
                    fib = arr[-1] + arr[-2]
                    if fib > MAXIM:
                        break
                    curr_len += len(str(fib))
                    arr.append(fib)
                fib_str = ''.join([str(e) for e in arr])
                if fib_str == num and len(arr) >= 3:
                    return arr
        return []
