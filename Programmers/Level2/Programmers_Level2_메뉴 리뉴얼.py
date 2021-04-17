
# combinations 활용 잘 보기!

from itertools import combinations

def solution(orders, course):
    result = []
    for i in course:
        ans = {}
        for j in orders:
            for k in combinations(j, i):
                temp = ''.join(sorted(k))
                if temp in ans:
                    ans[temp] += 1
                if temp not in ans:
                    ans[temp] = 1
        if len(ans) != 0:
            max_num = max(list(ans.values()))
            if max_num >= 2:
                for l in ans:
                    if ans[l] == max_num:
                        result.append(l)

    return sorted(result)


# 시간 초과 코드
'''
def perm(idx, n, m, sel, check, orders, person):
    global dic
    if idx == n:
        # print(sel)
        temp = ''.join(sorted(sel))
        if temp in dic:
            dic[temp] += 1
    else:
        for i in range(m):
            if check[i] == 0:
                check[i] = 1
                sel[idx] = orders[i]
                perm(idx+1, n, m, sel, check, orders, person)
                check[i] = 0



def solution(orders, course):
    dic = {}
    for j in range(len(course)):
        for i in range(len(orders)):
            sel = [0] * course[j]
            check = [0] * len(orders[i])
            perm(0, course[j], len(orders[i]), sel, check, orders[i], i+1)      # 여기서 i+1은 몇번째 손님인지
            # n = course[j], m = orders[i]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])

# ORDERS = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
# COURSE = [[2,3,4], [2,3,5], [2,3,4]]
# for i in range(3):
#     solution(ORDERS[i], COURSE[i])

# dic = {'s': 4, 't': 6, 'e': 9, 's': 2}
# n = max(list(dic.values()))
# for i, j in dic.items():
#     if j == n:
#         print(i, j)
'''
