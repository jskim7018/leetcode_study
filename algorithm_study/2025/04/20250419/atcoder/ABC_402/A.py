import string

S = input()

ans = []
for c in S:
    if c in string.ascii_uppercase:
        ans.append(c)

print(''.join(ans))