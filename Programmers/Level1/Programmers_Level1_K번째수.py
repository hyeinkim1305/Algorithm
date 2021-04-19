
def solution(array, commands):
    result = []
    for i, j, k in commands:
        ans = sorted(array[i-1:j])
        result.append(ans[k-1])
    return result


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

