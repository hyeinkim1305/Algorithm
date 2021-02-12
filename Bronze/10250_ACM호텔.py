
# 테스트 케이스
T = int(input())

for tc in range(T):
    # 데이터받기
    H, W, N = map(int, input().split())
    # 초기화
    number = 0
    level = 0

    if N % H == 0:
        # 방 호수
        number = N // H
        # 방 층
        level = H
    else:
        number = N // H + 1
        level = N % H

    if number < 10:
        output = str(level)+'0'+str(number)
    else:
        output = str(level) + str(number)

    print(output)

