
# sol1
number = list(map(int,input()))

# 리스트 오름차순 정렬하고 뒤집는다.
number = sorted(number)
number.reverse()

for n in number:
    print(n,end='')



# sol2
number = list(map(int,input()))

number.sort(reverse=True)

for n in number:
    print(n,end='')


