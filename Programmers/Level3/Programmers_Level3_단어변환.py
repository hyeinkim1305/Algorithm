
# words를 돌면서 바꿀 수 있으면 바꾸고 그때 최소 cnt값을 구해준다
def dfs(begin, target, words, cnt, visited):
    global min_cnt
    if begin == target:
        if cnt < min_cnt:
            min_cnt = cnt
        return


    for i in range(len(words)):
        diff = 0
        if visited[i] == 0:
            for j in range(len(begin)):
                if begin[j] != words[i][j]:
                    diff += 1  # 스펠링 다를 때
            if diff == 1:
                visited[i] = 1
                dfs(words[i], target, words, cnt + 1, visited)
                visited[i] = 0
    return          # 다 돌았는데 바꿀 수 없을 때

def solution(begin, target, words):
    global min_cnt
    if target not in words:
        return 0
    else:
        # 글자 하나 바꾼다는게 글자 하나만 다르면 된다는것!
        visited = [0] * (len(words))
        min_cnt = 9876543213
        dfs(begin, target, words, 0, visited)
        return min_cnt

# solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])


'''
# zip 함수 활용해도 될 듯
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')


>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for i in range(3):
...     pair = (numbers[i], letters[i])
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
'''