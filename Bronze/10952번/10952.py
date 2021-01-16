sum = 2
while sum > 0:
    a,b = map(int,input().split(' '))
    sum = a + b
    print(sum)

while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
# break로 반복문 탈출하는거 유념!
# 둘 코드의 차이는 위에는 입력을 0 0 했을 때 0이 나오고 아래는 입력 0 0 했을 때 아무것도 안나오고 반복문이 탈출된다. 따라서 이 문제는 조건이 입력 0 0 했을 때 아무것도 안나오므로 아래의 코드가 맞다!