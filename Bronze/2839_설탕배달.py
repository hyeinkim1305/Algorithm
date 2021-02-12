
sugar = int(input())
# 봉지 수
cnt = -1

if sugar < 5:
    if sugar % 3 == 0:
        cnt = sugar // 3
    else:
        cnt = -1
else:
    if sugar % 5 == 0:
        cnt = sugar // 5
    elif sugar % 5 != 0:
        # 5의 배수로 나눌 범위 구하기
        number = sugar // 5
        for i in range(number, -1, -1):
            if (sugar - (5*i)) % 3 == 0:
                cnt = i + ((sugar - (5*i)) // 3)
                break

print(cnt)