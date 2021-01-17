n  = int(input())
num = []
for i in range(n):
    m = list(map(int,input().split()))
    avg = sum(m[1:]) / m[0]    # 리스트 슬라이싱
    num = 0                    # 평균 이상의 수
    for j in m[1:]:
        if j > avg:
            num += 1

    rate = num / m[0] * 100     # m[0]으로 나누면 되는구나
    print(f'{rate:.3f}%')     # f-string, 소수점자릿수