n = int(input())
num_list = []
number = list(map(int,input().split()))

for num in number:
  if num == 1:
    continue
  else:
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      num_list.append(num)

print(len(num_list))
