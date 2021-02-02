t = int(input())
for i in range(t):
    s = list(map(int,input().split()))
    max_s = s[0]
    for j in s:
        if j > max_s:
            max_s = j
    print('#{} {}'.format(i+1,max_s))


