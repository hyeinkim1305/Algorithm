
# 푸는데 시간이 좀 걸렸음!

def dfs(idx, numbers, target, total):
    global cnt

    if idx == len(numbers):
        if total == target:
            cnt += 1
        return
    else:
        dfs(idx+1, numbers, target, total+numbers[idx])
        dfs(idx+1, numbers, target, total-numbers[idx])     # 여기로 올 땐 다시 idx로 돌아오니까 idx+1해줘야함

def solution(numbers, target):
    global cnt

    cnt = 0
    dfs(0, numbers, target, 0)
    return cnt

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))


'''
** 다른 풀이

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''
