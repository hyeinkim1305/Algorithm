#  30의 배수는 자리 수를 다 더해서 3의 배수가 되고, 맨 끝자리가 0이면 된다.

number = input()

ans = 0
for n in number:
    ans += int(n) 

if ('0' not in number) or (ans % 3 != 0):
    print(-1)
else:
    number_s = sorted(list(number),reverse=True)
    print(''.join(number_s))




