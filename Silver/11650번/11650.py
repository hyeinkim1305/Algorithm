n = int(input())

number = []
for i in range(n):
  m = list(map(int,input().split()))
  number.append(m)

number_s = sorted(number, key = lambda x : (x[0], x[1]))

for num in number_s:
  print(num[0], num[1])
