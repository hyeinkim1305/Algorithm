
# 메모이제이션 기법 활용
def solution(triangle):
    # 리스트 만들기
    tri = [[0] + t + [0] for t in triangle]

    for i in range(1, len(tri)):
        for j in range(1, len(tri[i]) - 1):
            tri[i][j] = max(tri[i - 1][j - 1] + tri[i][j], tri[i - 1][j] + tri[i][j])

    return max(tri[-1])


''' 이렇게 풀면 시간 초과 발생! dfs로 풀었으니 당연한 결과
# r : 행, c: 열, total : 총합
def dfs(r, c, total, triangle, vis):
    global max_total

    # 끝까지 도달하면
    if r == len(triangle):       
        if total > max_total:
            max_total = total
        return

    # 자신의 열, 자신의 열 +1 두가지 경우 가능
    for i in range(c, c+2):        
        # 여기서 i범위를 정의안하면 인덱스에러 발생함!!*****
        if 0 <= i < len(triangle[r]) and not vis[r][i]:
            vis[r][i] = 1
            dfs(r+1, i, total+triangle[r][i], triangle, vis)
            vis[r][i] = 0


def solution(triangle):
    global max_total

    # 방문배열
    vis = [[0] * i for i in range(1, len(triangle)+1)]
    max_total = -1

    dfs(0, 0, 0, triangle, vis)
    return max_total
'''