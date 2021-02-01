n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

ans = 0
for i in range(n):
  ans += min(a_list) * max(b_list)
  a_list.remove(min(a_list))
  b_list.remove(max(b_list))

print(ans)


