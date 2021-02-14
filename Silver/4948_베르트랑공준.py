
def number_list(n):
    number = [True] * n
    for i in range(2, int(n**0.5)+1):
        if number[i] == True:
            for j in range(2*i, n, i):
                number[j] = False

    return [i for i in range(2, n) if number[i] == True]
# 소수만 들어있는 리스트
li = number_list(246912)

while True:
    output = 0
    N = int(input())
    if N == 0:
        break
    for k in li:
        if N < k <= N*2:
            output += 1

    print(output)


















from math import sqrt

while True:
    N = int(input())
    cnt = 0
    if N == 0:
        break

    for i in range(N+1, 2*N+1):
        if i == 1:
            continue
        elif i == 2:
            cnt += 1
            continue
        else:
            for j in range(2, int(sqrt(i)+1)):
                if i % j == 0:
                    break
            else:
                cnt += 1
    print(cnt)