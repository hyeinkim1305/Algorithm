
# 문제를 꼼꼼이 보자! 제대로 이해 안하고 풀어서 시행착오가 있었음!

def sol(idx, cnt, result):
    global min_result

    if cnt == N - 1:
        result += arr[idx][0]       # 0은 처음 시작하는 r인덱스 맞춰준 것
        if result < min_result:
            min_result = result
            return

    for j in range(1, N):
        if visited[j] == 0 and arr[idx][j] != 0:
            visited[j] = 1
            result += arr[idx][j]
            cnt += 1
            sol(j, cnt, result)     # c인덱스가 r인덱스로 된다.
            result -= arr[idx][j]
            visited[j] = 0
            cnt -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    min_result = 987654321

    sol(0, 0, 0)
    print('#{} {}'.format(tc, min_result))









'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''