'''
그 사이에 있는 문자열은 균형이 어떻게?
'''

def test(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                return 'no'
            else:
                if stack.pop(-1) != '(':
                    return 'no'
        elif s[i] == ']':
            if len(stack) == 0:
                return 'no'
            else:
                if stack.pop(-1) != '[':
                    return 'no'
    if len(stack) != 0:
        return 'no'
    else:
        return 'yes'

words = []
while True:
    word = input()
    if word == '.':
        break
    words.append(word)

for i in range(len(words)):
    print(test(words[i]))
