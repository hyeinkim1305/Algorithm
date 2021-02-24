
# 정사각행렬
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 행렬크기
    number = []
    for i in range(N):  # 입력 값들을 한 리스트에 담음
        num = input().split()
        number.append(num)
    ans = []

    ans1 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans1[j][N-1-i] = number[i][j]
    ans.append(ans1)

    ans2 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans2[j][N-1-i] = ans1[i][j]
    ans.append(ans2)

    ans3 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans3[j][N - 1 - i] = ans2[i][j]
    ans.append(ans3)

    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            print(''.join(ans[j][i]),end=" ")
        print()








'''
헷갈린것
arr = [[[1, 2, 3],[4,5,6],[7,8,9]],[[1, 7, 3],[1,4,6],[7,7,9]]]
a = [[2,3,6],[3,5,7],[9,2,5]]
for i in range(3):
    for j in range(2):
        for k in arr[j][i]:
            print(k, end='')
        print(end=" ")
    print()
'''


