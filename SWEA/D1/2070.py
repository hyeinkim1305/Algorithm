# 시간초과 런타임에러 수정함.

n = int(input())
count = 0
for i in range(n):
    m = input().split()
    count += 1
    if int(m[0]) > int(m[1]):
        print('#{} >'.format(count))

    elif int(m[0]) < int(m[1]):
        print('#{} <'.format(count))
    else:
        print('#{} ='.format(count))