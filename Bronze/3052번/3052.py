
ans = []
for i in range(10):
    n = int(input())
    ans.append(n % 42)

ans = set(ans)   # set 사용

print(len(ans))  # len 이용하는거 생각 못 함