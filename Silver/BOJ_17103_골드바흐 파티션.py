'''
에라토네스의 체로 소수를 판별하고 소수는 True로, 아닌 것은 False로 한다.
그 상태에서 각 값마다 값의 반만큼 순회하며 True로 되어있으면 경우를 +1 한다.
이때 i, n-i로 두 수의 합이 n인 경우를 미리 골라 True인지 바로 판단하여 경우의 수를 줄인다.
'''
from sys import stdin

def prime(N):       # 소수 판별
    arr = [False, False]+[True] * (N-1)     # 0, 1 + 2~
    for i in range(2, int(N**0.5)+1):
        if arr[i] == True:
            for j in range(i*2, N+1, i):
                arr[j] = False
    return arr

T = int(stdin.readline())
N_list = [int(stdin.readline()) for _ in range(T)]
arr = prime(max(N_list))


for n in N_list:
    cnt = 0
    for i in range(n//2+1):
        if (arr[i] == True) and (arr[n-i] == True):
            cnt += 1
    print(cnt)


# 소수를 리스트에 담아서 각각 더해서 경우를 구하면 시간초과가 나온다
# for k in range(T):
#     cnt = 0
#     n = len(prime_list)
#     for i in range(n):
#         for j in range(i, n):
#             if prime_list[i] + prime_list[j] == N_list[k]:
#                 cnt += 1
#     print(cnt)


