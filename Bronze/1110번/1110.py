
# 문자열로 풀어서 시간초과가 생긴듯하다
'''
 n = input()
 if len(n) == 1:
     n = '0'+ n
 count = 0
 while True:
     sum = str(int(n[0]) + int(n[1]))
     new = n[1] + sum[-1]
     count += 1
     if new == n:
         break
 print(count)
 '''

 # 숫자로 푼 풀이 알아두기
num = n = int(input())
count = 0
while True:
    ten = num //10
    one = num % 10
    total = ten + one
    count += 1
    num = int(str(num % 10)+ str(total % 10))   
    if (n == num):
        break
print(count)