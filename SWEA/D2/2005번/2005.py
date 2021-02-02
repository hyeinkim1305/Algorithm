
T = int(input())

for t in range(T):

  N = int(input())
  answer = []

  for i in range(N):
    
    if i == 0 or i == 1:
      ans = [1] * (i+1)
      answer.append(ans)
    else:
      ans = [1]
      for j in range(1, i):
        ans.append(answer[-1][j-1] + answer[-1][j])
      ans.append(1)
      answer.append(ans)
  
  
  print('#{}'.format(t+1))
  for num in answer:
    num = map(str, num)
    print(' '.join(num))

      
    