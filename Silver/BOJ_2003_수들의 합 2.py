# 투포인터 알고리즘
N, M = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 0
summ = A[0]
cnt = 0

while start <= len(A)-1 and end <= len(A)-1:

    if summ < M:
        end += 1
        if end <= len(A)-1:
            summ += A[end]
    elif summ > M:
        start += 1
        if start <= len(A)-1:
            summ -= A[start-1]
    elif summ == M:
        cnt += 1
        end += 1
        if end <= len(A)-1:
            summ += A[end]

print(cnt)
