
K = int(input())
num = [int(input()) for _ in range(K)]

stack = []
for i in range(len(num)):
    if num[i] != 0:
        stack.append(num[i])
    elif num[i] == 0:
        stack.pop(-1)

print(sum(stack))