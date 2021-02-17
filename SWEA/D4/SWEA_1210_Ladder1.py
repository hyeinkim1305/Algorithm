# 주의할 점 : 사다리에서 도착점 기준으로 생각한다.
# if c-1 > -1 and arr[r][c-1] != 0: 이런 조건에서 앞에 조건을 뒤에 조건보다 나중에 쓰면 오류생긴다.
# continue 사용 잘하기 (헷갈렸었음!)

import sys
sys.stdin = open('input.txt','r')

T = 10

for tc in range(1, T+1):
    t = int(input())  # 테스트케이스
    arr = []
    for _ in range(100):
        a = list(map(int, input().split()))
        arr.append(a)
    # 2에 해당하는 것을 찾고
    for i in range(100):
        if arr[99][i] == 2:
            c = i
            r = 99
            break

    direction = '^'
    # break 생길 때까지 돌린다.
    while True:
        if r == 0:
            output = c
            break
        # 방향이 바뀌었을 때
        if direction == '<':
            if c-1 > -1 and arr[r][c-1] != 0:
                c -= 1
                continue
            if r-1 > -1 and arr[r-1][c] != 0:
                r -= 1
                direction = '^'
                continue

        if direction == '>':
            if c+1 < 100 and arr[r][c+1] != 0:   # 조건 순서 주의 (바꾸니까 돌아감) 시간 엄청 걸림 여기서 !!
                c += 1
                continue
            if r-1 > -1 and arr[r-1][c] != 0:
                r -= 1
                direction = '^'
                continue

        if c+1 < 100 and arr[r][c+1] != 0:
            c += 1
            direction = '>'
            continue
        if c-1 > -1 and arr[r][c-1] != 0:
            c -= 1
            direction = '<'
            continue
        # 위의 것들 중 아무것도 해당 안될 때
        r -= 1

    print("#{} {}".format(tc, output))