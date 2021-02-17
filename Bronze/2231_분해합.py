
# 자연수 M의 분해합이 N인 경우, M을 N의 생성자
def sep_sum(n):
    sep = 0
    sep += n
    while n != 0:
        sep += n % 10
        n //= 10

    return sep

N = int(input())
output = 0
for n in range(1, N):
    if sep_sum(n) == N:
        output = n
        break

if output > 0:
    print(output)
else:
    print(0)