
def solution(dartResult):
    answer = []

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                ans = 10
                continue
            elif dartResult[i] == '0' and dartResult[i-1] == '1':
                ans = 10
                continue
            ans = int(dartResult[i])
            continue

        elif not dartResult[i].isdigit():
            if dartResult[i] == 'S':
                answer.append(ans**1)
            elif dartResult[i] == 'D':
                answer.append(ans**2)
            elif dartResult[i] == 'T':
                answer.append(ans**3)
            elif dartResult[i] == '#':
                answer[-1] = answer[-1] * -1
            elif dartResult[i] == '*':
                if len(answer) >= 2:
                    answer[-2] = answer[-2] * 2
                    answer[-1] = answer[-1] * 2
                else:
                    answer[-1] = answer[-1] * 2

    return sum(answer)

# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
print(solution('1D2S3T*'))




# def solution(dartResult):
#     # start의 위치는 숫자에 놓기
#     answer = 0
#     start, end = 0, 1
#     while start <= len(dartResult)-1 and end <= len(dartResult)-1:
#         # 숫자가 아니라면
#         if not dartResult[end].isdigit():
#             if dartResult[end] == 'S':
#                 ans = int(dartResult[start]) ** 1
#             elif dartResult[end] == 'D':
#                 ans = int(dartResult[start]) ** 2
#             elif dartResult[end] == 'T':
#                 ans = int(dartResult[start]) ** 3
#             elif dartResult[end] == '#':
#                 ans *= -1
#                 answer += ans
#                 ans = 0
#             elif dartResult[end] == '*':
#                 answer += ans
#                 answer *= 2
#                 ans = 0
#                 start = end + 1
#                 end += 1
#             end += 1
#         elif dartResult[end].isdigit():
#             answer += ans
#             ans = 0
#             start = end
#             end += 1
#     if ans:
#         answer += ans
#
#     return answer


