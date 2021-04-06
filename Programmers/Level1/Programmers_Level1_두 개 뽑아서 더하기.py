

def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            result.append(numbers[i] + numbers[j])
    result = sorted(list(set(result)))
    return result