T = int(input())

for _ in range(T):
    p = input()
    s = input()

    curr = p[0]
    cnt = 0
    p_cnts = []
    for i in range(len(p)):
        if p[i] == curr:
            cnt += 1
        else:
            p_cnts.append((curr, cnt))
            curr = p[i]
            cnt = 1
        if i == len(p) - 1:
            p_cnts.append((curr, cnt))
    curr = s[0]
    cnt = 0
    s_cnts = []
    for i in range(len(s)):
        if s[i] == curr:
            cnt += 1
        else:
            s_cnts.append((curr, cnt))
            curr = s[i]
            cnt = 1
        if i == len(s) - 1:
            s_cnts.append((curr, cnt))

    if len(s_cnts) != len(p_cnts):
        print("NO")
    else:
        is_possible = True
        for i in range(len(s_cnts)):
            if p_cnts[i][0] != s_cnts[i][0] or s_cnts[i][1] > p_cnts[i][1]*2 or s_cnts[i][1] < p_cnts[i][1]:
                is_possible = False
                break
        if is_possible:
            print("YES")
        else:
            print("NO")