# import sys
# sys.stdin = open("input.txt","r")

# 가로 검색
def row(table):
    output = -654
    for i in range(4):   # 전체 행 순회
        for j in range(4,0,-1):  # 회문의 가능한 길이
            for k in range(4-j+1):  # 가능한 검사 횟수
                cnt = 0
                for l in range(int(j//2)):  # 회문인지 검사
                    if table[i][k+l] == table[i][k+j-(l+1)]:
                        cnt += 1
                if cnt == int(j//2):
                    if j > output:   # 여기를 j로 안하고 cnt로 해서 한참 헤맸다!
                        output = j
    return output

def col(table):
    output = -654
    for i in range(4):   # 전체 열 순회
        for j in range(4, 0, -1):
            for k in range(4-j+1):
                cnt = 0
                for l in range(int(j//2)):
                    if table[k+l][i] == table[k+j-(l+1)][i]:
                        cnt += 1
                if cnt == int(j//2):
                    if j > output:
                        output = j
    return output


for tc in range(1, 11):
    testcase = int(input())
    table = [list(input()) for _ in range(4)]

    if row(table) > col(table):
        print("#{} {}".format(tc, row(table)))
    else:
        print("#{} {}".format(tc, col(table)))



