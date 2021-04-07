
'''
A Counter is a dict subclass for counting hashable objects.
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
** 특징 : Counter 객체들끼리 뺄셈이 가능하다
'''


import collections

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
result = collections.Counter(participant)-collections.Counter(completion)
print(result)           # 결과값Counter({'vinko': 1})
print(list(result.keys()))          # 결과값 ['vinko']
print(list(result.keys())[0])          # 결과값 vinko




# 시간 초과 풀이
# def solution(participant, completion):
#     for i in range(len(participant)):
#         for j in range(len(completion)):
#             if participant[i] == completion[j]:
#                 completion[j] = ''
#                 break
#         else:
#             answer = participant[i]
#
#     return answer

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# print(solution(participant, completion))