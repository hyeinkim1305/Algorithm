# 순열 !!! 순열에서 최소값 갱신 형태

def perm(idx):
    global arr_sum, arr_min  # global 안하면 arr_min이 계속 전역에서 선언한 값으로 리셋됨

    if idx == N:
        if arr_sum < arr_min:  # sum이 min보다 작으면 min은 sum으로
            arr_min = arr_sum
    else:
        if arr_sum > arr_min:  # 만약에 sum이 min보다 크면 돌아감 (가지치기)
            return
        for i in range(N):
            if check[i] == 0:
                arr_sum += arr[idx][i]   # 더한다
                check[i] = 1
                perm(idx+1)
                arr_sum -= arr[idx][i]    # 빼줘야 한다 안그러면 누적되는 듯
                check[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_sum = 0   # 합
    arr_min = N ** 3  # 최소 합
    check = [0] * N  # 방문했는지 확인
    perm(0)
    print('#{} {}'.format(tc, arr_min))
