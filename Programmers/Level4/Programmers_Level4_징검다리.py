
# 좀 다르게 생각해야하는듯 @ 어려웠다
# 먼저 거리의 최솟값을 정의하고 바위를 제거했을 때 개수를 본다.
'''
바위를 먼저 제거하고, 각 바위 사이의 거리를 구해, 거리의 최솟값 중 큰 값을 찾을 것 같지만,
거꾸로 생각해서 푸는 듯 싶다
도착지점과 출발지점 사이의 이분탐색으로 거리의 최솟값을 미리 정해주고,
해당 최솟값보다 작은 최소값을 갖는 바위 사이 거리는 바위를 제거한다.
'''

def solution(distance, rocks, n):
    # mid가 바위랑 같을 때 삭제
    ans = -1
    rocks = sorted(rocks)
    l = 0                            # 시작 왼쪽
    r = distance                     # 시작 오른쪽


    while l <= r:
        mid = (l+r)//2              # 정하려는 최솟값
        idx, cnt = 0, 0              # 지금위치, 바위제거 개수
        for r in rocks:             # 바위를 돌면서 거리를 계산
            if r-idx < mid:         # 정해놓은 최솟값보다 작은 경우
                cnt += 1            # 바위제거 개수 + 1
            else:
                idx = r             # 현재 위치가 바위로!

        if cnt > n:                 # 바위가 많이 제거된 경우
            r = mid - 1             # 최소값을 줄인다
        else:                       # 바위가 덜 제거됬거나 딱 맞을 때
            if mid > ans:           # 지금까지 최솟값보다 크면 갱신
                ans = mid
            l = mid + 1
    return ans





distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
















'''

def combi(num, n):
    global temp,ans
    if n == 0:
        ans.append(temp[:])

    elif num < n:
        return
    else:
        temp[n-1] = rocks[num-1]
        combi(num-1, n-1)
        combi(num-1, n)

def sol(distance, rocks, n):
    global temp, ans

    # 제거될 바위의 위치 조합
    temp = [0] * n
    ans = []
    combi(5, n)

    # print(ans)
    # 각 조합을 돌며며
    fo i in range(len(ans)):



distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
sol(distance, rocks, n)

'''