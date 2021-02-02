
# round(n) 하면 소수점 첫째자리에서 반올림해서 int형으로 나옴!

n =int(input())
count = 0
for i in range(n):
    result = 0
    avg = 0
    count += 1
    m = list(map(int,input().split()))
    for j in m:
        result += j
    avg = round(result / len(m))
    print('#{} {}'.format(count,avg))
