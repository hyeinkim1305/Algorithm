mul = 1
for i in range(3):
    a = int(input())
    mul = a * mul

ans = str(mul)

# 문자 개수 세기
for i in range(0,10):
    num = ans.count(str(i))  # str 문자열 처리 주의
    print(num)


