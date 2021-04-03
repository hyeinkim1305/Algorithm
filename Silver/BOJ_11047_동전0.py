
N, K = map(int, input().split())
value = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N-1, -1, -1):
    if K == 0:
        break
    if value[i] > K:
        continue
    else:
        cnt += K // value[i]
        K = K % value[i]

print(cnt)