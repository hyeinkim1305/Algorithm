
word = input().split()
output = []
for w in word:
    s = ''
    for i in w:
        s = i + s
    output.append(s)

if output[0] > output[1]:
    print(output[0])
else:
    print(output[1])