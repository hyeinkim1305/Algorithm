
num = set(range(1,10001))
number = set()

for i in range(1,10001):
    for j in str(i):      # 이런 방법 알아두기
        i += int(j)
    number.add(i)
ans = sorted(num - number)
for i in ans:
    print(i)

