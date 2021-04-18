

def solution(s):
    s = s[2:-2].split('},{')
    arr = []
    for i in range(len(s)):     # 문자열과 {기호를 리스트 형태로 바꾼다
        temp = list(map(int, s[i].split(',')))
        arr.append(temp)
    arr = sorted(arr, key=lambda x: len(x))     # 길이별로 정렬한다.

    result = []
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if arr[j][k] not in result:
                result.append(arr[j][k])
    return result



s = "{{20,111},{111}}"
print(solution(s))