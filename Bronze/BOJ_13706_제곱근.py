
# 이분탐색
def find(start, end, N):
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 == N:
            return mid
        elif mid ** 2 < N:
            start = mid + 1
        elif mid ** 2 > N:
            end = mid - 1

N = int(input())

print(find(0, N, N))




