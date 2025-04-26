from collections import defaultdict

t = int(input())

for _ in range(t):
    s = input()
    counter = defaultdict(int)

    for c in s:
        counter[c] += 1

    ans = []
    for i in range(1,11):
        for j in range(10-i, 10):
            if counter[str(j)] > 0:
                ans += str(j)
                counter[str(j)] -= 1
                break

    print(''.join(ans))
