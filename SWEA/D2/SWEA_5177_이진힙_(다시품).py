'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

def insert(num):
    heap.append(num)
    idx = len(heap) - 1

    while idx > 0:
        parent = idx // 2
        if heap[parent] > heap[idx]:
            heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data_list = list(map(int, input().split()))
    heap = [0]

    for data in data_list:
        insert(data)

    ans = 0
    ans_idx = N // 2
    while ans_idx > 0:
        if ans_idx:
            ans += heap[ans_idx]
            ans_idx //= 2

    print(f'#{tc} {ans}')





