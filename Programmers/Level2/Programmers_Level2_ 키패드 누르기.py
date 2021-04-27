# 숫자 2, 5, 8, 0이 들어왔을 때 작동하는 함수
def mid(n, left, right, hand, keypad):
    left_d = abs(keypad[left][0] - keypad[n][0]) + abs(keypad[left][1] - keypad[n][1])
    right_d = abs(keypad[right][0] - keypad[n][0]) + abs(keypad[right][1] - keypad[n][1])

    if left_d < right_d:
        return 'L'
    elif left_d > right_d:
        return 'R'
    else:
        if hand == 'right':
            return 'R'
        elif hand == 'left':
            return 'L'


def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    # 초기상태
    left, right = '*', '#'
    for n in numbers:
        # 1, 4, 7 일 때
        if n % 3 == 1:
            answer += 'L'
            left = n
        # 3, 6, 9 일 때
        elif n != 0 and n % 3 == 0:
            answer += 'R'
            right = n
        # 2, 5, 8, 0 일 때
        elif n == 0 or n % 3 == 2:
            result = mid(n, left, right, hand, keypad)
            if result == 'L':
                answer += 'L'
                left = n
            elif result == 'R':
                answer += 'R'
                right = n
    return answer

# '''
# n을 3으로 나눈 나머지는 왼쪽인지 오른쪽인지 가운데인지 분별해줌
# n을 3으로 나눈 몫은 위치를 알려줌 (0, 1, 2)
# '''
# def solution(numbers, hand):
#     answer = ''
#     left, right = 0, 0
#     for n in numbers:
#         if n % 3 == 1:
#             answer += 'L'
#             left = n // 3
#         elif n % 3 == 0:
#             answer += 'R'
#             right = n // 3 - 1          # 통일성을 주기 위해 -1을 한다
#         elif n % 3 == 2:
#             mid = n // 3
#             if abs(left-mid) > abs(right-mid):
#                 answer += 'R'
#             elif abs(left-mid) < abs(right-mid):
#                 answer += 'L'
#             else:
#                 if hand == 'right':
#                     answer += 'R'
#                 else:
#                     answer += 'L'
#     return answer


# # 몇 번째 손가락인지 판단
# def finger(idx):
#     if idx in


# def solution(numbers, hand):
#     answer = ''

#     # 키패드 만들기
#     key = [[0] * 3 for _ in range(3)]
#     cnt = 1
#     for i in range(3):
#         for j in range(3):
#             key[i][j] = cnt
#             cnt += 1
#     key.append([0, 0, 0])

#     #
#     for i in numbers:
#         finger(i

#     print(key)

#     return answer