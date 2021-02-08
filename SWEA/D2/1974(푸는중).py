
t = int(input())
for i in range(t):
    number = []
    for j in range(9):
        num = list(map(int, input().split()))
        number.append(num)

    for n in number:
        result = 0
        for k in range(9):
            if n.count(n[k]) != 1:
                result += 1
            
        if result >= 1:
            print('#{} {}'.format(i+1, 1))
            break
    
    

