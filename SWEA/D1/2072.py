# 반복하기 전에 result 초기화 해야하는 거 잊지 말기

n =int(input())
count = 0
for i in range(n):
    result = 0
    count += 1
    m = map(int,input().split())
    for j in m:
        if j % 2 == 1:
            result += j 
    print('#{} {}'.format(count,result))