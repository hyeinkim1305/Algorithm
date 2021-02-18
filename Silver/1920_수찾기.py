
# sol1 이진탐색
def test(n, key):
    start = 0
    end = len(n) -1
    while start <= end:
        middle = int((start + end) // 2)
        if n[middle] == key:
            return 1
        elif n[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return 0    # 반복문 다 돌았는데 없으면 0이 나오게

N = int(input())
n = sorted(list(map(int, input().split())))
M = int(input())
m = list(map(int, input().split()))

for key in m:
    print(test(n, key))

# sol2 재귀
def test(n, key, start, end):
    if start > end:
        return 0
    middle = int((start + end) // 2)
    if key == n[middle]:
        return 1
    elif key < n[middle]:
        return test(n, key, start, middle-1)
    else:
        return test(n, key, middle+1, end)

N = int(input())
n = sorted(list(map(int, input().split())))
M = int(input())
m = list(map(int, input().split()))

for key in m:
    start = 0
    end = len(n) - 1
    print(test(n, key, start, end))
