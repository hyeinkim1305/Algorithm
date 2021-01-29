
n = int(input())

# 이중 리스트 위해 생성
student_list = []

# 입력값 리스트에 넣는다.
for i in range(n):
    s = list(map(int,input().split())) 
    student_list.append(s)        #[[34,45],[234,45],[34,4]] 이런 형식

rank_list = []
for j in range(len(student_list)):
    # 기본 rank는 1로 설정
    rank = 1
    # 조건에 맞으면 rank에 1을 더한다
    for k in range(len(student_list)):
        if (student_list[j][0] < student_list[k][0]) and (student_list[j][1] < student_list[k][1]):
            rank += 1
    # rank리스트에 넣는다.
    rank_list.append(rank)

for r in rank_list:
    print(r, end = " ")
