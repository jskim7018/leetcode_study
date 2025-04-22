from collections import deque

Q = int(input())

line = deque()
for q in range(Q):
    input_ = input().split()

    if int(input_[0]) == 2:
        print(line.popleft())
    elif int(input_[0]) == 1:
        line.append(int(input_[1]))


