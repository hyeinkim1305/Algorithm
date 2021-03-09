
# 시간 초과로 pop은 안쓰고, 큐의 가장 앞 원소의 인덱스를 front로 지정함
import sys
input = sys.stdin.readline

N = int(input())
q = []
front = 0
for i in range(N):
    M = input().split()
    if M[0] == 'push':
        q.append(int(M[1]))
    elif M[0] == 'pop':
        if front >= len(q):     # 이부분 주의
            print(-1)
        else:
            print(q[front])
            front += 1
    elif M[0] == 'size':
        print(len(q)-front)
    elif M[0] == 'empty':
        if front >= len(q):
            print(1)
            front = 0
            q = []
        else:
            print(0)
    elif M[0] == 'front':
        if front >= len(q):
            print(-1)
        else:
            print(q[front])
    elif M[0] == 'back':
        if front >= len(q):
            print(-1)
        else:
            print(q[-1])


