def distance(a, b, w, h):
    # 방향이 같을 때
    if a[0] == b[0]:
        if a[1] > b[1]:
            return a[1] - b[1]
        else:
            return b[1] - a[1]
    # 1,3 방향일 때
    if (a[0] == 1 and b[0] == 3) or (a[0] == 3 and b[0] == 1):
        return a[1] + b[1]
    # 1, 4 방향일 때
    if (a[0] ==1 and b[0] == 4) or (a[0] == 4 and b[0] == 1):
        if a[0] == 1:
            return w + b[1] - a[1]
        elif b[0] == 1:
            return w + a[1] - b[1]
    # 1, 2 방향일 때
    if (a[0] == 1 and b[0] == 2) or (a[0] == 2 and b[0] == 1):
        if (a[1] + b[1] + h) >= (w+h):
            return 2*(w+h) - (a[1] + b[1] + h)
        else:
            return a[1] + b[1] + h
    # 3, 2 방향일 때
    if (a[0] == 3 and b[0] == 2) or (a[0] == 2 and b[0] == 3):
        if a[0] == 2:
            return h + a[1] - b[1]
        elif b[0] == 2:
            return h + b[1] - a[1]
    # 2, 4 방향일 때
    if (a[0] == 2 and b[0] == 4) or (a[0] == 4 and b[0] == 2):
        return w + h - a[1] - b[1]
    # 3, 4 방향일 때
    if (a[0] == 4 and b[0] == 3) or (a[0] == 3 and b[0] == 4):
        if (w + a[1] + b[1]) >= (w+h):
            return 2*(w+h) - (w + a[1] + b[1])
        else:
            return w + a[1] + b[1]

# 가로 세로 길이
W, H = map(int, input().split())

# 상점 개수
store_cnt = int(input())

# 상점 묶음
stores = []
for _ in range(store_cnt):
    # 상점 방향, 위치
    store = list(map(int, input().split()))
    stores.append(store)

# 동근 위치
dong = list(map(int, input().split()))

# 총 최단 거리 합
output = 0

# 각 상점 사이의 최단 거리
for s in stores:
    output += distance(dong, s, W, H)

print(output)

# def check(a, b):
#     return a[0] + b[1]
# x = [6, 4]
# y = [3, 9]
# print(check(x, y))
# 결과값 15








