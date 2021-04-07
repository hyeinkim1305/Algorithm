
def solution(new_id):
    q = []
    # 1단계
    new_id = list(new_id.lower())
    dot_cnt = 0
    # 2단계
    for i in range(len(new_id)):
        # 알파벳 소문자 판별
        if new_id[i].isalpha():        # q.append()
            q.append(new_id[i])
        elif new_id[i].isdigit():
            q.append(new_id[i])
        elif new_id[i] == '-':
            q.append(new_id[i])
        elif new_id[i] == '_':
            q.append(new_id[i])
        elif new_id[i] == '.':
            q.append(new_id[i])
    # 3단계
    ans = []
    for i in range(len(q)):
        if q[i] == '.':
            if len(ans) >= 1 and ans[-1] == '.':
                continue
            else:
                ans.append(q[i])
        else:
            ans.append(q[i])
    # 단계 4
    if ans[0] == '.':
        ans.pop(0)
    if len(ans) >= 1 and ans[-1] == '.':
        ans.pop(-1)

    # 단계 5
    if not len(ans):
        ans.append('a')
    # 단계 6
    if len(ans) >= 16:
        ans = ans[:15]
        if ans[-1] == '.':
            ans.pop(-1)
    # 단계 7
    if len(ans) <= 2:
        temp = ans[-1]
        while len(ans) < 3:
            ans += temp

    return ''.join(ans)

inputdata = ["...!@BaT#*..y.abcdefghijklm","z-+.^.","=.=","123_.def","abcdefghijklmn.p"]
for new_id in inputdata:
    print(solution(new_id))
# 결과
# "bat.y.abcdefghi"
# "z--"
# "aaa"
# "123_.def"
# "abcdefghijklmn"

'''
(다른 사람 풀이 공부)
1. 단계2
나는 하나씩 판별해줬지만 
for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
이렇게도 할 수 있다.
2. 단계3
while '..' in answer:
        answer = answer.replace('..', '.')
이런 신박한 방법도 있다!! (결국 반복되는거 지우고 하나만 남기면 되니까!) + replace 활용
3. 단계7
다시 생각해보니 temp에 answer[-1] 안 넣어도 된다!
while len(answer) < 3:
        answer += answer[-1]
'''