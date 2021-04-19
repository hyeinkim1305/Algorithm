'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''


def divide(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = divide(a[:mid])
    right = divide(a[mid:])

    return merge(left, right)

def merge(left, right):
    global count

    # 길이 말고 인덱스로
    lindex, rindex = len(left), len(right)
    ldx, rdx = 0, 0      # 각 인덱스
    result = []    # 정렬 결과

    if left[-1] > right[-1]:
        count += 1

    while ldx < lindex or rdx < rindex:
        if ldx < lindex and rdx < rindex:
            if left[ldx] <= right[rdx]:
                result.append(left[ldx])        # 더 작은거를 결과 리스트에 넣고
                ldx += 1                        # 인덱스 증가
            else:
                result.append(right[rdx])
                rdx += 1
        elif ldx < lindex:          # 오른쪽꺼는 끝나고 왼쪽꺼 남았을 때
            result.append(left[ldx])
            ldx += 1
        elif rdx < rindex:
            result.append(right[rdx])
            rdx += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    count = 0

    result = divide(a)
    print(f'#{tc} {result[N//2]} {count}')
