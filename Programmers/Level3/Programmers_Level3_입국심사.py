
'''
n을 기준으로 푼다고 생각할 수 있지만 이거는 시간을 먼저 정하고, 해당하는 사람들의 수를 보는 것!
한명씩 처리하는 것은 복잡할 수 있음!
'''
def solution(n, times):
    min_result = min(times) * n

    l = 1
    r = min(times) * n              # 시간이 적게 걸리는 심사대에서 모두가 심사받는 경우

    while l <= r:
        mid = (l+r) // 2

        num = n
        for i in times:         # 정해준 시간에서 각 심사대 시간을 나눠서 처리가능한 사람 수를 구함
            num = num - mid // i

            # 시간이 남는다는 의미
            if num < 0:
                r = mid - 1
                break           # while문 다시 시작
        # 시간이 부족하다는 의미
        if num > 0:
            l = mid + 1
        elif mid < min_result:          # 지금까지 최소값보다 작으면
                min_result = mid
                r = mid - 1

    return min_result

n = 6
times = [7, 10]
print(solution(n, times))



