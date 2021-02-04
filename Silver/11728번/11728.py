
n = map(int, input().split())
answer = []
a = list(map(int, input().split()))
answer.append(a)
b = list(map(int, input().split()))
answer.append(b)    

result = []
for ans in answer:
  for a in ans:
    result.append(a)
  
result = sorted(result)

result = list(map(str, result))

print(' '.join(result))




