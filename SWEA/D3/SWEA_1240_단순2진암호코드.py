
def find_code():
    for i in range(N):
        for j in range(M-1, -1, -1):
            if int(data[i][j]):
                info = data[i][j-(7*8)+1:j+1]
                return info

T = int(input())
pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    code = find_code()

    # 패턴 숫자 찾기
    ans = []
    for i in range(8):
        temp = code[i*7:(i*7)+7]
        for j in range(10):
            if temp == pattern[j]:
                ans.append(j)

    # 암호 코드 계산
    odd_sum, even_sum, detec = 0, 0, 0
    for k in range(8):
        if k == 7:
            detec = ans[k]
        elif not k % 2:
            odd_sum += ans[k]       # 홀수 합
        elif k % 2:
            even_sum += ans[k]      # 짝수 합
    secret = odd_sum * 3 + even_sum + detec

    # 암호코드 정상 비정상 판별
    if not secret % 10:
        result = sum(ans)
    else:
        result = 0

    print(f'#{tc} {result}')

