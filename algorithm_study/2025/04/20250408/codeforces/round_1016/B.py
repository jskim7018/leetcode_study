N = int(input())

for _ in range(N):
    num = int(input())
    num = str(num)
    bef_len = len(num)
    num = num.rstrip('0')
    aft_len = len(num)
    ans = bef_len - aft_len
    for i in range(aft_len - 1):
        if num[i] != '0':
            ans += 1
    print(ans)