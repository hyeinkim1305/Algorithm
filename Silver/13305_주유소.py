
'''
더 작은 숫자를 발견하면 그거로 바꾸고 이전까지 거리를 이전 숫자에 곱한다.
처음에 min을 5로 하고 크면 패스하고
끝까지 가면 지금까지 거리에 오일가격 곱해서 더하기
'''

N = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))
min_oil = oil[0]
min_i = 0
cost = 0
for i in range(len(oil)):
    if i+1 == len(oil) -1:
        cost += min_oil * sum(length[min_i:i+1])
        break
    if oil[i+1] < min_oil:
        cost += min_oil * sum(length[min_i:i+1])
        min_i = i+1
        min_oil = oil[i+1]
    else:
        continue

print(cost)
