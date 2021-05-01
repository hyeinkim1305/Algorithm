import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    # 현재 시간
    sec = 0
    idx = 0
    # 걸린 시간 리스트
    ans = []

    while idx < len(jobs) or heap:
        for i in range(idx, len(jobs)):
            # 작업 요청시간이 현재 시간보다 작다면 작업소요시간을 앞으로 해서 넣기 (소요시간이 적은게 먼저 나오도록)
            if jobs[i][0] <= sec:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            else:
                # 다음 반복때 겹치지 않도록
                idx = i
                break
        else:
            idx = i + 1

        if heap:
            time, call = heapq.heappop(heap)
            ans.append(sec - call + time)
            sec += time
        # 비어있다면 현재 시간 증가
        else:
            sec += 1

    answer = sum(ans) // len(jobs)
    return answer

print(solution([[2, 3], [4, 6], [3, 9]]))