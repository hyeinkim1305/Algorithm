def solution(n, lost, reserve):
    # 초기화
    student = [1] * n
    # 도난당한 거 표시
    for i in range(len(lost)):
        student[lost[i] - 1] -= 1
    # 여벌있는 거 표시
    for j in range(len(reserve)):
        student[reserve[j] - 1] += 1

    for k in range(n):
        if student[k] == 0:
            if k - 1 >= 0 and student[k - 1] == 2:
                student[k - 1] -= 1
                student[k] += 1
            elif k + 1 <= n - 1 and student[k + 1] == 2:
                student[k + 1] -= 1
                student[k] += 1
            else:
                continue

    cnt = 0
    for l in student:
        if l != 0:
            cnt += 1
    return cnt


n = 3
lost = [3]
reserve = [1]
solution(n, lost, reserve)
'''
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''