

def Rev(x):
	result = 0
	for i in range(len(str(x)), 0, -1):
		n = (x % 10) * (10 ** (i-1))
		x = x // 10
		result += n
	return result

n, m = map(int, input().split())

print(Rev(Rev(n) + Rev(m)))


