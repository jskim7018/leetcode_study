import sys
from collections import deque

def main():
    t = int(input())
    index = 1
    out_lines = []

    for _ in range(t):
        q = int(input())
        index += 1

        A = deque()
        m = 0
        T = 0
        S_val = 0

        for _ in range(q):
            input_ = list(map(int, input().split()))
            index += 1
            op = input_[0]
            if op == 3:
                k_val = input_[1]
                index += 1
                A.append(k_val)
                m += 1
                T += k_val
                S_val += k_val * m
                out_lines.append(str(S_val))
            elif op == 1:
                last = A.pop()
                A.appendleft(last)
                S_val = S_val + T - m * last
                out_lines.append(str(S_val))
            elif op == 2:
                A.reverse()
                S_val = (m + 1) * T - S_val
                out_lines.append(str(S_val))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
