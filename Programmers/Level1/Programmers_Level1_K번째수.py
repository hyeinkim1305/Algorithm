

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        arr = sorted(arr)
        answer.append(arr[commands[i][2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

# 다른 풀이
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

