
M = int(input())
N = int(input())
# 소수들 합
sum_n = 0
# 최소값 소수 초기화
min_n = 10000001

for n in range(M, N+1):
    cnt = 0
    if n == 2 or n == 3:
        sum_n += n
        if min_n > n:
            min_n = n

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            cnt = 0
            break
        else:
            cnt += 1

    if cnt > 0:
        sum_n += n
        if min_n > n:
            min_n = n

if sum_n > 0:
    print(sum_n, min_n, sep="\n")
else:
    print(-1)