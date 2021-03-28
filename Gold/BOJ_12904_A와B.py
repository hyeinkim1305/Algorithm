
def change(s, t):
    while len(t) >= len(s):
        if t == s:
            return 1
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1][::-1]
    return 0


S = input()
T = input()
print(change(S, T))



# s -> t로 풀이 / 시간 초과 나옴
# def change(s, t):
#     q = [s]
#
#     while q:
#         cur = q.pop(0)
#         if cur == t:
#             return 1
#         if len(cur) <= len(t):
#             q.append(cur+'A')
#             q.append(''.join(reversed(cur))+'B')
#         else:
#             break
#     return 0
#
# # BFS로 풀기
# S = input()
# T = input()
# print(change(S, T))





