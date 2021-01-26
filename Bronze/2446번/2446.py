
num = int(input())

for i in range(num):
    n = 2 * (num-i-1) + 1
    print(" " * (i) + "*" * n)

for i in range(1,num):
    n = 2 * (i) + 1
    print(" " * (num-i-1) + "*" * n)


# 여기서 계속 오류가 생긴 이유는 별 뒤에 공백이 없어야 하기 때문!
num = int(input())

for i in range(num):
    n = 2 * (num-i-1) + 1
    print(" " * (i) + "*" * n + " " * (i))


for i in range(1,num):
    n = 2 * (i) + 1
    print(" " * (num-i-1) + "*" * n + " " * (num-i-1))

