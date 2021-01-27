
word = input()

# 아스키코드 이용
for n in range(97,123):

    if chr(n) in word:

        num = word.count(chr(n))
        print(num,end = " ")
        
    else:
        print(0, end = " ")