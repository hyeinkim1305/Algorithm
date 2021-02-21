# split을 잘 이용하면 된다.
# 처음에 런타임에러 있었음. 고려 안 한 경우가 있는지 확인하자.

number = input().split('-')
ans = 0

if len(number) == 1:   # +만 있을 경우 고려
    n = number[0].split('+')
    k = 0
    while True:
        if k == len(n):
            break
        ans += int(n[k])
        k += 1

else:
    for i in range(len(number)):
        if i == 0:
            num = number[i].split('+')
            j = 0
            while True:
                if j == len(num):
                    break
                ans += int(num[j])
                j += 1
        else:
            num = number[i].split('+')
            j = 0
            while True:
                if j == len(num):
                    break
                ans -= int(num[j])
                j += 1

print(ans)

# 헷갈렸던 것
# m = '60+12+10'.split('+')
# print(m)
# output
# ['60', '12', '10']


# sol2 좀 더 간단한 풀이
# number = input().split('-')      # 55 55+20 이런 상태
# ans = 0
#
# for i in number[0].split('+'):
#     ans += int(i)
#
# for j in number[1:]:
#     for i in j.split('+'):
#         ans -= int(i)
#
# print(ans)
