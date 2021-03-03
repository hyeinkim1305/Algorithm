'''
1
10 6 12 8 9 4 1 3
'''

def code(queue):
    while True:
        for k in range(1, 5+1):
            last = queue.pop(0)-k
            if last <= 0:
                last = 0
                queue.append(last)
                return queue
            queue.append(last)

T = 10
for tc in range(1, T+1):
    N = int(input())
    Queue = list(map(int, input().split()))
    ans = code(Queue)
    print(f'#{tc}', end=' ')
    for i in ans:
        print(i, end=' ')

    # 출력형식 다음과 같이도 가능
    # print(f'#{N} {" ".join(map(str, password(arr)))}')
    # print(*ans)



