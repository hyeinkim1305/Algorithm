



N = int(input())
q = [i for i in range(1, N+1)]
front = 0       # 남은 카드들 중 멘 앞에 숫자
if len(q) == 1 or len(q) == 2:      # 1이랑 2일때는 별도로 해줘야 런타임 에러 안 생김
    print(q[-1])
else:
    while True:
        front += 1      # 1. 가장 앞에 있는 숫자 버린다.
        if front + 1 == len(q):
            break
        q.append(q[front])      # 2. 앞에 있는 숫자를 뒤로 옮긴다
        front += 1
        if front + 1 == len(q):
            break
    print(q[front])