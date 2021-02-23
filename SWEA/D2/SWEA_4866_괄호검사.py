'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
'''

def words(word):
    for w in word:
        if w == '(' or w == '{':
            stack.append(w)

        if w == ')':
            if len(stack) == 0:
                return 0
            else:
                if stack[-1] == '(':
                    stack.pop(-1)
                elif stack[-1] == '{':
                    return 0
        if w == '}':
            if len(stack) == 0:
                return 0
            else:
                if stack[-1] == '{':
                    stack.pop(-1)
                elif stack[-1] == '(':
                    return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    print('#{} {}'.format(tc, words(word)))


# 헷갈린것
# li = [1,2,3,4]
# s = li.pop(-1)
# print(s)
# print(li)