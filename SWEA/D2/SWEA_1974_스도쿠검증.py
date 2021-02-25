# 행검사
def row(puzzle):
    for i in range(9):  # 행
        zero = [0] * 10
        for j in range(9):  # 열
            zero[puzzle[i][j]] += 1
        for k in range(1, 10):
            if zero[k] != 1:
                return False   # 겹치는 숫자가 있거나 0이거나 하면 False
    return True
# 열검사
def col(puzzle):
    for i in range(9):   # 열
        zero = [0] * 10
        for j in range(9):
            zero[puzzle[j][i]] += 1
        for k in range(1, 10):
            if zero[k] != 1:
                return False
    return True
# 사각형 검사
def rec(puzzle):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            zero = [0] * 10
            for k in range(3):
                for l in range(3):
                    zero[puzzle[i+k][j+l]] += 1
                    if zero[puzzle[i+k][j+l]] > 2:
                        return False
            for k in range(1, 10):
                if zero[k] != 1:
                    return False
    return True

T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    zero = [0] * 10

    if row(puzzle) == True and col(puzzle) == True and rec(puzzle) == True:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

'''
10
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9'''
