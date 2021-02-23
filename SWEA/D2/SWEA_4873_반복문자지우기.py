'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
'''

T = int(input())
for tc in range(1, T+1):
    stack = []
    word = input()

    for w in word:
        if len(stack) == 0:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop(-1)
            else:
                stack.append(w)
    if len(stack) != 0:
        print('#{} {}'.format(tc, len(stack)))
    else:
        print('#{} {}'.format(tc, 0))