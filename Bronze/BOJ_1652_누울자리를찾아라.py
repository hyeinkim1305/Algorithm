
N = int(input())

room = [list(input()) for _ in range(N)]
ans_r = 0
ans_c = 0
cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        elif room[i][j] == 'X':
            if cnt >= 2:
                ans_r += 1
            cnt = 0
    if cnt >=2:
        ans_r += 1


for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        elif room[j][i] == 'X':
            if cnt >= 2:
                ans_c += 1
            cnt = 0
    if cnt >=2:
        ans_c += 1

print(ans_r, ans_c)