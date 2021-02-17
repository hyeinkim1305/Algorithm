
'''
2칸씩 이동하면서 채우기
카운팅정렬로 일단 정렬을 다 하고
채우기
'''

T = int(input())
for tc in range(1, T+1):

    N = int(input())  # 정수의 개수
    M = 10   # 특별히 정렬된 숫자 리스트 길이

    number = list(map(int, input().split()))  # 입력력
    cnt = [0 for _ in range(101)]  # 카운팅정렬에서 숫자 인덱스 개수

    number_sort = []  # 정렬된 숫자들
    ans = [0 for _ in range(M)]  # 특별한 정렬을 담을 리스트

    # 숫자들 개수 세고 정렬
    for n in number:
        cnt[n] += 1
    for c in range(1, len(cnt)):
        while cnt[c] != 0:  # 중복된 숫자가 있을 수도 있으므로 while문
            number_sort.append(c)
            cnt[c] -= 1

    # 큰 숫자들부터 2칸씩 번갈아가며 넣기
    k = 0
    for i in range(-1, -(M//2+1), -1):
        ans[k] = number_sort[i]
        k += 2
    # 작은 숫자들부터 2칸씩 번갈아가며 넣기
    k = 1
    for j in range(M//2):
        ans[k] = number_sort[j]
        k += 2

    print('#{} {}'.format(tc, ' '.join(map(str, ans))))


