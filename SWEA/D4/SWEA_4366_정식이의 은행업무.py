
# 이진수 십진수로 변환
def two_to_ten(arr):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (2**(len(arr)-1-i))
    return ans

# 삼진수 십진수로 변환
def three_to_ten(arr):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (3**(len(arr)-1-i))
    return ans

# 경우 따지기
def sol():
    global result

    # 이진수
    for i in range(len(two)):
        if two[i]:      # 1이면
            two_n = two[:]
            two_n[i] = 0
            result.add(two_to_ten(two_n))
        if not two[i]:      # 0이면
            two_n = two[:]
            two_n[i] = 1
            result.add(two_to_ten(two_n))

    # 3진수
    for j in range(len(three)):
        vis = [0] * 3           # 0, 1, 2
        vis[three[j]] = 1       # 방문체크
        for k in range(3):      # 0, 1, 2
            if not vis[k]:      # 방문 안한 곳이면
                three_n = three[:]
                three_n[j] = k
                temp = three_to_ten(three_n)
                if temp in result:
                    return temp
                else:
                    continue

T = int(input())
for tc in range(1, T+1):
    two = list(map(int, input()))
    three = list(map(int, input()))

    result = set()
    print('#{} {}'.format(tc, sol()))

