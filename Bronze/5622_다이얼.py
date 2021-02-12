
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = list(input())
output = 0
for w in word:
    for i in range(len(alpha)):
        if w in alpha[i]:
            output += i+3
            break

print(output)

