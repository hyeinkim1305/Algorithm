T = int(input())

ss = []
for i in range(T):
    s = list(map(int, input().split()))
    ss.append(s)

result = sorted(ss, key = lambda x : (x[1], x[0]))

for res in result:
    print(res[0], res[1])

