a = []
for i in range(9):
    n = int(input())
    a.append(n)

a_max = max(a)
a_index = a.index(a_max) + 1
print(f'{a_max}\n{a_index}')