'''
r과 c는 1부터 시작
0 빈칸 1 집 2 치킨집

2개뽑아서 치킨거리 값 찾고 최소값이상을 넘어버리면 백트래킹으로 잘라버림
치킨집 : 종복허용하지 않고 순서없는 경우
'''

from itertools import combinations

N, M = map(int, input().split())
home = []
chicken = []

# 집, 치킨집 위치 찾기
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 2:
            chicken.append([i, j])
        if data[j] == 1:
            home.append([i, j])
chicken = list(combinations(chicken, M))

# 두 치킨집 당 치킨거리
# for문 활용 유의
total_distance = []
for i in range(len(chicken)):
    sum_distance = 0
    for j in range(len(home)):
        min_distance = 987654321
        for k in range(M):
            distance = abs(home[j][0] - chicken[i][k][0]) + abs(home[j][1] - chicken[i][k][1])
            if distance < min_distance:
                min_distance = distance
        sum_distance += min_distance
    total_distance.append(sum_distance)

print(min(total_distance))


'''
* combination 라이브러리 활용
print(chicken)
print(len(chicken))
print(chicken[0])
print(chicken[0][1])

[([1, 2], [2, 2], [4, 4])]
1
([1, 2], [2, 2], [4, 4])
[2, 2]
'''


# result = [0] * M       # 치킨집 뽑을 개수 만큼
# visited = [0] * len(chicken)        # 치킨집 개수 만큼

# # 치킨집 뽑기
# def chicken_cnt(idx):
#     if idx == M:
#         print(result)
#         return
#     else:
#         for i in range(M):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 result[idx] = chicken[i]
#                 chicken_cnt(idx+1)

