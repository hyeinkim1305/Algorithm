
n = int(input())
stack = []
ans = []
cnt = 1
output = True
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        output = False
        break

if output == False:
    print('NO')
else:
    for j in ans:
        print(j)

