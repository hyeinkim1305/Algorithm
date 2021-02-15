
while True:
    length = list(map(int, input().split()))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break
    for i in range(len(length)-1, 0, -1):
        for j in range(i):
            if length[j] > length[j+1]:
                length[j], length[j+1] = length[j+1], length[j]
    if length[0]**2 + length[1]**2 == length[2]**2:
        print('right')
    else:
        print('wrong')



