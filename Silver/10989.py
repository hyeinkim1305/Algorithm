
# 카운팅정렬 해보기
import sys
N = int(sys.stdin.readline())

li = [0 for _ in range(10001)]  # 빈도수 저장 리스트
for _ in range(N):
    n = int(sys.stdin.readline())
    li[n] += 1   # 빈도수 추가

for i in range(1, 10001):   # 주어지는 숫자는 자연수
    num = li[i]
    for _ in range(num):
        print(i)


# # 카운팅정렬 해보기
# N = int(input())
#
# li = [0 for _ in range(10001)]  # 빈도수 저장 리스트
# number = []
# for _ in range(N):
#     n = int(input())
#     number += [n]   # 정렬해야하는 수 리스트
#     li[n] += 1   # 빈도수 추가

# for i in range(len(li)):
#     if i == 0:
#         li[i] = li[i]
#     else:
#         li[i] = li[i] + li[i-1]
#
# # 이 부분 오류 해결해보기
# output = [0 for _ in range(N)]
# for j in range(N, -1, -1):
#     output[li[number[j]]] = number[j]
#     li[number[j]] -= 1
#
# print(output)







