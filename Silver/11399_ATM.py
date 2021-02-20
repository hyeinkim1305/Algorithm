

N = int(input())
P = list(map(int, input().split()))

# 선택정렬
for i in range(len(P)-1):
    min_idx = i
    for j in range(i+1, len(P)):
        if P[min_idx] > P[j]:
            min_idx = j
    P[min_idx], P[i] = P[i], P[min_idx]

ans = 0
for i in range(len(P)):
    Psum = 0
    for j in range(i+1):
        Psum += P[j]
    ans += Psum

print(ans)
