

# 팰린드롬이면서 소수
def f():
    for i in range(N, M):

        if prime[i]:        # 소수이면서
             if str(i) == str(i)[::-1]:
                 return i
    return 1003001


N = int(input())
M = 1000001

# 소수 구하기
prime = [False, False] + [True] * (M-2)
for i in range(2, int(M**0.5)+1):
    if prime[i]:
        for j in range(i*2, M, i):
            if prime[j]:
                prime[j] = False

print(f())

