n = int(input())
for i in range(n):
    m = list(map(int,input().split()))
    s = m[0] // m[1]
    ss = m[0] % m[1]
    print('#{} {} {}'.format(i+1,s,ss))