
# 중복가능한 순열 + j를 인자로 추가함으로써 연산횟수?줄임
def cnt(idx, j):
    global answer
    if idx == N:
        answer.append(sum(ans))
    else:
        for i in range(j, 4):
            ans[idx] = roma[i]
            cnt(idx+1, i)

N = int(input())
roma = [1, 5, 10, 50]

ans = [0] * N
answer = []
cnt(0, 0)
print(len(set(answer)))


# 순열 구하는 코드 (참고)
# arr = [1, 2, 3]
# N = 3
# sel = [0] * 2  # 결과들이 저장될 리스트
# check = [0] * N  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크
#
#
# def perm(idx):
#     # 다 뽑아서 정리했다면,
#     if idx == 2:
#         print(sel)
#         return
#     else:
#         for i in range(N):
#                 sel[idx] = arr[i]  # 값을 써라-
#                 perm(idx + 1)
# perm(0)