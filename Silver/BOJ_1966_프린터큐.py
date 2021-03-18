'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''
from collections import deque

def f(q, cnt, M):
    while q:
        if max(q) == q[0]:
            if M == 0:
                q.popleft()
                cnt += 1
                return cnt
            else:
                M -= 1
                q.popleft()
                cnt += 1        # 몇번째로 인쇄되는지 알기
        else:
            if M == 0:
                M = len(q)-1
                q.append(q[0])
                q.popleft()
            else:
                M -= 1
                q.append(q[0])
                q.popleft()




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = deque()
    prio = list(map(int, input().split()))
    for p in prio:
        q.append(p)
    cnt = 0
    print(f(q, cnt, M))



