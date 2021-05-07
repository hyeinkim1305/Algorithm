'''
max_heap과 min_heap을 만들어서 시작한다.
'''
import heapq
def solution(operations):
    heap = []
    max_heap = []

    for op in operations:
        if op[0] == 'I':
            heapq.heappush(heap, int(op[2:]))
            heapq.heappush(max_heap, (-int(op[2:]), int(op[2:])))
        else:
            if len(heap) == 0:
                continue
            elif op[2] == '-':
                min_value = heapq.heappop(heap)
                max_heap.remove((-min_value, min_value))
            else:
                max_value = heapq.heappop(max_heap)
                heap.remove(max_value[1])
    if not heap:
        answer = [0, 0]
        return answer
    else:
        min_value = heapq.heappop(heap)
        max_value = heapq.heappop(max_heap)
        answer = [max_value[1], min_value]
        return answer