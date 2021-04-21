
'''
다리가 q라고 생각!
아이디어 잘 보기!!
'''
## 처음에 풀이 방식 생각하는데에 시간이 걸림!

def solution(bridge_length, weight, truck_weights):

    q = [0] * bridge_length
    time = 0
    while q:
        time += 1
        q.pop(0)        # 길이가 변하는구나
        if not truck_weights:
            continue
        elif sum(q) + truck_weights[0] <= weight:
            q.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            q.append(0)
    return time


# solution(2, 10, [7,4,5,6])
# solution(100, 100, [10])
solution(100, 100, [10,10,10,10,10,10,10,10,10,10])


