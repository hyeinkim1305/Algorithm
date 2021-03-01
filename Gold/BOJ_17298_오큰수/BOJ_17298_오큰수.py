
N = int(input())
n = list(map(int, input().split()))
stack = []
ans = [-1 for _ in range(N)]
for i in range(len(n)):
    while len(stack)!= 0 and n[stack[-1]] < n[i]:
        ans[stack.pop()] = n[i]
    stack.append(i)

for k in ans:
    print(k, end=' ')


'''
# 시간 초과
N = int(input())
n = list(map(int, input().split()))
ans = []

for i in range(len(n)):
    if i == len(n)-1:
        ans.append(-1)
        break
    for j in range(i+1, len(n)):
        if n[i] < n[j]:
            ans.append(n[j])
            break
    else:
        ans.append(-1)

for k in ans:
    print(k, end=' ')
'''


