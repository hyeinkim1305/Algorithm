
def function1(arr1):
    global min_num
    arr2 = set(i for i in range(1, N+1)) - set(arr1)
    arr2 = list(arr2)
    if min_num > abs(function2(arr1)-function2(arr2)):
        min_num = abs(function2(arr1)-function2(arr2))



def function2(array):
    arr_s = 0
    for i in array:
        for j in array:
            arr_s += arr[i-1][j-1]
    return arr_s


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_num = 123456789
nn = 1      # 가짓수
for i in range(N, N//2, -1):
    nn = nn * i
for j in range(1, N//2+1):
    nn = nn // j


# 팀1 경우의 수인데 겹치는거 빼고
team = []
cnt = 0
for i in range(1<<N):
    ans = []
    for j in range(N):
        if i & (1<<j):
            ans.append(j+1)

    if len(ans) == N // 2:
        team.append(ans)
        cnt += 1
    if cnt == nn // 2:
        break


for k in range(len(team)):
    function1(team[k])

print(min_num)