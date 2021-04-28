'''
result.append(f'{user[i[1]]}님이 들어왔습니다.')
풀 때 따옴표 잘못 넣어서 에러있었음!
'''

def solution(record):
    result = []

    # 유저당 닉네임 키밸류로 저장
    user = {}
    for r in record:
        r = list(r.split())
        if r[0] == 'Enter':
            user[r[1]] = r[2]
        elif r[0] == 'Change':
            user[r[1]] = r[2]

    # 순회하면서 result만들기
    for i in record:
        i = list(i.split())
        if i[0] == 'Enter':
            result.append(f'{user[i[1]]}님이 들어왔습니다.')
        elif i[0] == 'Leave':
            result.append(f'{user[i[1]]}님이 나갔습니다.')

    return result