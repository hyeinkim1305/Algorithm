# 몇 번째 줄에 있는지 먼저 알고, 그 줄 안에서 해결
num = int(input())
n = 1

# 한 줄당 개수를 num에서 빼며 그 값이 0이 되기 전까지 실행
while (num -  n) > 0:
    num -= n
    n += 1

# num과 줄넘버 n이 나옴
# 홀수줄 일 때, 짝수줄 일 때 나눠서 출력
if n % 2 ==1:
    print(f'{n-num+1}/{num}')
else:
    print(f'{num}/{n-num+1}')




