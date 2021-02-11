
'''
A : 고정 비용
B : 가변 비용
C : 노트북가격
손익분기점 : 총 수입이 고정비용 + 가변비용의 총 비용을 넘어가는 순간
'''

A, B, C = map(int, input().split())

if C- B <= 0:
    print('-1')
else:
    output = (A // (C - B)) + 1
    print(output)