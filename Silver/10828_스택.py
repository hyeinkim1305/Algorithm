import sys
N = int(input())
stack = []

for i in range(N):
    orders = sys.stdin.readline().strip()

    if orders.split()[0] == 'push':
        push = orders.split()
        stack.append(int(push[1]))
    if orders == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print('-1')
    if orders == 'size':
        print(len(stack))
    if orders == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    if orders == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
