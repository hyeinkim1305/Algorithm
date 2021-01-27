
word = input()

# 아스키코드 이용
for i in range(97,123):
    if chr(i) in word:
        num = word.index(chr(i))
        print(num, end = " ")
    else:
        print( -1, end= " ")
