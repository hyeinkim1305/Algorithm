'''
sum = 2
while sum > 0:
    a,b = map(int,input().split(' '))
    sum = a + b
    print(sum)
    '''

while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
