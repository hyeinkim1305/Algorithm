
# 안풀리면 다른 방법 생각해보기

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * 401

    for i in range(len(pos)):
        for j in range(2):
            if pos[i][0] < pos[i][1]:
                minpos = pos[i][0]
                maxpos = pos[i][1]
            else:
                minpos = pos[i][1]
                maxpos = pos[i][0]
        if minpos % 2 == 0:
            minpos -= 1
        if maxpos % 2 == 1:
            maxpos += 1
        for k in range(minpos, maxpos+1):
            cnt[k] += 1
    print('#{} {}'.format(tc, max(cnt)))


'''
틀린 풀이 / 처음 접근이 잘못 되었음
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]
    # pos = [[10, 20],[30, 40],[50, 60],[70, 80]]
    # pos = [[10,100],[20,80],[30,50]]
    # ans = [[0]]
    max_cnt = 1
    for i in range(len(pos)):
        cnt = 1

        for j in range(len(pos)):
            if j == i:
                continue
            if (pos[i][0] > pos[j][0] and pos[i][0] < pos[j][1]) or (pos[i][1] > pos[j][0] and pos[i][1] < pos[j][1]):
                cnt += 1
                continue
            if (pos[i][0] < pos[j][0] and pos[i][1] > pos[j][1]) or (pos[i][0] > pos[j][1] and pos[i][1] < pos[j][0]):
                continue
            if abs(pos[i][0] - pos[j][0]) == 1 or abs(pos[i][0] - pos[j][1]) == 1:
                cnt += 1
                continue
            if abs(pos[i][1] - pos[j][0]) == 1 or abs(pos[i][1] - pos[j][1]) == 1:
                cnt += 1
                continue

        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))
'''

