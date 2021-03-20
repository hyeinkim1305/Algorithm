
def cal(a, end, s, op1, op2, op3, op4):        # a 시작인덱스 end 끝인덱스 signs 연산자들 s 지금까지합
    global max_s
    global min_s
    if a == end:        # 연산자 끝까지 왔을 때
        if s > max_s:
            max_s = s
        if s < min_s:
            min_s = s
        return

    else:
        if op1 > 0:
            cal(a+1, end, s+num[a], op1-1, op2, op3, op4)
        if op2 > 0:
            cal(a+1, end, s-num[a], op1, op2-1, op3, op4)
        if op3 > 0:
            cal(a+1, end, s*num[a], op1, op2, op3-1, op4)
        if op4 > 0:
            if (s < 0 and num[a] > 0) or (s > 0 and num[a] < 0):
                ss = abs(s) // abs(num[a]) * (-1)
                cal(a+1, end, ss, op1, op2, op3, op4-1)
            elif (s < 0 and num[a] < 0):
                ss = abs(s) // abs(num[a])
                cal(a+1, end, ss, op1, op2, op3, op4-1)
            else:
                cal(a+1, end, s//num[a], op1, op2, op3, op4-1)

N = int(input())        # 수의 개수
num = list(map(int, input().split()))       # 숫자들
op = list(map(int, input().split()))      # 연산자들
max_s = -1000000001
min_s = 1000000001

cal(1, N, num[0], op[0], op[1], op[2], op[3])
print(max_s)
print(min_s)




