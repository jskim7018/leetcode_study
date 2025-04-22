t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    left = 1
    right = n

    ans = []
    for c in s[::-1]:
        if c == '<':
            ans.append(left)
            left += 1
        else:
            ans.append(right)
            right -= 1
    ans.append(left)
    ans.reverse()
    for e in ans:
        print(e,end=" ")
    print()