
# sol1
test_case = int(input())

for t in range(test_case):
  n = int(input())
  
  e = 0
  a = 0
  b = 0
  c = 0
  d = 0

  if n % 11 == 0:
    while n % 11 == 0:
      n = n // 11
      e += 1

  if n % 7 == 0:
    while n % 7 == 0:
      n = n // 7
      d += 1

  if n % 5 == 0:
    while n % 5 == 0:
      n = n // 5
      c += 1

  if n % 3 == 0:
    while n % 3 == 0:
      n = n // 3
      b += 1

  if n % 2 == 0:
    while n % 2 == 0:
      n = n // 2
      a += 1

  print("#{} {} {} {} {} {}".format(t+1, a, b, c, d, e)) 


# sol2
test_case = int(input())
num_list = [2, 3, 5, 7, 11]

for t in range(test_case):
  n = int(input())
  
  answer = []
  for num in num_list:
    k = 0
    if n % num == 0:
      while n % num == 0:
        n = n // num
        k += 1
      answer.append(k)
    else:
      answer.append(0)

  print('#{} {} {} {} {} {}'.format(t+1, answer[0], answer[1], answer[2], answer[3], answer[4]))
      
