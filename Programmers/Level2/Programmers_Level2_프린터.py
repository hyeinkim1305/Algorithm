
def solution(priorities, location):
    cnt = 0                                              # 몇 번째로 인쇄되는지

    while priorities:
        p = priorities.pop(0)                            # 가장 첫 번째 원소 꺼내고

        for i in range(len(priorities)):
            if priorities[i] > p:                        # 우선순위가 더 큰게 있으면
                priorities.append(p)
                if location == 0:                        # location도 뒤로 보냄
                    location += (len(priorities) - 1)
                else:
                    location -= 1
                break
        else:                                             # 가중치가 더 큰거 없을 때
            if location == 0:
                return cnt +1
            else:
                location -= 1
                cnt += 1


'''
[ 다른풀이도 공부 ]
* 새로 배운 점 : enumerate, any

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]          # 이런 표현이 나는 익숙치 않은듯!
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1]<q[1] for q in queue):                     # wow!!
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''