import math

N, K = map(int, input().split())
S = input()

s_list = list(S)

for i in range(N):
    if s_list[i] == 'o':
        if i-1 >= 0 and s_list[i-1] == '?':
            s_list[i-1] = '.'
        if i+1 < N and s_list[i+1] == '?':
            s_list[i+1] = '.'

cnt_question = 0
cnt_o = 0

in_cnt_o = False
tmp = []
for i in range(N):
    if s_list[i] == '?':
        cnt_question += 1
        if i == N-1:
            if cnt_question > 0:
                tmp.append(cnt_question)
                cnt_question = 0
    elif s_list[i] == 'o':
        cnt_o += 1
        if cnt_question > 0:
            tmp.append(cnt_question)
            cnt_question = 0
    elif s_list[i] == '.':
        if cnt_question > 0:
            tmp.append(cnt_question)
            cnt_question = 0

need_o = K - cnt_o
rest_what = ''

tmp_need_o = need_o
rest_what_possible = False
for t in tmp:
    can_put = math.ceil(t/2)
    if can_put <= tmp_need_o:
        tmp_need_o -= can_put
    else:
        rest_what_possible = True
        break

if not rest_what_possible:
    idx_tmp = 0
    i = 0
    while i < N:
        if s_list[i] == '?':
            if tmp[idx_tmp] % 2 == 0:
                i += tmp[idx_tmp]
            else:
                is_o = True
                while i < N and s_list[i] == '?':
                    if is_o:
                        s_list[i] = 'o'
                        is_o = False
                    else:
                        s_list[i] = '.'
                        is_o = True
                    i += 1
            idx_tmp += 1
        else:
            i += 1

else:
    if need_o == 0:
        rest_what = '.'
    elif cnt_question == need_o:
        rest_what = 'o'
    else:
        rest_what = '?'

    for i in range(N):
        if s_list[i] == '?':
            s_list[i] = rest_what
print(''.join(s_list))