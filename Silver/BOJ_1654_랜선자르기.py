
K, N = map(int, input().split())
lope = [int(input()) for _ in range(K)]
start = 1
end = max(lope)


while start <= end:
    cnt = 0
    mid = (start+end) // 2
    for i in lope:
        cnt += i // mid
    if cnt < N:
        end = mid - 1
    elif cnt >= N:
        start = mid + 1

print(end)
