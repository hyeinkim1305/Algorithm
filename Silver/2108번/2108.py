import sys
from collections import Counter

T = int(sys.stdin.readline())
number_list = []
for i in range(T):
    n = int(sys.stdin.readline())
    number_list.append(n)

number_len = len(number_list)
number_list_s = sorted(number_list)

# 산술평균
# 소수점 첫째자리에서 반올림한다. 
number_avg = int(round(sum(number_list) / number_len, 0))  

# 중간값
number_mid = (sorted(number_list))[number_len // 2]

# 최빈값
number_counter = Counter(number_list_s).most_common()
# 숫자가 하나이면 그 숫자를 최빈값으로 한다.
if len(number_list_s) == 1:
    number_mode = n
else:
    if number_counter[0][1] == number_counter[1][1]:
        number_mode = number_counter[1][0]
    else:
        number_mode = number_counter[0][0]

# 범위
number_range = number_list_s[-1] - number_list_s[0]


print(number_avg)
print(number_mid)
print(number_mode)
print(number_range)
