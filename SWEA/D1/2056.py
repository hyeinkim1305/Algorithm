
# 주의할점 : 리스트형태를 int로 바꾸는 거를 했음 ! 이러지 말기
# 문자열에서도 리스트처럼 할 수 있는거 상기하기!
t = int(input())
for i in range(t):
    
    # 문자열로 받는다
    s = input()

    if ((int(s[4:6]) >= 1) and (int(s[4:6]) <= 12)):
        if (int(s[4:6]) == 2):
            if ((int(s[6:])) >=1 and (int(s[6:])) <= 28):
                print('#{0} {1}/{2}/{3}'.format((i+1), (s[0:4]), (s[4:6]), (s[6:])))
            else:
                print('#{} -1'.format(i+1))

        elif (int(s[4:6]) == 4) or (int(s[4:6]) == 6) or (int(s[4:6]) == 9) or (int(s[4:6]) == 11):
            if ((int(s[6:])) >=1 and (int(s[6:])) <= 30):
                print('#{0} {1}/{2}/{3}'.format((i+1), (s[0:4]), (s[4:6]), (s[6:])))
            else:
                print('#{} -1'.format(i+1))

        else:
            if ((int(s[6:])) >=1 and (int(s[6:])) <= 31):
                print('#{0} {1}/{2}/{3}'.format((i+1), (s[0:4]), (s[4:6]), (s[6:])))
            else:
                print('#{} -1'.format(i+1))

    else:
        print('#{} -1'.format(i+1))



# 오류 답안 - 리스트로 굳이 바꿀 필요가 없음
# t = int(input)
# for i in range(t):
    
#     # 문자열로 받는다
#     s = list(input())

#     if ((int(s[4:6]) >= 1) and (int(s[4:6]) <= 12)):
#         if (int(s[4:6]) == 2):
#             if ((int(s[6:])) >=1 and (int(s[6:])) <= 28):
#                 print('#{0} {1}/{2}/{3}'.format((i+1), (int(s[0:4])), (int(s[4:6])), (int(s[6:]))))
#             else:
#                 print('#{} -1'.format(i+1))

#         elif (int(s[4:6]) == 4) or (int(s[4:6]) == 6) or (int(s[4:6]) == 9) or (int(s[4:6]) == 11):
#             if ((int(s[6:])) >=1 and (int(s[6:])) <= 30):
#                 print('#{0} {1}/{2}/{3}'.format((i+1), (int(s[0:4])), (int(s[4:6])), (int(s[6:]))))
#             else:
#                 print('#{} -1'.format(i+1))

#         else:
#             if ((int(s[6:])) >=1 and (int(s[6:])) <= 31):
#                 print('#{0} {1}/{2}/{3}'.format((i+1), (int(s[0:4])), (int(s[4:6])), (int(s[6:]))))
#             else:
#                 print('#{} -1'.format(i+1))

#     else:
#         print('#{} -1'.format(i+1))
        
