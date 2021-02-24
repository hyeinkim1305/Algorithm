
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())
    ans = [0 for _ in range(len(card))]
    n = len(card) // 2

    if len(card) % 2 == 0:    # 카드 개수가 짝수개일때
        a = card[:n]  # 앞에서부터 반만큼 슬라이싱
        b = card[n:]  # 반에서부터 끝까지 슬라이싱
        for i in range(n):  # ans의 해당 인덱스에 넣는다
            ans[i*2] = a[i]
            ans[i*2+1] = b[i]

    elif len(card) % 2 != 0:  # 카드 개수가 홀수개 일때
        a = card[:n+1]  # 한개더 넣은 만큼 슬라이싱
        b = card[n+1:]
        for i in range(n+1):
            ans[i * 2] = a[i]
        for i in range(n):
            ans[i * 2 + 1] = b[i]

    print('#{} {}'.format(tc, ' '.join(ans)))

'''
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''



