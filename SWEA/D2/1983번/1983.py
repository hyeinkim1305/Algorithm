
T = int(input())


level = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

# for문을 돌면서 학생들의 총점과 번호를 리스트에 넣는다.
for j in range(T):
  N, K = map(int, input().split())
  students_list = []
  for i in range(1,N+1):
    student_list = []
    a, b, c = map(int, input().split())
    score = round(a * 0.35 + b * 0.45 + c * 0.2, 1)
    student_list.extend([i, score])
    students_list.append(student_list)

  students_list_s = sorted(students_list, key = lambda x : -x[1])


  for k in range(N):
    if students_list_s[k][0] == K:
      level_position = (k / (N / 10)) 
      
      print('#{} {}'.format(j+1, level[level_position]))








