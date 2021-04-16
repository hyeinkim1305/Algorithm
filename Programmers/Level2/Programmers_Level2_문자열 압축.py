
# 아하 스택 생각하고 하면 될 듯

def solution(s):
    min_result = 987654

    # 만약 길이가 1일 때 고려
    if len(s) == 1:
        min_result = 1
    else:
        # 문자열 자르기
        for i in range(1, len(s)//2+1):
            ans = []
            for j in range(len(s)//i):
                ans.append(s[j*i:j*i+i])
            if len(s) % i != 0:
                ans.append(s[len(s)//i*i:])


            # 압축하여 표현
            idx = -1
            result = ''
            cnt = 1
            while idx >= -len(ans):
                if len(ans[idx]) != i:
                    result = ans[idx] + result
                    idx -= 1
                elif result[:i] != ans[idx] or len(result) == 0:
                    if cnt > 1:
                        result = str(cnt) + result
                        cnt = 1
                    result = ans[idx] + result
                    idx -= 1
                elif result[:i] == ans[idx]:
                    cnt += 1
                    idx -= 1
            if cnt > 1:
                result = str(cnt) + result

            if len(result) < min_result:
                min_result = len(result)
            

    return min_result



s_input = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
for s in s_input:
    print(solution(s))
