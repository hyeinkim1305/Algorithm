
# 369개수의 합만큼 -의 개수를 출력하면됨.
# 푸는데 시간이 좀 걸렸음

n = int(input())

for i in range(1,n+1):
    ans = 0
    ans += str(i).count('3') + str(i).count('6') + str(i).count('9')
    if ans != 0:
        print('-'*ans, end = ' ')
    else:
        print(i,end=" ")