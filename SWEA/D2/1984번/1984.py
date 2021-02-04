# remove는 원본 변형

T = int(input())
for i in range(T):
  test = list(map(int,input().split()))
  test.remove(max(test))
  test.remove(min(test))

  result = round(sum(test) / len(test))

  print('#{} {}'.format(i+1, result))

