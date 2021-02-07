x_list = []
y_list = []

for i in range(3):
	n, m = map(int, input().split())
	x_list.append(n)
	y_list.append(m)

result = []
for x in set(x_list):
	if x_list.count(x) == 1:
		result.append(str(x))

for y in set(y_list):
	if y_list.count(y) == 1:
		result.append(str(y))

print(' '.join(result))