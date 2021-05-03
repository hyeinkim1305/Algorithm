# heapq를 이용하는데 최대힙이므로 넣는 수에 -를 취한다.
import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        # 배열이 비어있다면
        if not heap:
            print(0)
        else:
            ans = heapq.heappop(heap)
            print(-ans)
    else:
        heapq.heappush(heap, -x)



