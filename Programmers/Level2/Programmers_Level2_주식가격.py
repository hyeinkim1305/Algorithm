

def solution(prices):
    result = []
    for i in range(len(prices)):
        if i == len(prices)-1:
            result.append(0)
            break
        p = prices[i]
        cnt = 0
        idx = i + 1
        is_OK = True
        while idx <= len(prices)-1:
            if prices[idx] < p:
                cnt += 1
                result.append(cnt)
                is_OK = False
                break
            else:
                cnt += 1
                idx += 1
        if is_OK:
            result.append(cnt)
    return result


prices = [1, 2, 3, 2, 3]
print(solution(prices))